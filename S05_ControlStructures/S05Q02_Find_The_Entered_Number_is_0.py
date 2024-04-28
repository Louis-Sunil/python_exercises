'''S05Q02
    - Ask the user to enter a number till he enters 0. 
    - Print the maximum and minimum values among all entered numbers. 
    - Print the number of single, two and three digit numbers entered.'''

number = int(input("Enter any number:"))
single_digit = 0
two_digit = 0
three_digit = 0
lst = []

while number != 0:
    lst.append(number)
    number = int(input("Enter any number:"))
    if number in range(10,100):
        two_digit += 1
    elif number in range(100,1000):
        three_digit += 1
    else:
        single_digit += 1
else:
    lst.sort()
    print("Min number is", lst[0],"\nMax number is",lst[-1])
    print("There are",single_digit,"single digit numbers\n"
          "There are",two_digit,"double digit numbers\n"
          "There are",three_digit,"triple digit numbers\n")

    
