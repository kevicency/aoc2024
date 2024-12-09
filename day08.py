import itertools

from aocd import puzzle


def parse(raw: str):
    lines = raw.splitlines()
    grid = {x + 1j * y: c for y, l in enumerate(lines) for x, c in enumerate(l)}
    antennas = {}
    for (p, f) in grid.items():
        antennas[f] = antennas.get(f, []) + [p]

    return antennas, len(lines) - 1, len(lines[0]) - 1


def part1(raw: str):
    (antennas, mi, mr), antinodes = parse(raw), set()
    for (f, ps) in antennas.items():
        if f == '.': continue
        for (a, b) in itertools.product(ps, ps):
            if a == b: continue
            d = a - b
            antinodes.add(a + d)
            antinodes.add(b - d)
    return len(list(p for p in antinodes if 0 <= p.imag <= mi and 0 <= p.real <= mr))


def test_part1_ex():
    for ex in puzzle.examples:
        assert ex.answer_a == str(part1(ex.input_data))
    return True


def part2(raw: str):
    (antennas, mi, mr), antinodes = parse(raw), set()
    for (f, ps) in antennas.items():
        if f == '.': continue
        for (a, b) in itertools.product(ps, ps):
            if a == b: continue
            d = a - b
            while 0 <= a.imag <= mi and 0 <= a.real <= mr:
                antinodes.add(a)
                a = a + d
            while 0 <= b.imag <= mi and 0 <= b.real <= mr:
                antinodes.add(b)
                b = b - d

    return len(antinodes)


def test_part2_ex():
    for ex in puzzle.examples:
        assert '34' == str(part2(ex.input_data))
    return True


if __name__ == '__main__':
    if test_part1_ex() and not puzzle.answered_a:
        puzzle.answer_a = part1(puzzle.input_data)

    if test_part2_ex() and not puzzle.answered_b:
        puzzle.answer_b = part2(puzzle.input_data)
