# 지도 두개 가지고 . 부분 바꿔가면서 bfs 돌리기
# 1번 지도는 고슴도치가 해당 칸 가는데 걸리는 최소 시간
# 2번 지도는 물이 해당 칸 가는데 걸리는 최소 시간
# 1, 2번 비교해서 고슴도치 < 물이면 고슴도치가 갈 수 있음
# 비버 옆 칸에 갈 수 있으면 정답은 비버 옆 칸 숫자들 중에 최소 +1
# 못 가면 KAKTUS

# 비버에서 시작해서 물이랑 고슴도치에 가는데 얼마나 걸리는지 봐도 되나...?

import sys
from collections import deque
from copy import deepcopy

sys.stdin = open('boj3055.txt')

R, C = map(int, sys.stdin.readline().split())

lst = []
wyes = False

for i in range(R):
    lst.append(list(sys.stdin.readline().rstrip()))

sq = deque()
wq = deque()

hedgehog = deepcopy(lst)
water = deepcopy(lst)

# 고슴도치, 비버, 물 시작점 찾기
for i in range(R):
    for j in range(C):
        if lst[i][j] == 'D':
            dp = (i, j)
        elif lst[i][j] == '*':
            wyes = True
            w = (i, j, 0)
            wq.append(w)
        elif lst[i][j] == 'S':
            s = (i, j, 0)
            sq.append(s)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

while sq:
    value = sq.popleft()
    r = value[0]
    c = value[1]
    cnt = value[2]
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        ncnt = cnt + 1
        if 0 <= nr <= R - 1 and 0 <= nc <= C - 1 and hedgehog[nr][nc] == '.':
            hedgehog[nr][nc] = ncnt
            sq.append((nr, nc, ncnt))

if wyes is True:
    while wq:
        value = wq.popleft()
        r = value[0]
        c = value[1]
        cnt = value[2]
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            ncnt = cnt + 1
            if 0 <= nr <= R - 1 and 0 <= nc <= C - 1 and water[nr][nc] == '.':
                water[nr][nc] = ncnt
                wq.append((nr, nc, ncnt))

    for i in range(R):
        for j in range(C):
            if lst[i][j] == '.' and hedgehog[i][j] < water[i][j]:
                lst[i][j] = 'O'

anslst = []
dx = dp[0]
dy = dp[1]

for d in range(4):
    nx = dx + dr[d]
    ny = dy + dc[d]
    if 0 <= nx <= R - 1 and 0 <= ny <= C - 1 and lst[nx][ny] == 'S':
        anslst.append(0)
        break
    if wyes is True and 0 <= nx <= R - 1 and 0 <= ny <= C - 1 and lst[nx][ny] == 'O':
        anslst.append(int(hedgehog[nx][ny]))
    elif wyes is False and 0 <= nx <= R - 1 and 0 <= ny <= C - 1 and lst[nx][ny] != 'X':
        anslst.append(int(hedgehog[nx][ny]))

    
if len(anslst) >= 1:
    print(min(anslst) + 1)
else:
    print("KAKTUS")