from functools import cmp_to_key

from aocd import puzzle


def parse(raw: str):
    chunks = [chunk for chunk in raw.split('\n\n')]
    rules, updates = [r.split('|') for r in chunks[0].splitlines()], [u.split(',') for u in chunks[1].splitlines()]
    rdict = {p: ([l for l, r in rules if r == p]) for _, p in rules}
    key_fn = cmp_to_key(lambda a, b: -1 if a in rdict.get(b, []) else 1 if b in rdict.get(a, []) else 0)
    return [(sorted(u, key=key_fn), u) for u in updates]


mid = lambda arr: int(arr[int(len(arr) / 2)])


def part1(raw: str):
    return sum(mid(u) for (s, u) in parse(raw) if s == u)


def test_part1_ex():
    for ex in puzzle.examples:
        assert ex.answer_a == str(part1(ex.input_data))
    return True


def part2(raw: str):
    return sum(mid(s) for s, u in parse(raw) if s != u)


def test_part2_ex():
    for ex in puzzle.examples:
        assert '123' == str(part2(ex.input_data))
    return True


if __name__ == '__main__':
    if test_part1_ex() and not puzzle.answered_a:
        puzzle.answer_a = part1(puzzle.input_data)

    if test_part2_ex() and not puzzle.answered_b:
        puzzle.answer_b = part1(puzzle.input_data)
