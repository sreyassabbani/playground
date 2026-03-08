# seq = []

from functools import reduce
import sys

# l = [int(x) for x in sys.argv[1:]]
l = list(map(int, sys.argv[1:]))

print(reduce(lambda x, acc: x + 1 / acc, l[::-1]))
