"""
Make sure the number enter (total_beads) is either too small
to use or is not divisible by 6 or 9 before moving on.
"""
print('testing')
# If total_beads is less than 12, print error message
def less_than_12():
    if total_beads < 12:
        print('Error. Please use more than 12 beads.')
        return
        
# If total_beads is not divisible by 6 or 9, print error message
def not_divisible_by():
    if total_beads % 6 != 0 and total_beads % 9 != 0:
        print('Error. Please use a number that is divisible by 6 or 9')
        return