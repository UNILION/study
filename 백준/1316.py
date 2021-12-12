N = int(input())
result = 0
for _ in range(N):
    temp = set()
    flag = 1
    string = input()
    if len(string) == 1:
        result += 1
        continue
    temp.add(string[0])
    for s in range(len(string) - 1):
        if string[s] != string[s + 1]:
            flag = 0
            if string[s + 1] in temp:
                break
            else:
                temp.add(string[s])
                if s == len(string) - 2:
                    result += 1
    if flag:
        result += 1
print(result)