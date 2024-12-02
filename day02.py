import re
import numpy as np

from aocd import data, submit

reports = [list(map(int, re.split(r'\s', line))) for line in data.splitlines()]


def is_safe(report):
    deltas = [(l - r) for (l, r) in zip(report, report[1:])]
    s = np.sign(deltas[0])

    return all(0 < abs(d) < 4 and np.sign(d) == s for d in deltas)

def solve(safe_fn):
    return sum(+safe_fn(report) for report in reports)

def part1():
    return solve(is_safe)


def is_any_safe(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        if is_safe(report[:i] + report[i + 1:]):
            return True
    return False


def part2():
    return solve(is_any_safe)


if __name__ == '__main__':
    submit(part1(), part="a")
    submit(part2(), part="b")
