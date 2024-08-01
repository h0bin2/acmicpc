N = int(input())
space = 1
for i in range(N):
    temp = " " * (N-space) + ('*' * (space * 2 - 1))
    space += 1
    print(temp)
space -= 1
for i in range(N):
    space -= 1
    temp = " " * (N-space) + ('*' * (space * 2 - 1))
    print(temp)
    if space == 0:
        break