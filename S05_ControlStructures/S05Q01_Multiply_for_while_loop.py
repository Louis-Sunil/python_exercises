'''S05Q01 Multiplication table for any number using for loop and while loop'''

#defining global variable.
mult_of = int(input("Which multiplication table do you want to excute ?"))

def multiply_for_loop():
    print("\nExecuting Multiplication tabe of", mult_of,"using for loop\n")
    count = range(1,11)
    for numbers in count:
        multiply = mult_of * numbers
        print (mult_of ,"*\t" ,numbers,"\t=",multiply)

def multiply_while_loop():
    print("\nExecuting Multiplication tabe of", mult_of,"using while loop\n")
    count = 1
    while count < 11:
        multiply = mult_of * count
        print (mult_of ,"*\t" ,count,"\t=",multiply)
        count += 1
        
#Main Starts here
multiply_for_loop()
multiply_while_loop()
