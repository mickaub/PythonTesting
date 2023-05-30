lineCounter = open('textToRead.txt')
count = 0
for line in lineCounter:
    count = count + 1
print('Line Count:', count)