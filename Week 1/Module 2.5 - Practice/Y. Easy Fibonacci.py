# Problem link: https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Y

n = int(input())
n1, n2 = 0, 1
count = 0

if n == 1:
    print(n1)
else:
    while count < n:
        print(n1, end=' ')
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1