N, M = map(int, input().split())
output = [0 for x in range(N)]

for i in range(M):
    i, j, k = map(int, input().split())
    for u in range(i, j+1):
        output[u-1] = k

print(' '.join(map(str, output)))