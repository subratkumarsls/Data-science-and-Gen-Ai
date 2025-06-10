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

def solve(arr):
    for i in range (len(arr)):
        arr[i]=arr[i]**2
    for  i in arr:
        print(f"{i}")

list1=[1, 2, 3, 4, 5]
solve(list1)
