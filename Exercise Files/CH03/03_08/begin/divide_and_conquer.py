#!/usr/bin/env python3
""" Recursively sum a range of numbers """

def recursive_sum(lo, hi):
    if hi - lo <= 100_000: # base case threshold
        return sum(range(lo, hi))
    else:
        mid = (hi + lo) // 2 # middle index for splitting
        left = recursive_sum(lo, mid)
        right = recursive_sum(mid, hi)
        return left + right

if __name__ == '__main__':
    total = recursive_sum(1, 1_000_000)
    print('Total sum is', total)
