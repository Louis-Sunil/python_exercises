""" Set : S04
    Excercise Number : S04Q02
    Description : Program to calculate the results of a student
                  by taking the marks scored by the student as an input.
"""

def do_action(sub_1,sub_2,sub_3):
    # Compare present with redmark and bluemark
    # to decide the appropriate action
    print (sub_1)
    print (sub_2)
    print (sub_3)
    if sub_1 >= 95 and sub_2 >= 95 and sub_3 >= 95:
        print("Congratulations\nyou have passed in First Class")
    elif sub_1 >= 75 and sub_2 >= 75 and sub_3 >= 75:
        print("Congratulations\nyou have passed in Second Class")
    elif sub_1 > 35 and sub_2 > 35 and sub_3 > 35:
        print("Congratulations\nyou have passed in Average")
    else:
        print("Fail")

def get_current_score():
    # Get value from user
    # Return integer
    maths_in = int(input("Enter the marks scored in Mathematics:"))
    science_in = int(input("Enter the marks scored in Science:"))
    english_in = int(input("Enter the marks scored in English:"))
    return maths_in, science_in, english_in

# Main starts from here
score = get_current_score()
maths = (score[0] / 100) * 100
science = (score[1] / 90) * 100
english = (score[2] / 80) * 100
do_action(maths, science, english)
