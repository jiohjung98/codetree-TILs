import math

def calc_gcd(x,y):
    print(math.gcd(x,y))

x, y = tuple(map(int, input().split()))

calc_gcd(x,y)