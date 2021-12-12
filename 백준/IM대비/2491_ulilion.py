# 문제에서 3이상인 경우가 없으므로 2를 출력한다는 낚시에 낚여서 30분 허비함

N = int(input())                                # 수열의 길이
N_list = list(map(int, input().split()))        # 수열 리스트

N_min, N_max = N_list[0], N_list[0]             # 리스트 중 작은 값, 큰 값
min_cnt, max_cnt = 0, 0                         # 작은 갯수, 큰 갯수
result_min, result_max = 0, 0                   # 최종적으로 연속적으로 작은 갯수, 큰 갯수

for i in range(N):                  # 수열의 길이만큼 반복
    if N_list[i] <= N_min:          # 만약 현재 요소가 N_min보다 작거나 같으면
        min_cnt += 1                # min_cnt를 1 더함
        if result_min < min_cnt:    # result_min이 min_cnt보다 작다면
            result_min = min_cnt    # result_min을 min_cnt로 교체함
    else:                           # 현재요소가 N_min보다 크면
        min_cnt = 1                 # min_cnt를 1로 초기화

    if N_list[i] >= N_max:          # 만약 현재 요소가 N_max보다 크거나 같으면
        max_cnt += 1                # max_cnt를 1 더함
        if result_max < max_cnt:    # result_max가 max_cnt보다 작다면
            result_max = max_cnt    # result_max를 max_cnt로 바꿈
    else:                           # 현재요소가 N_amx보다 작으면
        max_cnt = 1                 # max_cnt를 1로 초기화
    
    N_min, N_max = N_list[i], N_list[i]     # N_min과 N_max를 현재 요소로 바꿔줌

if result_min >= result_max:              # result_min이 result_max 보다 크거나 같으면
    print(result_min)                       # result_min 값 출력

else:                                       # result_min이 result_max 보다 작으면
    print(result_max)                       # result_max 값 출력