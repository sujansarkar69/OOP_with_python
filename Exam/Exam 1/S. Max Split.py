# Problem link: https://codeforces.com/group/MWSDmqGsZm/contest/219856/problem/S?fbclid=IwAR1qi6o8WBDOrdzcZ--U5YO_40SSQmmLbZ8jggB6CFIRqog1ukVL_Z2wK2s

str = input()
res_Str = []
left = 0
right = 0
for char in str:
    if char == 'L':
        left += 1
    else:
        right += 1
    
    if left == right:
        res_Str.append(str[: left + right])
        str = str[left + right :]
        left = 0
        right = 0

print(len(res_Str))
for char in res_Str:
    print(char)
