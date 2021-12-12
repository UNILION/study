fact = [1] * 13
for i in range(2, 13):
    fact[i] = fact[i - 1] * i
print(fact[int(input())])