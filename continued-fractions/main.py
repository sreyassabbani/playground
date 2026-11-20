from functools import reduce
from typing import Callable
from collections.abc import Iterator

# import sys
# l = list(map(int, sys.argv[1:]))


def approx(seq: list[int]):
    return reduce(lambda acc, x: x + 1 / acc, seq[::-1])


def approx_all(seqs: Iterator[list[int]]):
    return map(approx, seqs)


def rep(start: int, f: Callable[[int], list[int]], terms: int = 50) -> Iterator[int]:
    yield start
    for i in range(1, terms):
        yield from f(i)


# fmt: off
print(
    *approx_all(map(list, [
        rep(2, lambda i: [1, 2*i, 1]),
        rep(2, lambda i: [2*i]),
        rep(3, lambda i: [1, 3*i, 1]),
    ]))
)
# fmt: on
