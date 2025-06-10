import sys

input = sys.stdin.readline

def print_line(s):
    print(s)
from collections import deque, defaultdict, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations, product
import math
import os
def cnt(arr,t):
    count=0
    for i in arr:
        if i==t:
            count+=1
    print_line(f"Number of times was seem = {count}")

INF = float('inf')
MOD = 10**9 + 7
arr =[1, 3, 7, 8, 3, 5, 3]
Target=  3
cnt(arr,Target)

