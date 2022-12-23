#!/usr/bin/python3

"""
This module aims to solve the RSA refactoring challenge
"""

import sys
import ctypes

path = "./liball.so"    # set library path
lib = ctypes.CDLL(path)		  # init library

# set argtype to avoid overflow
lib.smallest_divisor.argtypes = [ctypes.c_ulonglong]


def main():
    """driver program"""
    if len(sys.argv) != 2:
        return

    try:
        with open(sys.argv[1], 'r') as line:
            num = line.readline()
            while num != '':
                num_int = int(num)
                divisor = lib.smallest_divisor(num_int)
                print("{}={}*{}".format(num_int, num_int // divisor, divisor))
                num = line.readline()
    except FileNotFoundError:
        return


main()
