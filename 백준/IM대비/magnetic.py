''' # 10시 2분 문제 읽음 -> 10시 26분 시작
100줄 검사를 100번 실행
1. 위에부터 가로로 한 줄 씩 검사
2. 1(N극)이면 아래 0일 시 아래로만 이동
3. 2(S극)이면 위에 0일 시 위로만 이동
4. 1 발견 시 밑에 2를 발견하면 교착 + 1
'''

import sys
sys.stdin = open("magnetic_input.txt")
# 0. 입력
for t in range(1, 11):                  # 10개의 테스트 케이스
    magnetic = 0 # 교착 상태 갯수
    square = []
    square_width = int(input())         # 정사각형 한 변의 길이
    for _ in range(square_width):       # 정사각형 길이만큼 반복
        square.append(list(map(int, input().split())))  # 각 줄을 리스트로 받음
    
    # 최대로 돌 수 있는 횟수 = 1 + 2 + ... + square_width 
    full = 0
    for f in range(1, square_width +  1):
        full += f

    for _ in range(f):                      # 최대 횟수
        for i in range(square_width):       # 행, 정사각형 길이만큼 반복, 한 사이클
            for j in range(square_width):   # 열, 정사각형 길이만큼 반복, 한 사이클

# 1. 위에부터 가로로 한 줄 씩 검사
                current = square[i][j]      # 현재 값

# 2. 1(N극)이면 아래 0일 시 아래로만 이동
                if current == 1:                    # 현재 N극이면
                    try:
                        if square[i + 1][j] == 0:   # 아래가 비어있을 시
                            square[i + 1][j] = 1    # 아래로 이동
                            square[i][j] = 0        # 현재 자리를 0으로 만듦, 이유는 모르겠는데 current로 하면 안 먹히는데 square[i][j]로 하니까 먹힘..
                    except IndexError:              # 마지막 줄이라 인덱스 에러
                        square[i][j] = 0            # 마지막 줄에 N극 있을 시 비어 있게 만듦, 리스트 참조가 아닌 그 값을 받아와서 current는 안 됨

# 3. 2(S극)이면 위에 0일 시 위로만 이동
                elif current == 2:                  # 현재 S극이면
                    if i == 0:                      # 첫 줄이면 위로 내보내야 하므로 (-1이 되면 마지막 줄을 가르키므로)
                        square[i][j] = 0            # 마지막 줄에 N극 있을 시 비어 있게 만듦

                    elif square[i - 1][j] == 0:     # 위가 비어있을 시
                        square[i - 1][j] = 2        # 위로 이동
                        square[i][j] = 0            # 현재 자리를 0으로 만듦
                        

# 4. 1 발견 시 밑에 2를 발견하면 교착 + 1
        # for q in range(len(square)):
        #     print(square[q])
        # print()

    for x in range(square_width - 1):   # 행, 정사각형 길이 - 1만큼 반복
        for y in range(square_width):   # 열, 정사각형 길이만큼 반복
            if (square[x][y] == 1) and (square[x + 1][y] == 2): # 만약 현재가 1이고 아래가 2이면
                magnetic += 1           # 교착 + 1
# 출력
    print("#{} {}".format(t, magnetic))


"""
10
2 0 0 0 0 0 0 0 0 0
0 0 2 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 2 0 0 0
0 0 0 0 0 2 1 0 0 0
2 0 2 0 0 2 1 0 0 0
2 0 2 0 0 0 0 0 0 0
0 2 0 0 0 0 0 0 0 0
0 0 0 0 0 2 0 0 0 0
1 0 0 0 0 1 0 1 0 1
"""

"""
3
1 0 1
1 0 0
1 2 0
"""