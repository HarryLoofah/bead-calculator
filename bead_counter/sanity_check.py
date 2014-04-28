
"""
Before continuing through code, run a series of tests that check 
to see that the number entered (total_beads) is greater than 12 
and is divisible by 6 or 9.
"""
# Make sure the number entered is an integer
def is_an_int(total_beads):
    pass
# If total_beads is less than 12, print error message and return
def less_than_12(total_beads):
    if total_beads < 12:
        print('Error. Please use more than 12 beads.')
        return
        
# If total_beads is not divisible by 6 or 9, print error message and return
def not_divisible_by(total_beads):
    if total_beads % 6 != 0 and total_beads % 9 != 0:
        print('Error. Please use a number that is divisible by 6 or 9')
        return