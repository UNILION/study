#구글링
paper = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    
    #사각형 부분만 1로 바꾸어줌
    for i in range(x1, x2):
        for j in range(y1, y2):
            paper[i][j] = 1

answer = 0
for row in paper:
    answer += sum(row)
print(answer)

""" 거의 다 정답이 나오는데 엣지 케이스를 못 찾겠어서 포기
square = []         # 사각형 정보를 담을 리스트

for _ in range(4):
    square.append(list(map(int, input().split())))
square = sorted(square, key = lambda x : x[0])  # 좌측 하단 x 값을 기준으로 정렬

min_x = min(list(zip(*square))[0])  # 좌측 하단 x 값 중 최소값
min_y = min(list(zip(*square))[1])  # 좌측 하단 y 값 중 최소값
max_x = max(list(zip(*square))[2])  # 좌측 하단 x 값 중 최대값
max_y = max(list(zip(*square))[3])  # 좌측 하단 y 값 중 최대값

result = 0

for i in range(min_x, max_x):       # x 범위만큼 반복
    min_y, max_y = max_y, min_y     # 무조건 값 변경이 일어나게 최소 최대 y를 바꿔줌
    flag = 0                        # 상자가 해당 x 값에 있는지 확인
    for j in range(4):
        if square[j][0] <= i < square[j][2]:    # 현재 x값이 상자의 x 범위에 들어오면
            flag = 1                            # flag = 1
            if square[j][1] < min_y:            # 현재 상자의 최소 y값이 min_y보다 작으면
                min_y = square[j][1]            # min_y를 현재 상자의 최소 y값으로 교체

            if max_y < square[j][3]:            # 현재 상자의 최대 y값이 max_y보다 크면
                max_y = square[j][3]            # max_y를 현재 상자의 최대 y값으로 교체
    if flag == 1:                               # 현재 x에 상자가 있으면
        result += (max_y - min_y)               # result에 높이 차를 더해줌 (x범위가 1이기 때문)
        
    min_y = 0                                   # 위에서 max랑 바꿔줄 것이기에 0으로 만듦
    max_y = 101                                 # 위에서 min이랑 바꿔줄 것이기에 101으로 만듦

print(result)
"""