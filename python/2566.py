point = [0, 0]
max_value = 0
for i in range(9):
    temp = list(map(int, input().split()))
    mv = max(temp)
    mi = temp.index(mv)
    if mv >= max_value:
        max_value = mv
        point = [i + 1, mi + 1]
print(max_value)
print(' '.join(map(str, point)))