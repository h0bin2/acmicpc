N = int(input())
cnt = 0
for i in range(N):
    check = []
    word = input()
    for j in range(len(word)):
        try:
            if word[j] != word[j+1]:
                if word[j] in check:
                    continue
                else:
                    check.append(word[j])
                    cnt += 1
        except:
            if word[j] not in check:
                check.append(word[j])
                cnt += 1
print(cnt)