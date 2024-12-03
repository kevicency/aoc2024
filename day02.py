import re

import numpy as np
from aocd import data, puzzle


def parse(raw: str):
    return [list(map(int, re.split(r'\s', line))) for line in raw.splitlines()]


def is_safe(report):
    deltas = [(l - r) for (l, r) in zip(report, report[1:])]
    s = np.sign(deltas[0])

    return all(0 < abs(d) < 4 and np.sign(d) == s for d in deltas)


def solve(reports, safe_fn):
    return sum(+safe_fn(report) for report in reports)


def part1(raw: str):
    return solve(parse(raw), is_safe)


def is_safe_dampened(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1:]):
            return True
    return False


def part2(raw: str):
    return solve(parse(raw), is_safe_dampened)


def test_part1_ex():
    for ex in puzzle.examples:
        assert ex.answer_a == str(part1(ex.input_data))


def test_part2_ex():
    for ex in puzzle.examples:
        assert ex.answer_b == str(part2(ex.input_data) - 100)


if __name__ == '__main__':
    puzzle.answer_a = part1(data)
    puzzle.answer_b = part2(data)
