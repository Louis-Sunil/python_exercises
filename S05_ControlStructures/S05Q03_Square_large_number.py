#Module     : Control Structures - Part1
#Exercise No: S05Q03
''' Take a number as input from the user. 
    Print all the squares of numbers from 1 to any large number. 
    The numbers printed should be less than 
    the number given as input by the user'''

def usr_input():
    number = int(input("give any number as an input:"))
    return number

def square(num):
    for numbers in range(1,100):
        square = numbers * numbers
        if square < num:
            print("Square numbers below",num,"are",square)

            
#Main starts here
number = usr_input()
square(number)
