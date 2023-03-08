import sys
input = sys.stdin.readline

N = int(input().rstrip())

towns = list()
for i in range(N):
    towns.append(list(map(int, input().rstrip().split())))

intim = int(1e9)

memo = [[0] * N for i in range(N)]

for i in range(N):
    for j in range(N):
        if i != j:
            memo[i][j] = memo[j][i] = abs(towns[i][0] - towns[j][0]) + abs(towns[i][1] - towns[j][1]) + abs(towns[i][2] - towns[j][2])

for i in range(N):
    for j in range(N):