import math


def main():
    # Get the radiu
    r_str = input("Please input the radius of a sphere\n")
    # Check the legal input and caculate
    try:
        r = float(r_str)
        v = 4 / 3 * math.pi * math.pow(r, 3)
        a = 4 * math.pi * math.pow(r, 2)
        print("The valume is : ", v, "The surface is : ", a)
    except Exception as _:
        print("Please input a float number")
        main()


if __name__ == '__main__':
    main()
