import sys
input = sys.stdin.readline

def painting(i):    # 큰 수 부터 비교하기에 i = 4부터비교
    if first_painting.count(i) > second_painting.count(i):  # first의 i 갯수가 더 많으면
        return 'A'  # A 출력
    elif first_painting.count(i) == second_painting.count(i):   # 둘이 현재 i 갯수가 같으면
        if i == 1:      # i가 1이면 끝까지 돈 것이므로
            return 'D'  # D를 반환
        return painting(i - 1)  # 같으면 그 다음 숫자를 비교해야 하고 반환 값을 반환함
    elif first_painting.count(i) < second_painting.count(i):  # second의 i 갯수가 더 많으면
        return 'B'      # B를 반환
        
N = int(input())        # 라운드 수
for _ in range(N):      # 라운드 수 만큼 반복
    first = list(map(int, input().split()))  # 첫번째 아이의 딱지 갯수와 종류
    second = list(map(int, input().split())) # 두번째 아이의 딱지 갯수와 종류

    first_count = first[0]      # 첫번째 아이의 딱지 갯수
    first_painting = []         # 첫번째 아이의 딱지 종류
    second_count = second[0]    # 두번째 아이의 딱지 갯수
    second_painting = []        # 두번째 아이의 딱지 종류
    
    for i in range(1, first_count + 1): # 1부터 딱지 갯수만큼 반복
        first_painting.append(first[i]) # first_painting에 첫번째 아이의 종류를 담음
    
    for i in range(1, second_count + 1): # 1부터 딱지 갯수만큼 반복
        second_painting.append(second[i]) # second_painting에 두번째 아이의 종류를 담음
    
    print(painting(4))         # painting에 4를 넣어 결과값을 출력