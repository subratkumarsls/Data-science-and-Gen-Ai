import sys
input = sys.stdin.readline

def p(s):
    print(s)

def is_even(n):
    return n % 2 == 0

p(is_even(4))
p(is_even(5))