import sys
n = int(input())
a = list(map(int,input().split()))
ans = 0
minn = sys.maxsize
for i in range(0, len(a)):
    ans = 0
    while a[i] % 2 == 0:
        ans += 1
        a[i] /= 2
    minn = min(ans, minn)
print(minn)
