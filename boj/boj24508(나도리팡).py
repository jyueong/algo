# 나도리 총합이 터지는 개수로 나눠떨어지지 않으면 무조건 NO
# 1. 제일 적은데서 제일 큰 데로 옮기는 걸 반복...?
# 2-1. 총합 / 터지는 개수 = 터지는데 필요한 바구니 갯수
# 2-2. 내림차순으로 정렬해서 터지는데 필요한 바구니 갯수까지 합 구하기
# 2-3. 총합 - 2-2 가 T보다 작거나 같으면 가능할듯?

import sys

sys.stdin = open("boj24508.txt")

# 바구니 갯수, 터지는 갯수, 옮기기 횟수
N, K, T = map(int, sys.stdin.readline().split())

# 현재 바구니당 담겨있는 나도리 갯수 리스트
nadoris = list(map(int, sys.stdin.readline().split()))

# 전체 나도리 수
ts = sum(nadoris)
mok, na = divmod(ts, K)

if na != 0:
    print('NO')

else:
    nadoris.sort(reverse=True)
    nadoris = nadoris[:mok]
    subs = sum(nadoris)
    cnt = ts - subs
    if cnt <= T:
        print('YES')
    else:
        print('NO')