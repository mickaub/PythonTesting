class CountingUp :
    x = 0
    adder = 0
    def __init__(self,num):
        self.adder = num

    def increase(a):
        a.x = a.x + a.adder
        print(a.x)

an = CountingUp(3)
an.increase()
an.increase()