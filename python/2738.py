N, M = map(int, input().split())

array1 = []
array2 = []

for i in range(N):
    array1.append(list(map(int, input().split())))

for i in range(N):
    array2.append(list(map(int, input().split())))

output = []
for i in range(N):
    temp = []
    for j in range(M):
        print(array1[i][j] + array2[i][j], end=' ')
    print("")