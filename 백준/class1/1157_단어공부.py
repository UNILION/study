char = input()
char_list = [0] * 26
for c in char:
    if 65 <= ord(c) <= 90:
        char_list[ord(c)-65] += 1

    elif 97 <= ord(c) <= 122:
        char_list[ord(c)-97] += 1

max_x = max(char_list)
cnt = 0
for i in char_list:
    if max_x == i:
        cnt += 1
if cnt >= 2:
    print("?")
else:
    print(chr(char_list.index(max_x) + 65))