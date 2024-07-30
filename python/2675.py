N = int(input())
for n in range(N):
    T, text = input().split(" ")
    output = ""
    for t in text:
        output += (t * int(T))

    print(output)