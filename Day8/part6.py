import sys
input = sys.stdin.readline

def p(s):
    print(s)

def is_even(n):
    return n % 2 == 0

for i in range(1, 21):
    if is_even(i):
        p(i)