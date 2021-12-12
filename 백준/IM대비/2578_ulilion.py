cnt = 0     # 전체 빙고 줄 수
cnt1 = 0    # 대각선 빙고 수
cnt2 = 0    # 역대각선 빙고 수
cnt3 = 0    # 가로 빙고 수
cnt4 = 0    # 세로 빙고 수
result = 0  # 몇 번째 숫자에서 3개 이상 빙고인지
flag = 0    # 3개 다 찾을 시 for 문 완전 탈출을 위한 flag 변수
participant = []    # 참가자 빙고 리스트
moderator = []      # 사회자 빙고 리스트
for _ in range(5):  # 5줄
    participant.append(list(map(int, input().split()))) # 참가자 빙고 리스트, extend 썼으면 try 안 써도 됐을지도...
    
for _ in range(5):  # 5줄
    moderator.append(list(map(int, input().split())))   # 사회자 빙고 리스트

for i in range(5):          # 사회자 i 줄
    for j in range(5):      # 사회자 j 열
        for k in range(5):  # 참가자 k 줄
            try:            # 없는 번호 부를까봐 넣음
                find = participant[k].index(moderator[i][j])    # 사회자가 부른 숫자 확인
                participant[k][find] = 0            # 참가자 빙고 리스트 중 해당 자리 0으로 치환
                for x in range(5):                  # 사회자가 번호를 부르면 빙고가 됐는지 확인
                    for y in range(5):
                        # 가로 검사
                        if participant[x][y] == 0:  # 해당 자리가 0이면
                            cnt3 += 1               # cnt3 + 1
                        
                        # 세로 검사
                        if participant[y][x] == 0:  # 해당 자리가 0이면
                            cnt4 += 1               # cnt4 + 1

                    if cnt3 == 5:                   # cnt3이 5이면 가로 빙고 이므로
                        cnt += 1                    # cnt + 1
                    cnt3 = 0                        # cnt3을 0으로 다시 초기화
                    if cnt4 == 5:                   # cnt4가 5이면 세로 빙고이므로
                        cnt += 1                    # cnt4 + 1
                    cnt4 = 0                        # cnt4를 0으로 다시 초기화
                    # 대각선 검사
                    if participant[x][x] == 0:      # 대각선이 0이면
                        cnt1 += 1                   # cnt1 + 1
                    if participant[x][4 - x] == 0:  # 역 대각선이 0이면
                        cnt2 += 1                   # cnt2 + 1
                if cnt1 == 5:                       # cnt1이 5이면
                    cnt += 1                        # cnt + 1
                cnt1 = 0                            # cnt1을 0으로 기화
                if cnt2 == 5:                       # cnt2가 5이면
                    cnt += 1                        # cnt + 1
                cnt2 = 0                            # cnt2를 0으로 초기화
                if cnt >= 3:                        # cnt가 3이상이면 빙고 3줄 이상 이므로
                    result = 5 * i + j + 1          # result에 5 * i * j + 1값을 넣음 (n번째 번호)
                    flag = 1                        # flag를 1로 세움
                    break                           # 탈출
                cnt = 0                             # 다음 반복을 위해 cnt 0으로 초기화
                        
            except:     # 혹시나 오류가 일어나면
                pass    # 패스
        if flag == 1:   # 빙고 3줄이상이므로
            break       # 탈출
    if flag == 1:       # 빙고 3줄 이상이므로
            break       # 탈출
    
print(result)           # 결과 출력