"""
This file contains algorithms that do decimal to octal conversions and vice versa.
Important note: The decimal numbers here are positive integers.
"""

def dec_to_oct(dec: int):
    res = ""
    while dec != 0:
        res = str(dec % 8) + res
        dec //= 8
    return res

def oct_to_dec(octal: str):
    result = 0
    for n in range(len(octal) - 1, -1, -1):
        result += int(octal[n]) * 8 ** (len(octal) - 1 - n)
    return result

if __name__ == "__main__":
    import os
    result = dec_to_oct(int(os.getenv("NUMBER")))
    print(result)
    print(oct_to_dec(result))
