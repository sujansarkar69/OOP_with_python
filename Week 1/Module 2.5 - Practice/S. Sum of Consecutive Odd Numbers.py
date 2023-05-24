# Problem link: https://codeforces.com/group/MWSDmqGsZm/contest/219432/problem/S

t = int(input())

for i in range(t):
    x, y = map(int, input().split())
    
    start = min( x, y) + 1
    end = max(x, y)
    sum_odd = 0

    for num in range(start, end):
        if num % 2 != 0:
            sum_odd += num
    
    print(sum_odd)
    