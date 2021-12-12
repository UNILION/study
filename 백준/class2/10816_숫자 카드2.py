N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))
result = {}
for n in N_list:
    if n in result:
        result[n] += 1
    else:
        result[n] = 1
for m in M_list:
    try:
        print(result[m], end=" ")
    except:
        print(0, end=" ")