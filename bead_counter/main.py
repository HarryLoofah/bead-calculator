#!/usr/bin/env python

"""
bead-counter
============

A simple Python script to help peyote stitch beadworkers to figure out
how many beads to use to start a new project.

BeadCounter checks to make sure that the number of beads used in the project
will work mathematically and lets the beadworker know what design elements
will be possible for the number of starting beads entered.

##To Use:

1. Run the program.
2. Measure the object that you'll be beading by stringing beads and wrapping
thread around the object.
3. Enter the number of beads from the initial measurement around the object.
4. BeadCounter tells you if that number of beads will work, and if it doesn't,
BeadCounter suggests an alternative number or numbers to start with.

BeadCounter also tells the beadworker how many bead to string, how many to add
(when the first two lines of beads are added to the project), and what long
and short side design elements will be available.
"""

# imports


__version__ = "0.0.1"


def less_than_12(beads):
    """
    Before running full code, check to see that the number entered
    (total_beads), is greater than 12 and is divisible by 6 or 9.
    """
    # If total_beads is less than 12, print error message and return
    if beads < 12:
        print('Error. Please use more than 12 beads.')
        return
# If total_beads is not divisible by 6 or 9, print error message and return
def not_divisible_by(beads):
    if beads % 6 != 0 and beads % 9 != 0:
        print('Please pick a number that is divisible by 6 or 9')
        return beads

def long_short_valuess(beads):
    """
    Returns long and short side of design elements available depending on
    whether the number of beads entered in raw_input is mod 6, 9, or 12.
    
    If number of beads entered is not mod 6, 9, or 12, find a values higher and lower 
    values that match the above criteria and suggest those numbers to the user.
        
    Also show the new list values so that the user can see which option would offer
    more design choices.
    """
    d = {
        6: (3,5), 
        9: (4,7), 
        12: (5,9)
        }
    list = [v for k, v in d.items() if int(beads) % k == 0]
    # return list

    # If length of list is not 0, print sorted(list).
    if len(list) != 0:
        print sorted(list)
    
    # If list contains no values, find next usable bead numbers.
    if len(list) == 0:
        print('Nothing here...') # testing
        higher_list = list
        print higher_list # testing
        
        next_higher_bead_number = beads
        
        while len(higher_list) == 0: 
            print('Still nothing here...') # testing
           
            # Check to see if the new number matches modulo criteria.
            higher_list = [v for k, v in d.items() if int(next_higher_bead_number) % k == 0]
            next_higher_bead_number += 1
            print beads # testing
            print next_higher_bead_number
            print higher_list  # testing
            #return higher_list
#            print higher_list
#            print("Try %s beads instead." % next_higher_bead_number)
#            print sorted(higher_list) 

    # Find next usable next_lower bead number
#    lower_list = list
#    if len(lower_list) == 0:
#        next_lower = beads
#        next_lower -= 1
#        lower_list = [v for k, v in d.items() if int(next_lower) % k == 0]
#        print("Try %s beads instead." % next_lower)
#        print sorted(lower_list)
    
if __name__ == "__main__":
    beads = int(raw_input("Please specify number of beads: "))
    less_than_12(beads)
    not_divisible_by(beads)
    long_short_valuess(beads)
    # high_low_values(beads)
