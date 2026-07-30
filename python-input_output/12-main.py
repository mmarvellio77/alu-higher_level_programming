#!/usr/bin/python3
pascal_triangle = __import__('12-pascal_triangle').pascal_triangle
def print_triangle(triangle):
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))
print_triangle(pascal_triangle(5))
