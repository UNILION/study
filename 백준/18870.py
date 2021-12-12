N = int(input())
N_list = tuple(map(int, input().split()))
M_list = []
for i in range(N):
    if not N_list[i] in M_list:
        M_list.append(N_list[i])
temp_list = [0] * N
for i in range(N):
    for j in range(len(M_list)):
        if M_list[j] < N_list[i]:
            temp_list[i] += 1
print(*temp_list)