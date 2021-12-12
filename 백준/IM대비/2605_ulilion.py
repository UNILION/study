import sys
input = sys.stdin.readline

# 학생들은 자신이 뽑은 번호표대로 인덱스가 앞으로 이동함
# ex) 3명이 있으면 idx가 0 ~ 2 까지인데 여기에 4번이 1번을 뽑았으면 4번은 idx 2로, 3은 3으로 이동됨
# 고로 번호 숫자만큼 학생이 빠진 뒤 번호표를 뽑은 학생이 추가되고 빠진 학생을 다시 추가 시킴

student = int(input())                              # 학생 수 입력받음
temp = []                                           # 정렬될 학생을 담을 변수
student_list = list(map(int, input().split()))      # 학생 이동 번호표
stack = []                                          # 이동할 때 임시로 담을 학생 변수
for i in range(1, student + 1):                     # sttudent 수 만큼 반복
    for _ in range(student_list[i - 1]):            # 학생 번호 수 만큼 반복
        if temp:                                    # temp 내 요소가 존재하면
            stack.append(temp.pop())                # stack에 temp 요소 하나씩 담음 (번호표의 숫자만큼)
    temp.append(i)                                  # temp에 학생 번호 넣어줌
    for _ in range(student_list[i - 1]):            # 학생 번호 수 만큼 반복
        if stack:                                   # stack이 있으면
            temp.append(stack.pop())                # temp에 stack 하나씩 다시 담음

for i in temp:              # temp에 있는 것을 하나씩 출력
    print(i, end = " ")     # 공백을 두고 출력