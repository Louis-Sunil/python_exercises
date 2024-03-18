''' S03Q01 program to check 2 digit and 3 digit numbers and perform operation
    based on the user input '''

def do_1digit_oper(number):
    if number in range(0,10):
        print(number + 7)

def do_2digit_oper(number):
    if number in range(10,100):
        print(number ** 5)

def do_3digit_oper(number):
    if number in range(100,1000):
        num = int(input("Enter any number:"))
        print(number + num)

def perform_check(number):
    do_1digit_oper(number)
    do_2digit_oper(number)
    do_3digit_oper(number)
    
def get_number():
    number = int(input("Enter any number:"))
    return number

# Main starts from here
num1 = get_number()
perform_check(num1)
