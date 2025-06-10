import sys

input = sys.stdin.readline

def print_line(s):
    print(s)
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, product
import math
import os
def max_min(arr):
    maxi = -INF
    mini = INF
    for i in arr:
        if i > maxi:
            maxi = i
        if i < mini:
            mini = i
    print_line(f"Maximum value {maxi} and minimum value {mini}")

INF = float('inf')
MOD = 10**9 + 7
test_array = [10, 5, 8, 12, 3]
max_min(test_array)

