#ARITHMETIC ARRANGER: FCC PYTHON PROJECT 1
#arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True) true is answers inc
#32
#+ 8
#----
#40
# ANSWER: print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
# limit of 5 problems, + and - only, digits only, four digits max for numbers
#numbers should be right aligned, dashes between each problem

def arithmetic_arranger(arr,switch = False): #a default value for argument can be given
    a = len(arr)
    if a>5:
        print("error")
    else:
        for x in arr:
            b = "" #first num
            c = "" #second num
            d = 0 #num index
            e = "" #sign
            f = x
            for y in f: #change x to y for simplicity
                if y.isnumeric(): #checks if value is numberic
                # if f.index(y) != 0 checks if iteration is 1st or not
                    if d == 0:
                        b = b + y
                    if d == 1:
                        c = c + y
                else:
                    if y == "-" or y == "+":
                        e = y    
                        d = 1   
                    if y == "*" or y == "/":
                        c = 10000 # due to d not changing, forces error by making c too large for final if
            l = int(b)
            m = int(c)
            n = 0
            if e == "-":
                n = l - m
            if e == "+":
                n = l + m
            if e == "" or l>9999 or m>9999:
                print("error")
            else:
                if switch == False:
                    print(f"{l: >6}\n{e}{m: >5}\n------\n")                
                else:
                    print(f"{l: >6}\n{e}{m: >5}\n------\n{n: >6}\n") # > is to the right, ^ is to centre, < is to the left                

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"],True)
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])