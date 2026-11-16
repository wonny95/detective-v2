# Cute chimes for the discovery notice (new person / new place), synthesised with the standard library only.
# usage: python scripts/make-discovery-sfx.py <out folder> [name ...]   (no names: every candidate)
import math, random, struct, sys, wave, os

RATE = 44100

def note(freq, start, dur, partials, decay, vol=1.0, bend=0.0, att=0.004):
    """one struck note: partials [(ratio, amp, decay factor)], exponential decay; bend: pitch rise over the first 60 ms"""
    out = []
    for i in range(int(dur * RATE)):
        t = i / RATE
        f = freq * (1 + bend * max(0.0, 1 - t / 0.06)) if bend else freq
        attack = min(1.0, t / att)
        v = sum(a * math.exp(-t * decay * d) * math.sin(2 * math.pi * f * r * t) for r, a, d in partials)
        out.append(vol * attack * v)
    return start, out

BELL = [(1, 1, 1), (2.0, .35, 1.8), (3.0, .12, 3), (4.2, .06, 4)]
BOX = [(1, 1, 1), (3.0, .25, 2.5), (5.0, .08, 4)]
WOOD = [(1, 1, 1), (4.0, .3, 6), (10.0, .05, 10)]
POP = [(1, 1, 1), (2.0, .2, 2)]
MARIMBA = [(1, 1, 1), (4.0, .12, 5)]        # warm, few high partials
FELT = [(1, 1, 1), (2.0, .15, 2), (3.0, .04, 3)]   # felt piano: soft and round
KALIMBA = [(1, 1, 1), (5.9, .07, 6)]

def sweep(f0, f1, start, dur, vol=1.0):
    """a bubble pop: a sine that glides from f0 up to f1 in dur, with a quick swell and fade"""
    out, ph = [], 0.0
    for i in range(int(dur * RATE)):
        t = i / RATE; x = t / dur
        f = f0 * (f1 / f0) ** (x ** .6)
        ph += 2 * math.pi * f / RATE
        out.append(vol * math.sin(ph) * min(1, t / .004) * (1 - x) ** 1.5)
    return start, out

def mix(notes, length, level=.7):
    buf = [0.0] * int(length * RATE)
    for start, s in notes:
        o = int(start * RATE)
        for i, v in enumerate(s):
            if o + i < len(buf): buf[o + i] += v
    peak = max(abs(v) for v in buf) or 1
    fade = int(.03 * RATE)
    return [v / peak * level * (min(1, (len(buf) - i) / fade)) for i, v in enumerate(buf)]

N = lambda name: 440 * 2 ** ((('C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B').index(name[:-1]) - 9) / 12 + int(name[-1]) - 4)

CANDIDATES = {
    # A: two bell notes going up, ding-dong
    'a-bell': lambda: mix([note(N('E6'), 0, .9, BELL, 5), note(N('A6'), .11, 1.0, BELL, 5)], 1.1),
    # B: a little pop that rises, then a tiny sparkle
    'b-pop': lambda: mix([note(N('C6'), 0, .25, POP, 18, bend=-.35), note(N('G6'), .09, .5, BELL, 9, .55), note(N('C7'), .15, .5, BELL, 10, .35)], .7),
    # C: music box, three notes up
    'c-musicbox': lambda: mix([note(N('C6'), 0, .8, BOX, 4), note(N('E6'), .09, .8, BOX, 4), note(N('G6'), .18, 1.0, BOX, 4)], 1.2),
    # D: xylophone, two short knocks
    'd-xylo': lambda: mix([note(N('G5'), 0, .45, WOOD, 9), note(N('C6'), .12, .6, WOOD, 8)], .75),
    # D, one knock per ribbon when several pop in at once: each a step higher (G5, C6, E6, G6)
    'd-knock1': lambda: mix([note(N('G5'), 0, .45, WOOD, 9)], .5),
    'd-knock2': lambda: mix([note(N('C6'), 0, .5, WOOD, 8)], .55),
    'd-knock3': lambda: mix([note(N('E6'), 0, .5, WOOD, 8)], .55),
    'd-knock4': lambda: mix([note(N('G6'), 0, .5, WOOD, 8)], .55),
    # calmer ones, about as long as D (user: "또롱 같은 길이인데 좀 차분한")
    # F: low marimba, two notes a fifth apart
    'f-marimba': lambda: mix([note(N('C5'), 0, .5, MARIMBA, 6, att=.008), note(N('G5'), .14, .62, MARIMBA, 5.5, att=.008)], .78),
    # G: felt piano, two soft notes up a fourth
    'g-felt': lambda: mix([note(N('E5'), 0, .55, FELT, 5, att=.02), note(N('A5'), .16, .6, FELT, 5, .9, att=.02)], .78),
    # H: kalimba, two notes down then settling (A5, E5)
    'h-kalimba': lambda: mix([note(N('A5'), 0, .5, KALIMBA, 6, att=.006), note(N('E5'), .15, .6, KALIMBA, 5, att=.006)], .78),
    # I: one soft water drop that rises a little, low
    'i-drop': lambda: mix([note(N('F5'), 0, .7, [(1, 1, 1), (2.0, .08, 2)], 6, bend=-.18, att=.01)], .75),
    # calmer still (user: "좀더 차분한건?"): lower, slower attack, quieter (level .5)
    # J: a soft chord, C5 and E5 together, fading in a little
    'j-chord': lambda: mix([note(N('C5'), 0, .8, FELT, 4, att=.04), note(N('E5'), 0, .8, FELT, 4, .8, att=.04)], .8, .5),
    # K: one low marimba note
    'k-marimba-one': lambda: mix([note(N('C5'), 0, .75, MARIMBA, 4.5, att=.01)], .75, .5),
    # L: felt piano, two notes going down (G5, D5), like a nod
    'l-felt-down': lambda: mix([note(N('G5'), 0, .5, FELT, 5, att=.03), note(N('D5'), .17, .6, FELT, 4.5, att=.03)], .8, .5),
    # M: one round bell tone, slow to start, no bright partials
    'm-soft-tone': lambda: mix([note(N('A4'), 0, .8, [(1, 1, 1), (2.0, .1, 2)], 3.5, att=.06)], .8, .5),
    # N: a bubble pop like the user's sample (ui-pop-sound): about 50 ms, gliding up from low to high
    'n-pop': lambda: mix([sweep(300, 1000, 0, .05)], .12, .6),
    # N per ribbon, each pop a little higher
    'n-pop2': lambda: mix([sweep(380, 1250, 0, .05)], .12, .6),
    'n-pop3': lambda: mix([sweep(470, 1550, 0, .05)], .12, .6),
    # E: a quick sparkle up a pentatonic run
    'e-sparkle': lambda: mix([note(N(n), i * .045, .7, BELL, 7, .8 if i < 4 else 1) for i, n in enumerate(['C6', 'D6', 'E6', 'G6', 'C7'])], 1.0),
}

if __name__ == '__main__':
    out = sys.argv[1]; names = sys.argv[2:] or list(CANDIDATES)
    os.makedirs(out, exist_ok=True)
    for n in names:
        data = CANDIDATES[n]()
        with wave.open(os.path.join(out, f'{n}.wav'), 'wb') as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE)
            w.writeframes(b''.join(struct.pack('<h', int(v * 32767)) for v in data))
        print(n, round(len(data) / RATE, 2), 's')
