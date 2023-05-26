# Problem link: https://atcoder.jp/contests/arc087/tasks/arc087_a

n = int(input())
a = list(map(int, input().split()))
dict = {}
for i in a:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

result = 0
for key, value in dict.items():
    if key > value:
        result += value
    else:
        result += (value-key)
print(result)
