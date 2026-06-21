#!/usr/bin/python3
print(("{} = 0x{:x}\n" * 99).format(
    *(x for i in range(99) for x in (i, i))
), end="")
