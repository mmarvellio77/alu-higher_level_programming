#!/usr/bin/python3
print(("{} = 0x{:x}\n" * 99).format(
    *sum(((i, i) for i in range(99)), ())
), end="")
