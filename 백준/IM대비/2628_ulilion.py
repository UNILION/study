import sys
input = sys.stdin.readline

col, row = map(int, input().split())    # 열과 행 받기
paper_list = []                         # 종이 가위질 리스트
tc = int(input())                       # 테스트 케이스
for _ in range(tc):                     # 테스트 케이스 수만큼 반복
    paper_list.append(list(map(int, input().split())))  # 종이 가위질 input 받아서 리스트에 리스트로 넣기

zero = [0, row]                         # 0 : 가로 (0과 가로 길이)
one = [0, col]                          # 1 : 세로 (0과 세로 길이)
for paper in paper_list:                # 가위질 횟수만큼 반복
    if paper[0] == 0:                   # 가로이면
        zero.append(paper[1])           # zero 리스트에 점선 번호 추가
    else:                               # 세로이면
        one.append(paper[1])            # one 리스트에 점선 번호 추가

zero.sort()                               # zero 정렬 (종이가 잘린 순으로 보기 위해)
result = []                               # result 리스트 생성
for i in range(1, len(zero)):             # 인덱스 1부터 마지막 이전 인덱스까지
    result.append(zero[i] - zero[i - 1])  # result에 zero의 큰 인덱스에서 이전 인덱스 뺀 값 추가

one.sort()                                # one 정렬 (종이가 잘린 순으로 보기 위해)
result2 = []                              # result2 리스트 생성
for j in range(1, len(one)):              # 인덱스 1부터 마지막 이전 인덱스까지
    result2.append(one[j] - one[j - 1])   # result2에 one의 큰 인덱스에서 이전 인덱스 뺀 값 추가

print(max(result) * max(result2))         # result의 최댓값과 result2의 최댓값의 곱을 출력