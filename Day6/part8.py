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
    newlist  = set()
    list3=[]
    for i in arr:
        newlist.add(i)
    for i in newlist:
        list3.append(i)
    return list3
list1 = [1, 2, 3, 2, 4, 5, 3, 6, 5]
List =  solve(list1)
for i in List:
    print(f"{i}",end=' ')
