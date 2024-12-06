from aocd import puzzle


def parse(raw: str):
    grid = {x + 1j * y: c for y, l in enumerate(raw.splitlines()) for x, c in enumerate(l)}
    return [grid, next(k for k, v in grid.items() if v == '^'), -1j]


def part1(raw: str):
    grid, p, d = parse(raw)
    seen, g = set(), lambda pos: grid.get(pos, '')
    while g(p) != '':
        while g(p + d) == '#':
            d *= 1j
        seen.add(p)
        p += d
    return len(seen)


def test_part1_ex():
    for ex in puzzle.examples:
        assert ex.answer_a == str(part1(ex.input_data))
    return True


def part2(raw: str):
    grid, s, sd = parse(raw)
    r, g = 0, lambda pos, obs: '#' if pos == obs else grid.get(pos, '')
    for o in grid:
        if o == s or g(o, None) != '.':
            continue
        p, d, seen = s, sd, set()
        while (p, d) not in seen and g(p, o) != '':
            seen.add((p, d))
            while g((p + d), o) == '#':
                d *= 1j
            p += d
        s += (p, d) in seen
    return s


def test_part2_ex():
    for ex in puzzle.examples:
        assert '6' == str(part2(ex.input_data))
    return True


if __name__ == '__main__':
    if test_part1_ex() and not puzzle.answered_a:
        puzzle.answer_a = part1(puzzle.input_data)

    if test_part2_ex() and not puzzle.answered_b:
        puzzle.answer_b = part2(puzzle.input_data)
