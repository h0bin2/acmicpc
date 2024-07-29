price = int(input())
answer = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    answer += (a*b)

if answer == price:
    print("Yes")
else:
    print("No")