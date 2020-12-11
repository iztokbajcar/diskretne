# Program za ugotavljanje lastnosti števil
# Iztok Bajcar, 2020
import math

def gcd(a, b):
    n = max(a, b)
    m = min(a, b)
    o = n % m
    while (True):
        n = m
        m = o
        if (n % m == 0):
            return o
        o = n % m

def prastevila(n):  # vrne seznam prastevil na intervalu od 2 do n, vključno
    n = n + 1
    s = [False for i in range(n)]
    p = 2
    while p <= math.sqrt(n):
        for i in range(2 * p, n, p):
            s[i] = True
        for i in range(p + 1, n):
            if not s[i]:
                p = i
                break

    rez = [n for n in range(2, len(s)) if not s[n]]
    return rez

def delitelji(n):  # vrne delitelje števila
    rez = [];
    for i in range(1, n + 1):
        if n % i == 0:
            rez.append(i)
    return rez
