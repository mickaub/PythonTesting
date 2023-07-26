# FCC Project 3
"""
Category class
different budget categories like food, clothing and entertainment
ledger variable, which is a list
Methods:
deposit:
-appends to ledger in form of {"amount":amount, "description":description}
- if no description, description should be empty string
- accepts amount and description only
withdraw:
-amount and description similar to deposit
-amount should be stored as negative number
-if there are not enough funds, nothing should be added to the ledger
-should return True if withdrawal took place and False otherwise

get_balance:
-returns the current balance of the budget category based on the deposits
and withdrawals that have occurred

transfer:
-accepts amount and another budget category as arguments
-should add a withdrawal with the amount and description "Transfer to
(budget category)"
-add a deposit to the other budget category with amount and description:
"Transfer from (budget category)
-if there are not enough funds for transfer, nothing should be added to ledger
-should return True if transfer took place and False otherwise

check_funds:
-acccepts amount as argument
-returns False if amount is greater than the balance and returns True otherwise
-should be used by both the withdraw and the transfer method

When printed the budget object should display:
-A title line of 30 characters with category name centred within * characters
-A list of items in the ledger, with description followed by amount
-the first 23 character of description only, with amount right aligned and containing
two decimal spaces and maximum of 7 characters
-A line displaying the category total

Create a function called create_spend_chart outside of class
- takes a list of categories as an argument
- should return string that is a bar chart
- add all category withdrawals and calculcate percentage of total spending amount
- down the left side whould be 0-100 in 10s, followed by |, with o being chart display
and 0 having all o amounts, rounded down to nearest 10 otherwise
- horizontal line of 10 - should be below bars and each column should align with 2,5,8
"""

class Category:
    def __init__(self,name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self,amount,description = ""):  
        self.balance += amount      
        self.ledger.append({"amount:": amount, "description:": description})
        #for x in self.ledger:
        #    print(x)        

    def withdraw(self,amount,description = ""):
        if self.check_funds(amount) == True:
            self.balance -= amount
            amount = 0 - amount        
            self.ledger.append({"amount:": amount, "description:": description})
         #   for x in self.ledger:
         #       print(x)        
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self,amount,other):
        if self.check_funds(amount) == True:
            self.balance -= amount
            amount = 0 - amount
            other_name = other.name
            self.ledger.append({"amount:": amount, "description:": "Transfer to "+other_name})
        #    print(self.ledger)#temp
            amount = amount *-1
            other.balance += amount
            other.ledger.append({"amount:": amount, "description:": "Transfer from "+self.name})
         #   print(other.balance)#temp
        #    print(other.ledger)
            return True            
        else:
            return False            
    
    def check_funds(self, amount):        
        if self.balance<amount:
            return False
        else:
            return True
    
    def print(self):
        l = len(self.name)        
        side1 = 0
        side2 = 0
        if l%2==0:
            side1 = (30 - l)/2
            side2 = (30 - l)/2
        else:
            side1 = ((30 - l)/2)-0.5
            side2 = ((30 - l)/2)+0.5
        lside = "*" * int(side1) #multiplies string
        rside = "*" * int(side2)
        print(lside+self.name+rside)  
        for x in self.ledger:
            a = x.keys()
            b = x.values()
            plist = []
            for y in b:
                plist.append(y)
            plist[1] = plist[1][0:22]            
            plist[0] = '%.2f' % plist[0] # % says where to input % value
            desstr = "{:<23}".format(plist[1])
            amtstr = "{:>7}".format(plist[0])
            print(desstr+amtstr)
        balstr = '%.2f' % self.balance
        totstr = "{:<20}".format("Total")+"{:>10}".format(balstr)
        print(totstr)

def create_spend_chart(*args):
    for x in args:
        print("Bal",x.balance)
    for x in range(11):
        a = x * 10
        b = 100 - a
        print("{:<3}".format(b),"|")

food = Category("food")
clothing = Category("clothing")
entertainment = Category("entertainment")
food.deposit(300,"Deposit")
food.transfer(100,clothing)
food.print()

create_spend_chart(food,clothing)
"""
EXAMPLE:
def setUp(self):
    self.food = budget.Category("Food")
    self.entertainment = budget.Category("Entertainment")
    self.business = budget.Category("Business")

def test_deposit(self):
    self.food.deposit(900, "deposit")
    actual = self.food.ledger[0]
    expected = {"amount": 900, "description": "deposit"}
    self.assertEqual(actual, expected, 'Expected `deposit` method to create a 
    specific object in the ledger instance variable.')
"""