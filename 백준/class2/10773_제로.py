N = int(input())
N_list = [int(input()) for _ in range(N)]
result = [0]
for n in N_list:
    if n != 0:
        result.append(n)
    else:
        result.pop()
print(sum(result))