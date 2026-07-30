#!/usr/bin/python3
Rectangle = __import__('4-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(repr(my_rectangle))
new_rectangle = eval(repr(my_rectangle))
print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))
