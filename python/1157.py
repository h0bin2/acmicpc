text = input().lower()
output = {}
for t in text:
    try:
        output[t] += 1
    except:
        output[t] = 1

sorted_output = sorted(output.items(), key = lambda item: item[1], reverse=True)
if len(sorted_output) > 1:
    if sorted_output[0][1] == sorted_output[1][1]:
        print('?')
    else:
        print(sorted_output[0][0].upper())
else:
    print(sorted_output[0][0].upper())