#!/usr/bin/python
# -*- coding: utf-8 -*-
def main():
    # Creat dict for pair of (grade and corresponding grade)
    grade_table = {
        '0': 'F',
        '1': 'F',
        '2': 'D',
        '3': 'C',
        '4': 'B',
        '5': 'A'
    }
    
    try:
        # Get input score
        corsp_grade = input("Please input a row score")
        # Check the legal input
        if len(corsp_grade) == 1 and corsp_grade >= '0' and corsp_grade <= '5' :
            # get the match grade in dict and output
            print("The corresponding grade is",grade_table[corsp_grade])
            main()
        else:
            print("Your input is invaild!")
            main()
    except Exception as e:
        print("There is somethin error",e)
        main()
    

if __name__ == '__main__':
    main()