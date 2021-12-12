n = int(input())
n_list = list(map(int, input().split()))
max_n = max(n_list)
for i in range(len(n_list)):
    n_list[i] = n_list[i] / max_n * 100
print(sum(n_list) / n)