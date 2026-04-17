import sys
input = sys.stdin.readline

def build_bit(size):
    return [0] * (size + 1)

def update(bit, i, size):
    while i <= size:
        bit[i] += 1
        i += i & (-i)

def query(bit, i):
    s = 0
    while i > 0:
        s += bit[i]
        i -= i & (-i)
    return s

def count_greater(bit, l, r, size):
    if l > r:
        return 0
    return query(bit, r) - query(bit, l - 1)

def solve():
    n = int(input())
    A = list(map(int, input().split()))

    OFFSET = 10**6
    MAX_VAL = 10**6
    SIZE = 2 * MAX_VAL + 1

    bit = build_bit(SIZE + 1)
    result = 0

    for j in range(n):
        aj = A[j]
        threshold = aj * aj

        lower_bound = threshold + 1

        if lower_bound <= MAX_VAL:
            bit_lower = max(lower_bound + OFFSET + 1, 1)
            bit_upper = MAX_VAL + OFFSET + 1
            result += count_greater(bit, bit_lower, bit_upper, SIZE)

        bit_index = aj + OFFSET + 1
        update(bit, bit_index, SIZE)

    print(result)

solve()

