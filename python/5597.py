output = [n for n in range(1, 31)]
for i in range(28):
    n = int(input())
    output.remove(n)

for out in output:
    print(out)