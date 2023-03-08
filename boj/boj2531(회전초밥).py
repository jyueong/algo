import sys
from collections import defaultdict
input = sys.stdin.readline

N, d, k, c = map(int, input().rstrip().split())

lst = list()
chobab = defaultdict(int)

chobab[c] += 1

s = 1
e = (s + k -1) % N

for i in range(N):
    lst.append(int(input().rstrip()))

for i in range(k):
    chobab[lst[i]] += 1

cnt = len(chobab)

while s <= N:
    if chobab[lst[s-1]] == 1:
        chobab.pop(lst[s-1])
    else:
        chobab[lst[s-1]] -= 1
    chobab[lst[e]] += 1
    cnt = max(cnt, len(chobab))

    s += 1
    e = (s + k - 1) % N

print(cnt)