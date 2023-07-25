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

    def deposit():
        pass

    def withdraw():
        pass

    def get_balance():
        pass

    def transfer():
        pass

    def check_funds():
        pass
    
    def print(self):
        print(self.ledger)

food = Category("food")
clothing = Category("clothing")
entertainment = Category("entertainment")