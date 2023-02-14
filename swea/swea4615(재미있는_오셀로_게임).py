import sys
sys.stdin = open('swea4615.txt')

dx = [0, 0, -1, 1, -1, 1]
dy = [-1, 1, 0, 0, -1, 1]

def othello(rx, ry, c):
    candidate = []
    # 흑돌 놓을 차례
    if c == 1:
        board[rx][ry] = 'B'
        for d in range(6):
            x = rx
            y = ry
            while 1:
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 'W':
                    candidate.append((nx, ny))
                    x = nx
                    y = ny
                elif 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 'B':
                    for i in range(len(candidate)):
                        x, y = candidate[i]
                        board[x][y] = 'B'
                    candidate = []
                    break
                else:
                    candidate = []
                    break
            candidate = []
    # 백돌 놓을 차례
    else:
        board[rx][ry] = 'W'
        for d in range(6):
            x = rx
            y = ry
            while 1:
                nx = x + dx[d]
                ny = y + dy[d]
                if 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 'B':
                    candidate.append((nx, ny))
                    x = nx
                    y = ny
                elif 0 <= nx < len(board) and 0 <= ny < len(board) and board[nx][ny] == 'W':
                    for i in range(len(candidate)):
                        x, y = candidate[i]
                        board[x][y] = 'W'
                    candidate = []
                    break
                else:
                    candidate = []
                    break
            candidate = []
            

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [[0]*N for i in range(N)]
    board[N//2][N//2], board[N//2-1][N//2-1] = 'W', 'W'
    board[N//2-1][N//2], board[N//2][N//2-1] = 'B', 'B'
    for m in range(M):
        x, y, c = map(int, input().split())
        othello(x, y, c)
    cnt_b = 0
    cnt_w = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 'B':
                cnt_b += 1
            elif board[i][j] == 'W':
                cnt_w += 1
    print(f'#{tc} {cnt_b} {cnt_w}')