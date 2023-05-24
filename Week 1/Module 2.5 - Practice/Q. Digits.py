# # Problem link: https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/Q

t = int(input())
while t > 0:
    str = input()
    for i in range(len(str) - 1, -1, -1):
        print(str[i], end=" ")
    print()
    t -= 1