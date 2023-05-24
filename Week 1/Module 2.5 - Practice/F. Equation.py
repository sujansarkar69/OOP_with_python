# Problem link: https://codeforces.com/group/MWSDmqGsZm/contest/223205/problem/F

def power_of(x, n):
    sum = 0
    for i in range(2, n + 1, 2):
       sum += pow(x, i)
    return sum

x, n = map(int, input().split())
ans = power_of(x, n)
print(ans)