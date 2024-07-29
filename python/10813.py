N, M = map(int, input().split())
output = [n for n in range(1, N+1)]
for i in range(M):
    i, j = map(int, input().split())
    
    temp = output[i-1]
    output[i-1] = output[j-1]
    output[j-1] = temp

print(' '.join(map(str, output)))