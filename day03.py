import functools
import re

from aocd import puzzle

ex_input_data = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


def parse(raw: str):
    return re.findall(r'(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\))', raw)


def part1(raw: str):
    return sum([int(a) * int(b) for op, a, b in parse(raw) if op.startswith('mul')])


def test_part1_ex():
    assert '161' == str(part1(ex_input_data))
    return True


def part2(raw: str):
    def step(acc, instr):
        (s, m), (op, a, b) = acc, instr
        return (s + (int(a) * int(b) * m), m) if op.startswith('mul') else (s, 't' not in op)

    return functools.reduce(step, parse(raw), (0, 1))[0]


def test_part2_ex():
    assert '48' == str(part2(ex_input_data))
    return True


if __name__ == '__main__':
    if test_part1_ex() and not puzzle.answered_a:
        puzzle.answer_a = part1(puzzle.input_data)

    if test_part2_ex() and not puzzle.answered_b:
        puzzle.answer_b = part2(puzzle.input_data)
