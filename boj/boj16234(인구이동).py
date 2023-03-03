import sys
sys.setrecursionlimit(100000)

# 연합 표시용 리스트 하나 만들어서
# 기본은 0 으로 해
# (0, 0)부터 델타탐색 돌려 > 연합 할 수 있는 애면 걍 양쪽에 가능 때려박고
# 가능인 좌표들은 set에 때려박기
# 그러면 연합 표시용 리스트에는 가능 아니면 0이 되겠지?

# 이제 set 가지고 bfs 돌려서 한번에 통해있는 애들 개수 체크하고 sum 합치고 얘네는 연표리 지나감으로 바꿔 근데 이 좌표들도 기억해야함
# bfs 끝났으면 해당 좌표들 값 sum / 개수 해서 값 바꿔주고
# set에서 연표리 가능인 좌표 찾아서 또 bfs 돌려
# set 다 끝나면 하루 끝남

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def ganeung():

    for i in range(N):
        for j in range(N):
            a = population[i][j]
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if 0 <= nx < N and 0 <= ny < N and L <= abs(a - population[nx][ny]) <= R:
                    possible.add((i, j))
                    possible.add((nx, ny))
                    if visited[i][j] == '아직':
                        visited[i][j] = '가능'
                    if visited[nx][ny] == '아직':
                        visited[nx][ny] = '가능'
    return


def bfs(x, y):
    global union_sum

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == '가능' and L <= abs(population[x][y] - population[nx][ny]) <= R:
            union.add((nx, ny))
            union_sum += population[nx][ny]
            visited[nx][ny] = '지나감'
            bfs(nx, ny)


N, L, R = map(int, input().split())

population = list()

for i in range(N):
    population.append(list(map(int, input().split())))

cnt = 0


while 1:
    visited = [['아직' for i in range(N)] for j in range(N)]
    possible = set()

    ganeung()

    if len(possible) == 0:
        break

    while possible:
        x, y = possible.pop()

        if visited[x][y] != '지나감':
            union = set()
            union_sum = 0

            union.add((x, y))
            union_sum += population[x][y]
            visited[x][y] = '지나감'
            bfs(x, y)

            for x, y in union:
                population[x][y] = union_sum//len(union)

    cnt += 1

print(cnt)