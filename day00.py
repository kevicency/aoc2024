from aocd import puzzle


def parse(raw: str):
    return [line for line in raw.splitlines()]


def part1(raw: str):
    return None


def test_part1_ex():
    for ex in puzzle.examples:
        assert ex.answer_a == str(part1(ex.input_data))
    return True


def part2(raw: str):
    return None


def test_part2_ex():
    for ex in puzzle.examples:
        assert ex.answer_b == str(part2(ex.input_data))
    return True


if __name__ == '__main__':
    if test_part1_ex() and not puzzle.answered_a:
        puzzle.answer_a = part1(puzzle.input_data)

    if test_part2_ex() and not puzzle.answered_b:
        puzzle.answer_b = part2(puzzle.input_data)
