#ARITHMETIC ARRANGER: FCC PYTHON PROJECT 1
#arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True) true is answers inc
#32
#+ 8
#----
#40
# ANSWER: print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# limit of 5 problems, + and - only, digits only, four digits max for numbers
#numbers should be right aligned, dashes between each problem
# TO DO: start from array, max of 5 problems in array
d = "9999 + 9999"
e = ""
f = ""
g = 0
h = ""
for x in d:
    if x.isnumeric(): #checks if value is numberic
        if g == 0:
            e = e + x
        if g == 1:
            f = f + x
    else:
        if x == "-" or x == "+":
            h = x    
            g = 1   
        if x=="*" or x=="/":
            f = 10000 # due to g not changing, forces error by making f too large for final if
l = int(e)
m = int(f)
n = 0
if h == "-":
    n = l - m
if h == "+":
    n = l + m

if h == "" or l>9999 or m>9999:
    print("error")
else:
    print(l,m,n)
    print(f"{l: >6}\n{h}{m: >5}\n------\n{n: >6}") # > is to the right, ^ is to centre, < is to the left