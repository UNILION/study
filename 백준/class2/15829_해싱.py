import sys
input = sys.stdin.readline

N = int(input())
string = input()
cnt = 0
result = 0
for x in range(N):
    result += (ord(string[x]) - 96) * (31 ** cnt)
    cnt += 1
print(result % 1234567891)