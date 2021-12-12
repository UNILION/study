"""
1. 첫 줄은 무조건 흰색
2. 두 번째 줄 부터 흰색과 파란색 비교
3. 같을 시 파란색으로 도배
4. 그 다음부턴 파란색과 빨간색 비교
5. 같을 시 빨간색으로 도배
6. 마지막줄은 무조건 빨간색
"""
tc = int(input())
for t in range(tc):
    square_list = []
    result = 0

    N, M = map(int, input().split())
    for _ in range(N):
        square_list.append(list(input()))

    for n in range(N):
        w = 0
        b = 0
        r = 0

        for m in range(M):
# 1. 첫 줄은 무조건 흰색
            if n == 0:
                if square_list[n][m] != 'W':
                    square_list[n][m] = 'W'
                    result += 1
            
# 2. 마지막줄은 무조건 빨간색
            elif n == N - 1:
                if square_list[n][m] != 'R':
                      square_list[n][m] = 'R'
                      result += 1

# 3. 두 번째 줄 부터 흰색과 파란색 비교
# 4. 같을 시 파란색으로 도배
# 5. 그 다음부턴 파란색과 빨간색 비교
# 6. 같을 시 빨간색으로 도배           
            else:
                if square_list[n][m] == 'W':
                    w += 1
                elif square_list[n][m] == 'B':
                    b += 1
                elif square_list[n][m] == 'R':
                    r += 1

        if (n != 0) and (n != N - 1):
            if square_list[n - 1][m] == 'W':
                if b >= w:
                    result += w
                    square_list[n - 1] = 'B' * M
                else:
                    result += b
                    square_list[n - 1] = 'W' * M

            elif square_list[n-1][m] == 'B':
                if r >= b:
                    result += b
                    square_list[n - 1] = 'R' * M
                else:
                    result += r
                    square_list[n - 1] = 'B' * M
            
            if n == N - 2:
                if square_list[n][m] == 'W':
                    result -= w
                    result += b
                    square_list[n] =  'B' * M

    print(square_list)
    print("#{} {}".format(t, result))