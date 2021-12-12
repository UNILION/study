from itertools import permutations

N, M = map(int, input().split())
cctv = [6] * (M + 2)
for _ in range(N):
    cctv += [6, *list(map(int, input().split())), 6]
cctv += [6] * (M + 2)

cctv_case_list = [0, 4, 2, 4, 4, 0] # 5번은 경우가 1개라 제외 시킴
cctv_case = 0
for i in range(1, 6):
    cctv_case += (cctv.count(i) * cctv_case_list[i])
direction1 = [[1], [-1], [M + 2], [-(M + 2)]]
direction2 = [[1, -1], [M + 2, -(M + 2)]]
direction3 = [[M + 2, 1], [1, -(M + 2)], [-(M + 2), -1], [-1, M + 2]]
direction4 = [[-1, M + 2, 1], [M + 2, 1, -(M + 2)], [1, -(M + 2), -1], [-(M + 2), -1, M + 2]]

direction = [direction1, direction2, direction3, direction4]
a = permutations(direction,4)
print(a)
for j in range(cctv_case):
    result = 0
    for d in range(4):
        for k in range(len(cctv)):
            if cctv[k] == 1:
                while cctv[k + direction[d]] != 6:
                    k += 1
                    if cctv[k] == 0:
                        cctv[k] = 6

                   