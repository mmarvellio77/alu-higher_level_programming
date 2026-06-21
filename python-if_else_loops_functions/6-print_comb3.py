#!/usr/bin/python3
print(("{}{}, " * 44 + "{}{}").format(
    *sum(((i, j) for i in range(10) for j in range(10) if i < j), ())
))
