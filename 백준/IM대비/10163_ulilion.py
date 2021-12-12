import sys
input = sys.stdin.readline
import copy

# 해당 색종이 위치에 해당 색종이 번호를 전부 표시하고
# 표시가 끝나면 전체 탐색으로 해당 숫자가 몇 번 나왔는지 확인하면 된다고 생각했다.

tc = int(input())                                           # 테스트 케이스 입력 받음
square_list = []                                            # 색종이 좌표 리스트
for t in range(1, tc + 1):                                  # 테스트 케이스 갯수만큼 반복
    square_list.append(list(map(int, input().split())))     # 색종이 좌표를 입력 받음
temp_list = copy.deepcopy(square_list)                      # 색종이좌표 깊은 복사
square_list.sort(key=lambda x:x[1])                         # 1번 인덱스 기준 정렬
min_y = square_list[0][1]                                   # y의 최소값을 min_y에 저장

square_list.sort(key=lambda x:x[0])                         # 0번 인덱스 기준 정렬
min_x = square_list[0][0]                                   # x의 최소값을 min_x에 저장

square_list.sort(key=lambda x:-(x[0]+x[2]))                 # 0번과 2번 인덱스 합친 것을 기준으로 역순 정렬
max_x = square_list[0][0] + square_list[0][2] - 1           # max_x에 x의 최댓값 저장

square_list.sort(key=lambda x:-(x[1]+x[3]))                 # 1번과 3번 인덱스 합친 것을 기준으로 역순 정렬
max_y = square_list[0][1] + square_list[0][3] - 1           # max_y에 y의 최댓값 저장

square = [[0] * (max_y - min_y + 1) for _ in range(max_x - min_x + 1)]      # square에 최대 최소 y값의 차이만큼 0을 채우고 그것을 최대 최소 x값의 차이만큼 반복

square_list = copy.deepcopy(temp_list)                                      # temp_list를 깊은 복사시켜 square_list에 담음
for t in range(tc):                                                         # 테스트 케이스만큼 반복
    for i in range(square_list[t][0] - min_x, square_list[t][0] + square_list[t][2] - min_x):       # 현재 색종이를 square내에 표시되도록 위치 조정
        for j in range(square_list[t][1] - min_y, square_list[t][1] + square_list[t][3] - min_y):   # 현재 색종이를 square내에 표시되도록 위치 조정
            square[i][j] = t + 1        # square의 해당 자리에 색종이 번호를 넣어줌

for idx in range(1, tc + 1):            # 테스트 케이스 만큼 반복
    cnt = 0                             # cnt 0으로 초기화
    for i in range(len(square)):        # square 반복
        cnt += square[i].count(idx)     # cnt에 해당 숫자 몇 개 있는지 더해 나감
    print(cnt)                          # cnt 출력