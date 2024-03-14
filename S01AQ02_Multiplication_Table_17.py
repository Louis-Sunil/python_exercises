""" 
S01Q02 program for Mutiplication table 17
"""

def print_mtable():
    """ 
    This function is to execute multiplication table of 17
    """
    mul_of = 17
    count = 1
    while count <= 10:
        m_table = mul_of * count
        print(mul_of, " *", count,"\t=", m_table)
        count += 1

# Main starts from here
print_mtable()
