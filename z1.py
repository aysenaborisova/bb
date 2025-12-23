#1
"""def n(a=3, b=12):
    if a > b:
        return 0
    if a == b:
        return 1
    ways = 0 
    ways += n(a + 1, b)
    ways += n(a + 2, b)
    ways += n(a * 2, b)
    return ways
print(n())
"""
#2
"""
def f(a, b):
    if a == 26 or a > b:
        return 0
    if a == b:
        return 1
    return f(a + 1, b)+f(2 * a + 1, b)
print(f(1, 27))"""

#3

def s(a,b,n):
    if a > b or b == n:
        return 0
    if a == b:
        return 1
    return s9a+ 1, b, n) + s(a + 2,b, n)
s1 = s(2,9,14)
s2 = s(9,18,14)
r = s1 * s2
print(s1,s2,r)