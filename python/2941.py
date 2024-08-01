croatia = input()
croatia_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for word in croatia_list:
    croatia = croatia.replace(word, '*')
    
print(len(croatia))