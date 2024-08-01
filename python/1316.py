N = int(input())
cnt = 0
for n in range(N):
    word = input()
    check = ["" for i in range(len(word))]
    wcnt = len(word)
    for i in range(len(word)):
        if i == 0:
            check[i] = word[i]
        else:
            if word[i] != check[i-1] and word[i] in check:
                break
            else:
                check[i] = word[i]
                wcnt -= 1

    if wcnt == 1:
        cnt += 1    

print(cnt)