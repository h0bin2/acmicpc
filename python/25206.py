grades = {
    'A+':4.5,
    'A0':4.0,
    'B+':3.5,
    'B0':3.0,
    'C+':2.5,
    'C0':2.0,
    'D+':1.5,
    'D0':1.0,
    'F':0.0
}

output = 0
score_sum = 0
for i in range(20):
    subject, score, grade = map(str, input().split())
    if grade not in ('P'):
        output += (float(score) * grades[grade])
        score_sum += float(score)
print(round(output/score_sum, 6))