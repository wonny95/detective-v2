# The button click (audio/ui-close.mp3): a soft wooden tap, one low struck note with a little knock (user pick E of the
# click mockups), standard library only.
# usage: python scripts/make-ui-click-sfx.py <out.wav>   then: ffmpeg -i <out.wav> -b:a 128k audio/ui-close.mp3
import math, random, struct, sys, wave

RATE = 44100

def wood(dur=.14, f=520):
    out = []
    random.seed(3)
    for i in range(int(dur * RATE)):
        t = i / RATE
        v = math.exp(-t * 38) * math.sin(2 * math.pi * f * t) + .3 * math.exp(-t * 90) * math.sin(2 * math.pi * f * 2.7 * t)
        knock = random.uniform(-1, 1) * math.exp(-t * 400) * .25
        out.append((v + knock) * min(1, t / .002))
    return out

if __name__ == '__main__':
    s = wood(); peak = max(abs(v) for v in s)
    with wave.open(sys.argv[1], 'wb') as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE)
        w.writeframes(b''.join(struct.pack('<h', int(v / peak * .8 * 32767)) for v in s))
    print('ok')
