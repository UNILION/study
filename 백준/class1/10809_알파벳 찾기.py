S = input()
temp = []
cnt = 0
result = [-1] * 26
for s in S:
    if s not in temp:
        temp.append(s)
        result[ord(s) - 97] = cnt
    cnt += 1
print(*result)