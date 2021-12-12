import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
n_list = deque()
for i in range(n):
    n_list.append(i + 1)
while len(n_list) > 1:
    n_list.popleft()
    n_list.append(n_list.popleft())
print(n_list.popleft())