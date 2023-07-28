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
        else:
            line = "*" * self.width
            line += "\n"
            shape = line * self.height
            print(shape)

    def get_amount_inside(self,object):
        widthfit = self.width / object.width
        heightfit = self.height / object.height
        newarea = int(widthfit) * int(heightfit)        
        print(newarea)
        print(widthfit,heightfit)

    def __str__(self):
        a = str(self.width)
        b = str(self.height)
        return "Rectangle" + "(width=" + a + ",height=" + b + ")"

class square(rectangle):
    def __init__(self, side, height = 0):
        #super().__init__(width, height)
        self.width = side
        self.height = side

    def set_width(self,nside):
        self.width = nside
        self.height = nside
    
    def set_height(self,nside):
        self.width = nside
        self.height = nside

    def set_side(self,nside):
        self.width = nside
        self.height = nside

    def __str__(self):
        a = str(self.width)
        return "Square(side=" + a + ")"

rect1 = rectangle(2,3)
rect1.set_height(4)
rect1.get_diagonal()
rect1.get_picture()
print(rect1)
rect2 = rectangle(5,4)
rect2.get_amount_inside(rect1)
square1 = square(4)
square1.set_height(5)
square1.get_picture()
print(square1)