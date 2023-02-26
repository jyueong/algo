N = int(input())

game = [list(input()) for n in range(N)]

sr, er, sc, ec = -1, -1, -1, -1

for i in range(N):
    for j in range(N):
        if game[i][j] == 'G':
            if sr == -1:
                sr, er = i, i
                sc, ec = j, j
            else:
                sr = min(sr, i)
                er = max(er, i)
                sc = min(sc, j)
                ec = max(ec, j)

# 곰곰이가 한 개일 경우
if sr == er and sc == ec:
    print(0)

else:
    x = min(ec, N-sc+1)
    y = min(er, N-sr+1)
    if sr == er:
        print(x)
    elif sc == ec:
        print(y)
    else:
        print(x + y)