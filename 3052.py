output = 0
lst = []
for i in range(10):
    n = int(input())
    if n % 42 in lst:
        continue
    lst.append(n % 42)
    output += 1
print(output)