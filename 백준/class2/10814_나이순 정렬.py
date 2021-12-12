N = int(input())
N_list = [0] * N
for n in range(N):
    age, name = map(str, input().split())
    N_list[n] = (int(age), name)
N_list = sorted(N_list, key = lambda x:x[0])
for n in range(N):
    print(N_list[n][0], N_list[n][1])