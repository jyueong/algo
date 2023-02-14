import sys
from collections import deque

sys.stdin = open('boj7569.txt')

M, N, H = map(int, sys.stdin.readline().split())

tomatoes = list(list(list(map(int, input().split())) for n in range(N)) for h in range(H))
# [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]]

if 0 in tomatoes:
    q = deque()
    for h in range(H):
        for n in range(N):
            for m in range(M):
                if tomatoes[h][n][m] == 1:
                    q.append((h, n, m))
    print(q)

else:
    print(0)