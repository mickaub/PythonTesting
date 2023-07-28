# FCC Project 4
"""
rectangle class and square class

rectangle class:
width and height arguments
methods:
set_width
set_height
get_area
    returns width x height
get_perimeter
    returns 2xwidth + 2xheight
get_diagonal                    ** means to the power of
    (width to the power of 2 + height to the power of 2) to the power of .5
get_picture
    string made of * to show shape
    \ n at the end of each line
    if width or height is larger than 50, should return string of "too big for picture"
get_amount_inside
    returns number of times a passed in shape could fit inside shape
When represented as string should output Rectangle(width=x,height=y)

square class:
a subclass of rectangle
a single side length is passed in during creation
the __init__ methods should store the side length in both the height and width
attributes from the rectangle class
should be able to access the rectangle class methods but should also contain
the set_side method
When represented as string should output Square(side=x)
set_width and set_height methods should set both the width and the height

"""
class rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height

    def set_width(self,nwidth):
        self.width = nwidth
        print(self.width)
    
    def set_height(self,nheight):
        self.height = nheight
        print(self.height)

    def get_area(self):
        area = self.width * self.height
        print(area)

    def get_perimeter(self):
        per = (2 * self.width)+(2 * self.height)
        print(per)

    def get_diagonal(self):
        diag = (self.width**2 + self.height**2)**0.5
        print(diag)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            print("too big for picture")

    def get_amount_inside(self,object):
        pass

    def __str__(self):
        pass

class square(rectangle):
    def __init__(self, side, height = 0):
        #super().__init__(width, height)
        self.width = side
        self.height = side

    def set_width():
        pass
    
    def set_height():
        pass

    def set_side():
        pass

    def __str__(self):
        pass

rect1 = rectangle(2,3)
rect1.set_height(4)
rect1.get_diagonal()