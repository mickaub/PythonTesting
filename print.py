print('Hello')
x = 3
if x == 3 :
    print(x)
rawstr = input('enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0 :
    print('Nice')
else:
    print('Not a number')
print('\U0001F642')