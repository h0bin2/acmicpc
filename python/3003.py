chess = {
    0:1,
    1:1,
    2:2,
    3:2,
    4:2,
    5:8
}

data = list(map(int, input().split()))
output = []
for i in range(len(data)):
    c = chess[i]
    d = data[i]
    if c != d:
        output.append(c-d)
    else:
        output.append(0)

print(' '.join(map(str, output)))