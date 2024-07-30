output = [0 for x in range(26)]

text = input()
for i in range(len(output)):
    if chr(i+97) in text:
        output[i] = text.index(chr(i+97))
    else:
        output[i] = -1

print(' '.join(map(str, output)))