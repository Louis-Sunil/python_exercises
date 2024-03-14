""" 
    S01AQ03 : Program for multiplication of any number
"""

def get_number():
    """ 
        This function should fetch a number from user
        Input : None
        Return : an integer
    """
    number = input("Which multiplication table do you want to execute ?")
    # Check out your code behaviour by commenting the line below
    number = int(number)
    # What happens if you dont perform this operation ?
    #It acts as a string if not converted to intiger
    return number


def print_mtable(num):
    """ 
        This function prints the multiplication table of num
        Input : an integer
        Output : Display multiplication table of input integer
        Return : None
    """
    # Your solution code goes in here
    count = 1
    while count < 11:
        multiply = num * count
        print(num, " * ", count, " \t=", multiply)
        count += 1

def main():
    '''
        Main program
    '''
    inp = get_number()
    print_mtable(inp)

# Main starts from here
main()
