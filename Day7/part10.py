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

def solve(password):
    if len(password) <= 6:
        print_line("Weak Password")
    elif any(c.isdigit() for c in password):
        print_line("Strong Password")
    else:
        print_line("Medium Password")

password = input().strip()
solve(password)