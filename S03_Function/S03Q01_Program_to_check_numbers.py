''' S03Q01 program to check 2 digit and 3 digit numbers '''

def perform_check(number):
    """ This function uses helper functions
        check_if_2digit
        check_if_3digit
        to perform the required operations
    """
    # Your solution code goes here
    # Invoke check_if_2digit and
    # check_if_3digit to check if the number
    # matches the criteria and print accordingly
    if number in range(10,100):
        print(number,"is a 2 digit number")
    elif number in range(100,1000):
        print(number,"is a 3 digit number")
    else:
        print("your entered number is:",number)

def get_number():
    number = int(input("Enter any number:"))
    return number

# Main starts from here
num1 = get_number()
num2 = get_number()
perform_check(num1)
perform_check(num2)
