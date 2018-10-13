#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "SA18225036 Min Chen"
__email__ = "mchen330@mail.ustc.edu.cn"

import math

def main():
    # Get the radiu
    r_str = input("Please input the radius of a sphere\n")

    # Check the legal input and caculate
    try:
        # Transfor input str to float
        r = float(r_str)
        # Check positive number
        if r >= 0:
            v = 4 / 3 * math.pi * math.pow(r, 3)
            a = 4 * math.pi * math.pow(r, 2)
            print("The valume is : ", v, "The surface is : ", a)
        else:
            print("Invalid Input! Please input a positive number")
            # If not legal input ,recall main
            main()
    except Exception as _:
        print("Invalid Input! Please input a float number")
        # If not legal input ,recall main
        main()


if __name__ == '__main__':
    main()
