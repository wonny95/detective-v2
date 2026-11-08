// Image helpers for the violin case's art scripts (scripts/cut-violin-art.ps1): PowerShell on Windows has
// System.Drawing but no Python here, so the crop/trim/icon steps of the Python cut-*.py scripts are done the same way
// in C#. Loaded with Add-Type; every method works on 32-bit ARGB bitmaps.
using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Imaging;
using System.Runtime.InteropServices;

public static class ArtTools {
  public static Bitmap Load(string path) {
    using (var src = new Bitmap(path)) {
      var bmp = new Bitmap(src.Width, src.Height, PixelFormat.Format32bppArgb);
      using (var g = Graphics.FromImage(bmp)) g.DrawImage(src, 0, 0, src.Width, src.Height);
      return bmp;
    }
  }
  static byte[] Bytes(Bitmap b, out BitmapData d) {
    d = b.LockBits(new Rectangle(0, 0, b.Width, b.Height), ImageLockMode.ReadWrite, PixelFormat.Format32bppArgb);
    var buf = new byte[d.Stride * b.Height]; Marshal.Copy(d.Scan0, buf, 0, buf.Length); return buf;
  }
  static void Put(Bitmap b, BitmapData d, byte[] buf) { Marshal.Copy(buf, 0, d.Scan0, buf.Length); b.UnlockBits(d); }
  public static Bitmap Crop(Bitmap b, int x, int y, int w, int h) {
    var o = new Bitmap(w, h, PixelFormat.Format32bppArgb);
    using (var g = Graphics.FromImage(o)) { g.CompositingMode = CompositingMode.SourceCopy; g.DrawImage(b, new Rectangle(0, 0, w, h), new Rectangle(x, y, w, h), GraphicsUnit.Pixel); }
    return o;
  }
  public static Bitmap Resize(Bitmap b, int w, int h) {
    var o = new Bitmap(w, h, PixelFormat.Format32bppArgb);
    using (var g = Graphics.FromImage(o)) {
      g.CompositingMode = CompositingMode.SourceCopy; g.InterpolationMode = InterpolationMode.HighQualityBicubic;
      g.PixelOffsetMode = PixelOffsetMode.HighQuality; g.SmoothingMode = SmoothingMode.HighQuality;
      using (var a = new ImageAttributes()) { a.SetWrapMode(WrapMode.TileFlipXY); g.DrawImage(b, new Rectangle(0, 0, w, h), 0, 0, b.Width, b.Height, GraphicsUnit.Pixel, a); }
    }
    return o;
  }
  // the box of pixels more opaque than `min`: [x, y, w, h]
  public static int[] AlphaBox(Bitmap b, int min) {
    BitmapData d; var p = Bytes(b, out d); int x0 = b.Width, y0 = b.Height, x1 = -1, y1 = -1;
    for (int y = 0; y < b.Height; y++) for (int x = 0; x < b.Width; x++) if (p[y * d.Stride + x * 4 + 3] > min) {
      if (x < x0) x0 = x; if (x > x1) x1 = x; if (y < y0) y0 = y; if (y > y1) y1 = y; }
    b.UnlockBits(d); return new[] { x0, y0, x1 - x0 + 1, y1 - y0 + 1 };
  }
  // trim to the drawing and leave a margin of `share` of its longer side (as the Python scripts' 3%)
  public static Bitmap Trim(Bitmap b, double share) {
    var r = AlphaBox(b, 24); int m = (int)Math.Round(Math.Max(r[2], r[3]) * share);
    var o = new Bitmap(r[2] + 2 * m, r[3] + 2 * m, PixelFormat.Format32bppArgb);
    using (var g = Graphics.FromImage(o)) { g.CompositingMode = CompositingMode.SourceCopy; g.DrawImage(b, new Rectangle(m, m, r[2], r[3]), new Rectangle(r[0], r[1], r[2], r[3]), GraphicsUnit.Pixel); }
    return o;
  }
  // a face icon as the other cases' (160 px: the face square scaled to 148 at 6,6, a white rim around it)
  public static Bitmap Icon(Bitmap sprite, int fx, int fy, int side) {
    var face = new Bitmap(side, side, PixelFormat.Format32bppArgb);
    using (var g = Graphics.FromImage(face)) { g.CompositingMode = CompositingMode.SourceCopy; g.DrawImage(sprite, new Rectangle(0, 0, side, side), new Rectangle(fx, fy, side, side), GraphicsUnit.Pixel); }
    var small = Resize(face, 148, 148);
    var icon = new Bitmap(160, 160, PixelFormat.Format32bppArgb);
    using (var g = Graphics.FromImage(icon)) g.DrawImage(small, 6, 6, 148, 148);
    BitmapData d; var p = Bytes(icon, out d); int S = 160; var rim = new byte[S * S];
    for (int y = 0; y < S; y++) for (int x = 0; x < S; x++) {   // dilate the drawing by 3 px
      bool on = false;
      for (int dy = -3; dy <= 3 && !on; dy++) for (int dx = -3; dx <= 3 && !on; dx++) {
        int xx = x + dx, yy = y + dy; if (xx < 0 || yy < 0 || xx >= S || yy >= S) continue;
        if (p[yy * d.Stride + xx * 4 + 3] > 40) on = true; }
      rim[y * S + x] = on ? (byte)255 : (byte)0; }
    for (int y = 0; y < S; y++) for (int x = 0; x < S; x++) {   // the rim in white under the face
      int i = y * d.Stride + x * 4; double a = p[i + 3] / 255.0, r = rim[y * S + x] / 255.0, outA = a + r * (1 - a);
      if (outA <= 0) continue;
      for (int c = 0; c < 3; c++) p[i + c] = (byte)Math.Round((p[i + c] * a + 255 * r * (1 - a)) / outA);
      p[i + 3] = (byte)Math.Round(outA * 255); }
    Put(icon, d, p); return icon;
  }
  // paste `src` onto `dst` at (x, y), its edges faded over `feather` px
  public static void PasteFeathered(Bitmap dst, Bitmap src, int x, int y, int feather) {
    BitmapData dd, sd; var dp = Bytes(dst, out dd); var sp = Bytes(src, out sd);
    for (int j = 0; j < src.Height; j++) for (int i = 0; i < src.Width; i++) {
      int edge = Math.Min(Math.Min(i, j), Math.Min(src.Width - 1 - i, src.Height - 1 - j));
      double w = feather > 0 ? Math.Min(1.0, (edge + 1.0) / feather) : 1.0;
      int si = j * sd.Stride + i * 4, di = (y + j) * dd.Stride + (x + i) * 4;
      for (int c = 0; c < 3; c++) dp[di + c] = (byte)Math.Round(dp[di + c] * (1 - w) + sp[si + c] * w); }
    src.UnlockBits(sd); Put(dst, dd, dp);
  }
  public static void SavePng(Bitmap b, string path) { b.Save(path, ImageFormat.Png); }
  public static void SaveJpg(Bitmap b, string path, long quality) {
    var enc = Array.Find(ImageCodecInfo.GetImageEncoders(), e => e.MimeType == "image/jpeg");
    var ps = new EncoderParameters(1); ps.Param[0] = new EncoderParameter(System.Drawing.Imaging.Encoder.Quality, quality);
    using (var rgb = new Bitmap(b.Width, b.Height, PixelFormat.Format24bppRgb)) {
      using (var g = Graphics.FromImage(rgb)) { g.Clear(Color.White); g.DrawImage(b, 0, 0, b.Width, b.Height); }
      rgb.Save(path, enc, ps); }
  }
}
