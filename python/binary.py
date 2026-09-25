"""
This file contains some algorithms to convert decimal numbers to binary.
One important note: the decimal numbers discussed here are positive integers.
"""

def dec_to_bin_remainder(dec: int):
    """
    This function takes in a positive integer and converts it to a string representation of a binary number.
    **Algorithm Description**
    As long as our number is greater than 0 we will do the following:
        - To the result (from right to left) we add the remainder of our number when devided by two.
        - We do an integer devide by 2 of our number, so without the remainder.
    """
    # make sure dec is a positive integer
    if dec < 0: raise ValueError("The decimal number must be a positive integer!")
    res = ""
    while dec > 0:
        res = str(dec % 2) + res 
        dec //= 2
    return f"0b{res}"

def bin_to_dec(bi: str):
    """
    This function takes in a string representation of a binary number and converts it to a positive integer.
    **Algorithm Description**
    """
    for n in range(len(bin) - 1, 0, -1):
        pass

# test some stuff
if __name__ == "__main__":
    import os
    print(dec_to_bin_remainder(int(os.getenv("NUMBER"))))
