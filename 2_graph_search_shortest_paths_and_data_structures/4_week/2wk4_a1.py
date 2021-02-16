#!/usr/bin/env python
import time
from bisect import bisect_left, bisect_right


def read_file(name):
    """
    Given the name of the file, return the sorted list.
    """
    with open(name, 'r') as f:
        data = set([int(i.strip()) for i in f.readlines()])
    return sorted(data)


def two_sum(arr):
    """
    Given sorted arr and target value t, return the result.
    """
    sum_value = set()
    for i in arr:
        # find the indices
        left = bisect_left(arr, -10000 - i)
        right = bisect_right(arr, 10000-i)

        for j in arr[left:right]:
            if i != j:
                sum_value.add(i+j)

    return len(sum_value)


if __name__ == '__main__':
    start = time.time()

    array = read_file('data.txt')
    total = two_sum(array)

    print(total, 'calculated in {}'.format(time.time()-start))
