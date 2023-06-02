# Problem link: https://codeforces.com/group/MWSDmqGsZm/contest/219774/problem/V

n, m = map(int, input().split())
a = list(map(int, input().split()))
 
freq = [0 for i in range(m + 1)]
for i in a:
    freq[i] += 1
for i in range(1, m + 1):
    print(freq[i])

