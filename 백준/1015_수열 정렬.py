import sys                  # input 쓰기 위한 모듈
input = sys.stdin.readline

test = input()
result = list(map(int, input().split(" ")))
resulted = sorted(result)
result_list=[0 for _ in range(int(test))]
for i in range(int(test)):
    result_list[result.index(resulted[i])] = i
    result[result.index(resulted[i])] = -1
for j in result_list:
    print(j, end=" ")