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

if __name__ == "__main__":
    import os 
    print(dec_to_oct(int(os.getenv("NUMBER"))))

