import sys

T = int(sys.stdin.readline())

for tc in range(1, T+1):
    n = int(sys.stdin.readline())
    word = ""
    for i in range(n):
        c, k = sys.stdin.readline().split()
        word += c*int(k)
    a, b = divmod(len(word), 10)
    for i in range(a):
        print(word[:10])
        word = word[10:]
    if b > 0:
        print(word)