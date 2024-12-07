import re

from aocd import puzzle


def parse(raw: str):
    lines = [list(map(int, re.findall(r'\d+', line))) for line in raw.splitlines()]
    return [(line[0], line[1:]) for line in lines]


def any_valid(xs: [str]):
    return next((x for x in xs if len(x) > 0), '')


def solve(r: int, ns: [int], ops: str = '', concat=False):
    match ns:
        case [head]:
            return ops if r == head else ''
        case [head, *tail]:
            return any_valid([
                solve(int(r / head), tail, ops + '*', concat) if r % head == 0 else '',
                solve(r - head, tail, ops + '+', concat) if r - head > 0 else '',
                solve(int(re.sub(rf'{head}$', '', str(r))), tail, ops + '||', concat) if concat and re.search(
                    rf'\d+{head}$', str(r)) else ''
            ])
        case _:
            return ''


def part1(raw: str):
    results = [(r, solve(r, list(reversed(xs)), '', False)) for r, xs in parse(raw)]
    return sum(r for r, ops in results if len(ops) > 0)


def test_part1_ex():
    for ex in puzzle.examples:
        assert ex.answer_a == str(part1(ex.input_data))
    return True


def part2(raw: str):
    results = [(r, solve(r, list(reversed(xs)), '', True)) for r, xs in parse(raw)]
    return sum(r for r, ops in results if len(ops) > 0)


def test_part2_ex():
    for ex in puzzle.examples:
        assert '11387' == str(part2(ex.input_data))
    return True


if __name__ == '__main__':
    if test_part1_ex() and not puzzle.answered_a:
        puzzle.answer_a = part1(puzzle.input_data)

    if test_part2_ex() and not puzzle.answered_b:
        puzzle.answer_b = part2(puzzle.input_data)
