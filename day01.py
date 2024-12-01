import re
from collections import Counter

from aocd import data, submit

[left, right] = map(sorted, zip(*[map(int, re.split(r'\s+', line)) for line in data.splitlines()]))


def part1():
    return sum([abs(l - r) for l, r in zip(left, right)])


def part2():
    c = Counter(right)
    return sum([l * c[l] for l in left])


if __name__ == '__main__':
    submit(part1(), part="a")
    submit(part2(), part="b")
