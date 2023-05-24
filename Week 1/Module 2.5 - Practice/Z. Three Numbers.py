# Problem link: https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Z

K, S = map(int, input().split())
res = 0
for i in range(K + 1):
    for j in range(K + 1):
        if S - i - j >= 0 and S - i - j <= K:
            res += 1
print(res)