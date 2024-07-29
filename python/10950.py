n = int(input())
answer = []
for i in range(n):
    a, b = map(int, input().split())
    answer.append(a+b)

for aw in answer:
    print(aw)