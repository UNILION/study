N_list = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'], ['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
string = input()
result = 0
for s in string:
    cnt = 2
    for n in N_list:
        cnt += 1
        if s in n:
            result += cnt
print(result)