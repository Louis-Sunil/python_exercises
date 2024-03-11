'''Modify program in S01Q02 to print the multiplication table 
           of any number desired by the user'''

multiply_of = int(input("Which multiplicatin table do you want to execute?"))
count = 1

while count < 11:
    multiply_output = multiply_of * count
    print(multiply_of,"*",count,"=",multiply_output)
    count += 1
