c, r = map(int, input().split())            # 가로 세로 길이
number = int(input())                       # 찾을 번호

position = 0                                # 현재 번호
result = []                                 # 결과 위치
d = [1, -1]                                 # 행렬 조작
n = 0                                       # 움직일 값 감소
flag = 0                                    # 반복문 빠져나오게 할 변수
coordinate = [1, 0]                         # 현재 위치
if number > c * r:                          # 찾을 숫자가 전체 범위보다 크면
    print(0)                                # 0 출력
else:                                       # 찾을 숫자가 전체 범위 이내에 있으면
    while (position <= c * r):              # 현재 번호가 전체 번호가 작을 때 까지 반복
        for k in range(2):                  # 1과 -1 반복
            for j in range(r - n):          # r-n까지 반복
                coordinate[1] += d[k]       # 현재 위치의 y값을 1이나 -1 더함
                position += 1               # 현재 번호 + 1
                if position == number:      # 현재 번호랑 찾을 번호랑 같으면
                    result = coordinate     # 결과값에 현재 위치 넣어줌
                    flag = 1                # flag = 1
                    break                   # 탈출
            n += 1                          # 움직일 값 1증가시켜 감소
            if flag == 1:                   # flag가 1이면
                break                       # 탈출

            for i in range(c - n):          # c-n까지 반복
                coordinate[0] += d[k]       # 현재 위치의 x값에 1이나 -1 더함
                position += 1               # 현재 번호 + 1
                if position == number:      # 현재 번호랑 찾을 번호가 같으면
                    result = coordinate     # 결과값에 현재 위치 넣음
                    flag = 1                # flag = 1
                    break                   # 탈출
            if flag == 1:                   # flag가 1이면
                break                       # 탈출
        if flag == 1:                       # flag가 1이면
            break                           # 탈출

    print(*result)                          # 결과값 출력