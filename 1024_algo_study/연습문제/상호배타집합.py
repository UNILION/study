def make_set(x):
    pass

def find_set(x):
    pass

def union(x, y):
    pass

#1.
p = [0] * (6+1)

print(p)
print('----------------------------------')

#2.
union(1, 3)
print(p)
print('----------------------------------')

union(2, 3)
print(p)
print('----------------------------------')

union(5, 6)
print(p)
print('----------------------------------')

#3.
print(find_set(6))
print(find_set(3))
print(find_set(2))