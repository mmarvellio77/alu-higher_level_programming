#!/usr/bin/python3
print(("{:02d}, " * 99 + "{:02d}").format(*(i for i in range(100))))
