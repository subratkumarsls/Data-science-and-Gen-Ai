import sys
input = sys.stdin.readline

def print_line(s):
    print(s)

from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, product
import math
import os

INF = float('inf')
MOD = 10**9 + 7

def solve(s):
    rev = ''
    for i in range(len(s) - 1, -1, -1):
        rev += s[i]
    print_line(rev)

s = input().strip()
solve(s)