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
    newlist  = []
    for i in range (len(arr)):
        newlist.append(arr[i]+arr2[i])
    for  i in newlist:
        print(f"{i}")

list1 = ["Hello", "Good"]
list2 = ["World", "Morning"]
solve(list1,list2)
