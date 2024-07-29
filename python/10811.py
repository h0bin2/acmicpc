N, M = map(int, input().split())
output = [n for n in range(1, N+1)]
for i in range(M):
    i, j = map(int, input().split())
    rev = list(reversed(output[i-1:j]))
    for r in rev:
        output[i-1] = r
        i += 1

print(' '.join(map(str, output)))