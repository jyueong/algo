import sys

sys.stdin = open("boj15922.txt")

N = int(sys.stdin.readline())
line = 0

s, e = map(int, sys.stdin.readline().split())

for i in range(1, N):
    ns, ne = map(int, sys.stdin.readline().split())
    if ns <= e:
        e = max(ne, e)
    else:
        line += e - s
        s = ns
        e = ne

line += e - s

print(line)