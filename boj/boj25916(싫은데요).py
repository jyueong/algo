N, M = map(int, input().split())
h_lst = list(map(int, input().split()))

s = 0
len = 0
v = 0
maxv = 0

while s+len < N:
    if v + h_lst[s+len] <= M:
        v += h_lst[s+len]
        len += 1
    else:
        maxv = max(maxv, v)
        v -= h_lst[s]
        s += 1
        len -= 1

maxv = max(maxv, v)

print(maxv)