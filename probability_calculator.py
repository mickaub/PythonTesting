#FCC Project 5
"""
Creata a Hat Class with variable amount of arguments (*args).
Quantity will always be at least 1.
Arguments should be converted into contents instance variable,
with contents being a list of strings that contain the quantity
of each category sequentially.
eg. Hat(yellow=3)
contents = ["yellow","yellow","yellow"]

draw method:
accepts argument indicating the number of balls to draw out of hat.
should remove balls at random from contents and return the results
as a new list of strings.
If the number of balls to draw exceeds the available quantity,
return all of the balls.

seperate experiment function:
arguments:
hat: hat object which contains balls should be copied into the function
expected_balls: the exact group of balls to attempt to draw from the hat.
eg. expected_balls should be {"blue":2, "red":1}
num_balls_drawn: the number of balls to draw out of the hat for each experiment.
num_experiments: the number of experiments to perfrom

The function should return a probability between 1 and 0.

eg. hat = Hat(black=6,red=4,green=3)
probability = experiment(hat=hat,expected_balls={"red":2,"green":1},
num_balls_drawn=5,num_experiments=2000)
"""
import random

class Hat:
    def __init__(self,**hat_list): #use ** to accept equals sign with argument,
        #with the value being turned into a dictionary (object)
        self.hats = hat_list
        self.contents = []
        for x in self.hats:
            name = x #key
            quantity = self.hats[x] #value
            for y in range(quantity):
                self.contents.append(name)            
            
        print(self.contents)
    def draw(self,draws):
        if draws>=len(self.contents):
            print(self.contents)
            return self.contents            
        else:
            print(draws) # need to randomise draws

hat = Hat(black=6,red=2)
hat.draw(9)