N = int(input())
lst = list(map(int, input().split()))
M = max(lst)
output = 0.0

for l in lst:
    output += (l / M * 100)

print(output / N)