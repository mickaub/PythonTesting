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