t = int(input())
if t % 4 == 0 and (t % 100 != 0 or t % 400 == 0):
    print(1)
else:
    print(0)