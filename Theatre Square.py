n, m, a = map(int, input().split())

if n % a != 0 and a < n:
    n = n + (n-a)
else:
    a1 = a - (a-n)

if m % a != 0 and a < m:
    m = m + (m-a)
else:
    a2 = a - (a-m)

print((n*m)//(a1*a2))
