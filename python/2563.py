paper = [[0 for j in range(100)] for i in range(100)]
def painting(paper, x, y):
    for i in range(10):
        for j in range(10):
            paper[y+i][x+j] = 1
    return paper

N = int(input())
for n in range(N):
    x, y = map(int, input().split())

    paper = painting(paper, x, y)

# print(paper)
print(sum(list(map(sum, paper))))