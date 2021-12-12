import time
import sys
sys.stdin = open('input.txt')
start = time.time()

tc = int(input())      # 테스트 케이스
for t in range(tc):
    n = int(input())        # 배열의 크기
    n_list = []
    cnt = 0

    for i in range(n):
        n_list.append(list(input()))


    for i in range(n):
        for j in range(n):
            if n_list[i][j] == 'A' or n_list[i][j] == 'B' or n_list[i][j] == 'C':
                if 0 <= (i - 1) and n_list[i - 1][j] == 'H':
                    n_list[i - 1][j] = 'X'
                if (i + 1) < n and n_list[i + 1][j] == 'H':
                    n_list[i + 1][j] = 'X'
                if 0 <= (j - 1) and n_list[i][j - 1] == 'H':
                    n_list[i][j - 1] = 'X'
                if (j + 1) < n and n_list[i][j + 1] == 'H':
                    n_list[i][j + 1] = 'X'
            
            if n_list[i][j] == 'B' or n_list[i][j] == 'C':
                if 0 <= (i - 2) and n_list[i - 2][j] == 'H':
                    n_list[i - 2][j] = 'X'
                if (i + 2) < n and n_list[i + 2][j] == 'H':
                    n_list[i + 2][j] = 'X'
                if 0 <= (j - 2) and n_list[i][j - 2] == 'H':
                    n_list[i][j - 2] = 'X'
                if (j + 2) < n and n_list[i][j + 2] == 'H':
                    n_list[i][j + 2] = 'X'

            if n_list[i][j] == 'C':
                if 0 <= (i - 3) and n_list[i - 3][j] == 'H':
                    n_list[i - 3][j] = 'X'
                if (i + 3) < n and n_list[i + 3][j] == 'H':
                    n_list[i + 3][j] = 'X'
                if 0 <= (j - 3) and n_list[i][j - 3] == 'H':
                    n_list[i][j - 3] = 'X'
                if (j + 3) < n and n_list[i][j + 3] == 'H':
                    n_list[i][j + 3] = 'X'

    for i in range(n):
        for j in range(n):
            if n_list[i][j] == 'H':
                cnt += 1
    print("#{} {}".format(t, cnt))
end = time.time()
print('time elapsed:', end - start)