from aocd import puzzle

dirs = [1, 1 + 1j, 1j, -1 + 1j, -1, -1 - 1j, -1j, 1 - 1j]


def parse(raw: str):
    return {x + 1j * y: c for y, l in enumerate(raw.splitlines()) for x, c in enumerate(l)}


def part1(raw: str):
    grid, g = parse(raw), lambda c: grid.get(c, '.')
    return sum("".join([g(c + i * d) for i in range(4)]) == "XMAS" for c in grid for d in dirs)


def part2(raw: str):
    grid, g = parse(raw), lambda c: grid.get(c, '.')
    return sum(
        [g(c - d) + g(c) + g(c + d) == "MAS" and g(c - d * 1j) + g(c + d * 1j) == "MS" for c in grid for d in dirs if
         d.imag and d.real])


if __name__ == '__main__':
    puzzle.answer_a = part1(puzzle.input_data)
    puzzle.answer_b = part2(puzzle.input_data)
