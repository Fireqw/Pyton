a, b, c = map(int, input().split())

maxn = a
minx = a

if b > maxn:
    maxn = b

if c > maxn:
    maxn = c

if b < minx:
    minx = b

if c < minx:
    minx = c

print(maxn - minx)
