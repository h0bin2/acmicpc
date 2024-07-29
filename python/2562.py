value = []
for i in range(9):
    value.append(int(input()))

m = max(value)
print(m)
print(value.index(m) + 1)