import sys

input = sys.stdin.readline

def print_line(s):
    print(s)
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, product
import math
import os
def solve(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] = 0  
    for i in arr:
        print(f"{i}")

INF = float('inf')
MOD = 10**9 + 7
test_array = [4, -3, 7, -1, 0, 5]
solve(test_array)

