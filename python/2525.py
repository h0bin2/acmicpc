A, B = map(int, input().split())
C = int(input())

print(str((A + ((B+C) // 60)) % 24) + ' ' + str((B+C) % 60))