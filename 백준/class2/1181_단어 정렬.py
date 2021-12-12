N = int(input())
N_list = [0] * N
for n in range(N):
    N_list[n] = input()
N_list = set(N_list)
N_list = sorted(N_list, key = lambda x:(len(x), x))
for n in N_list:
    print(n)