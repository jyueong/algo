T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # 길이가 짧은 쪽을 lst_a로 고정
    if N >= M:
        lst_b = list(map(int, input().split()))
        lst_a = list(map(int, input().split()))
    else:
        lst_a = list(map(int, input().split()))
        lst_b = list(map(int, input().split()))

    ms = 0

    for i in range(len(lst_a)):
        ms += lst_b[i]*lst_a[i]

    for i in range(1, len(lst_b)-len(lst_a)+1):
        s = 0
        for j in range(len(lst_a)):
            s += lst_b[i+j]*lst_a[j]
        print(s)
        ms = max(ms, s)


    print(f'#{tc} {ms}')