#!/usr/bin/python3

"""
This module aims to solve the RSA refactoring challenge
"""

import sys
import ctypes

path = "./lib_my_c_lib.so"    # set library path
lib = ctypes.CDLL(path)		  # init library

# set argtype to avoid overflow
lib.smallest_divisor.argtypes = [ctypes.c_long]


def main():
    """driver program"""
    with open(sys.argv[1], 'r') as line:
        num = line.readline()
        while num != '':
            num_int = int(num)
            # divisor = get_smallest_div(num_int)
            divisor = lib.smallest_divisor(num_int)
            print("{}={}*{}".format(num_int, num_int // divisor, divisor))
            num = line.readline()


def get_smallest_div(num: int) -> int:
    """ return the smallest divisor of a number"""
    if num % 2 == 0:
        return 2

    _fac = 3
    while (_fac * _fac <= num):
        if num % _fac == 0:
            return _fac
        else:
            _fac += 2

    return 1    # num is prime


main()
