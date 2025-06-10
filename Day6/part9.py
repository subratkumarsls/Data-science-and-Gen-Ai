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


def solve(arr,arr2):
    sum=0;
    for i in range (len(arr)):
        sum+=arr[i]*arr2[i]
    print(f"{sum}" ,end=' ')
quantities = [2, 3, 5, 1]
prices = [50, 30, 20, 10]

solve(quantities,prices)
