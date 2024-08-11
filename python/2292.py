N = int(input())

cnt = 1
room = 1
for n in range(N):
    if room % 6 == 0:
        cnt += 1
    room += 1