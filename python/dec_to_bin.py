"""
This file contains some algorithms to convert decimal numbers to binary.
One important note: the decimal numbers discussed here are positive integers.
"""

def dec_to_bin_remainder(dec: int):
    # make sure dec is a positive integer
    if dec < 0: raise ValueError("The decimal number must be a positive integer!")
    res = ""
    while dec > 0:
        res = str(dec % 2) + res 
        dec //= 2
    return f"0b{res}"


# test some stuff
if __name__ == "__main__":
    import os
    print(dec_to_bin_remainder(int(os.getenv("NUMBER"))))
