import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())

tomatoes = list(list(list(map(int, sys.stdin.readline().split())) for n in range(N)) for h in range(H))

zcnt = 0
q = deque()

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomatoes[h][n][m] == 0:
                zcnt += 1
            elif tomatoes[h][n][m] == 1:
                q.append((h, n, m, 0))

if zcnt == 0:
    print(0)

else:
    dz = [-1, 1]
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    mcnt = 0

    while q:
        h, n, m, cnt = q.popleft()
        cnt += 1
        for d in range(2):
            nh = h + dz[d]
            if 0 <= nh < H and tomatoes[nh][n][m] == 0:
                tomatoes[nh][n][m] = 1
                q.append((nh, n, m, cnt))
                mcnt = max(mcnt, cnt)
                zcnt -= 1
        for d in range(4):
            nn = n + dc[d]
            nm = m + dr[d]
            if 0 <= nn < N and 0 <= nm < M and tomatoes[h][nn][nm] == 0:
                tomatoes[h][nn][nm] = 1
                q.append((h, nn, nm, cnt))
                mcnt = max(mcnt, cnt)
                zcnt -= 1

    if zcnt != 0:
        print(-1)

    else:
        print(mcnt)