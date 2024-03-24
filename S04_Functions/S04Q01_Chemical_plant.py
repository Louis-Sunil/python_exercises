""" Exercise Number : S04Q01
    set : S04
    Description : Program to alert the user when the Ethanol tank is High or Low
                  and take necessary action based on the user input
"""

def do_action(present, redmark, bluemark):
    # Compare present with redmark and bluemark
    # to decide the appropriate action
    if present > redmark:
        print("Alert....High!!\nClose the Valve")
    elif present < bluemark:
         print("Alert....Low!!\nbuy more fluid")
    else:
        print("Normal..")

def get_current_level():
    # Get value from user
    # Return integer
    current_value = int(input("Enter the current value if Ethanol in the tank:"))
    return current_value

# Main starts from here
capacity = 900
high = (900 * 80) // 100
low = (900 * 20) // 100

level = get_current_level()
do_action(level, high, low)
