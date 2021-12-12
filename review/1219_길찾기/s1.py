import sys
sys.stdin = open('input.txt')

def dfs():
    global result   # 결과 값, 길 있으면 1, 없으면 0
    result = 0      # result 초기화
    stack = [0]     # stack은 모든 길 확인 용도로 0으로 초기화

    while stack:    # stack이 빌 때 까지 반복
        s = stack.pop() # satck 안에 있는 값을 pop
        
        if s == 99:     # 도착점인 99와 s가 같다면 길이 있으므로
            result = 1  # result에 1을 넣어주고
            break       # 탈출

        for i in temp_list[s]:  # temp_list의 s번째 인덱스 값들을
            stack.append(i)     # stack에 넣어줌
    

for t in range(1, 11):  # 테스트 케이스 갯수
    T, E = map(int, input().split())    # 테스트 케이스 번호, 간선 갯수
    E_list = list(map(int, input().split()))    # 간선 정보 리스트
    temp_list = [[] for _ in range(100)]        # 간선의 인덱스에 맞는 연결 정보 리스트
    for x in range(0, len(E_list), 2):          # 짝수 인덱스 = 인덱스 번호, 홀수 인덱스 = 인덱스에 연결된 간선 정보
        temp_list[E_list[x]].append(E_list[x + 1])  # 짝수 인덱스에 홀수 인덱스 번호 넣어주기
    dfs()   # dfs 함수 돌기

    print("#{} {}".format(t, result))   # 결과 출력