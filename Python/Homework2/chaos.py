#!/usr/bin/python
# -*- coding: utf-8 -*-
def calc_chaos(init_val_a, init_val_b, iterations):
    # open file and calc the chaos number
    with open("result_for_chaos.txt",'w') as f:
        f.write("index   " + str(init_val_a) + "    " + str(init_val_b) + "\n")
        f.write("---------------------" + "\n")
        for i in range(iterations):
            # calc the num
            init_val_a = 3.9 * init_val_a * (1 - init_val_a)
            init_val_b = 3.9 * init_val_b * (1 - init_val_b)
            # output the result in file
            f.write(str(i + 1) + "    " + str(init_val_a) + "    " + str(init_val_b) + "\n")
        f.close()

def main():
    # get interations number and check ,ensure the data type
    iterations = 0
    init_val_a = 0.0
    init_val_b = 0.0

    try:
        iterations = int(eval(input("Enter a number for iterations:  ")))
        init_val_a = float(eval(input("Enter a number for init_val_a:  ")))
        init_val_b = float(eval(input("Enter a number for init_val_b:  ")))
    except Exception as e:
        print("Please input valid number. Error is ",e)
        main()
    # call the function to caculate
    calc_chaos(init_val_a, init_val_b, iterations)

if __name__ == '__main__':
    main()