from functools import reduce

# import sys
# l = list(map(int, sys.argv[1:]))


def approx(seq: list[int]):
    return reduce(lambda acc, x: x + 1 / acc, seq[::-1])


def approx_all(seqs: list[list[int]]):
    return map(approx, seqs)


# fmt: off
print(
    *approx_all([
        [2, 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, 1, 1, 10, 1, 1, 12, 1, 1, 14, 1, 1, 16, 1, 1, 18, 1, 1, 20, 1, 1, 22, 1, 1, 24, 1, 1, 26, 1, 1, 28, 1, 1, 30, 1, 1, 32, 1, 1, 34, 1, 1, 36, 1, 1, 38, 1, 1, 40, 1, 1, 42, 1, 1, 44, 1, 1, 46, 1, 1, 48, 1, 1, 50, 1, 1, 52, 1, 1, 54, 1, 1, 56, 1, 1, 58, 1, 1, 60, 1, 1, 62, 1, 1, 64, 1, 1, 66],
        [2, 1] + [x for i in range(1, 40) for x in (2*i, 1, 1)],
        [3, 1] + [x for i in range(1, 40) for x in (3*i, 1, 1)],
        [1, 1, 2, 3, 4],
        [1, 1, 2, 3, 4],
        [1, 1, 2, 3, 4],
        [1, 1, 2, 3, 4],
    ])
)
# fmt: on
