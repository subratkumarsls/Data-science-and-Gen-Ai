
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

def solve(lst):
    count = 0
    for word in lst:
        if 'e' in word:
            count += 1
    print_line(str(count))

lst = ["Pine", "Oak", "Maple", "Neem", "Banyan"]
solve(lst)