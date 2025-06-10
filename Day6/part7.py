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
    newlist  = set()
    list3=[]
    for i in arr:
        newlist.add(i)
    for  i in arr2:
       if i in newlist :
            list3.append(i)
    for i in list3:
        print(f"{i}" ,end=' ')
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
solve(list1,list2)
