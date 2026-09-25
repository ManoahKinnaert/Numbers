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
    return f"0b{res}" if res != "" else "0b0"

def bin_to_dec(bi: str):
    """
    This function takes in a string representation of a binary number and converts it to a positive integer.
    **Algorithm Description**
    We loop from right to left and multiply the bit with a power of two (that increases as we move from right to left).
    """
    bi = bi.split("0b")[1]  # remove binary identifier
    result = 0
    for n in range(len(bi) - 1, -1, -1):
        result += int(bi[n]) *  2 ** (len(bi) - 1 - n)
    return result

# test this
if __name__ == "__main__":
    import os
    result = dec_to_bin_remainder(int(os.getenv("NUMBER")))
    print(result)
    print(bin_to_dec(result))
