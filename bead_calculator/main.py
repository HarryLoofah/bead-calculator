#!/usr/bin/env python

"""
bead-calculator
============

A simple Python script to help peyote stitch beadworkers to figure out
how many beads to use to start a new project.

BeadCalculator checks to make sure that the number of beads used in the project
will work mathematically and lets the beadworker know what design elements
will be possible for the number of starting beads entered.

##To Use:

1. Run the program.
2. Measure the object that you'll be beading by stringing beads and wrapping
thread around the object.
3. Enter the number of beads from the initial measurement around the object.
4. BeadCalculator tells you if that number of beads will work, and if it doesn't,
BeadCalculator suggests an alternative number or numbers to start with.

BeadCalculator also tells the beadworker how many bead to string, how many to add
(when the first two lines of beads are added to the project), and what long
and short side design elements will be available.
"""
# imports

__version__ = "0.1"

def sanity_check(beads):
    """
    Before running full code, check to see that the number entered
    (beads), is greater than 12 and that it is divisible by 6 or 9.
    """
    # If beads is less than 12, print error message and return.
    if beads < 12:
        print('Error. Please use more than 12 beads.')
        return
    # If beads is not divisible by 6 or 9, print error message and return
    if beads % 6 != 0 and beads % 9 != 0:
        print('Please pick a number that is divisible by 6 or 9')
        return 

def long_short_valuess(beads):
    """
    Returns short and long side of design elements depending on
    whether the number of beads entered in raw_input is mod 6, 9, or 12.
    
    If number of beads entered is not mod 6 or 9, find the higher and lower 
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
    
    if len(list) != 0 and beads >= 12:
        # If the list contains values, print (or return in finished code) sorted(list).
        print("You can use these short/long design elements:\n %s") % sorted(list)
        
        # Suggest starting bead number and number of beads to add.
        # These formulas are based on the specific 'three drop' peyote
        # stitch pattern used (as opposed to the simpler 'two drop.'
        suggested = beads 
        beads_to_add = suggested/3
        starting_number = beads_to_add*2
        print('Start with {0} beads then add {1}.' .format(str(starting_number), str(beads_to_add,)))
    
    if len(list) == 0:
        # If list contains no values, find next usable number higher than beads.
        higher_list = list
        higher_bead_number = beads
        
        while len(higher_list) == 0: 
            # Iterate, then check to see if the new number matches modulo criteria.
            higher_bead_number += 1
            higher_list = [v for k, v in d.items() if int(higher_bead_number) % k == 0]
            
            if len(higher_list) != 0:
                # Print a message with the suggested higher number and
                # a list of short and long values when a usable lower number found.
                print("Try %s beads instead." % higher_bead_number)
                print("Which gives you these design options:\n %s ") % sorted(higher_list)
                
    if len(list) == 0:
        # If list contains no values, find next usable number higher than beads.
        lower_list = list
        lower_bead_number = beads
        
        while len(lower_list) == 0 and lower_bead_number > 12:
            # Iterate, then check to see if the new number matches modulo criteria.
            lower_bead_number -= 1
            lower_list = [v for k, v in d.items() if int(lower_bead_number) % k == 0]
            
            if len(lower_list) != 0:
                # Print a message with the suggested higher number and
                # a list of long and short values when a usable lower number found. 
                print("Or, try %s beads." % lower_bead_number)
                print("Which gives you these design options:\n %s ") % sorted(lower_list)

    
if __name__ == "__main__":
    import sys
    # Force the user to input a valid integer.
    try:
        beads = int(raw_input("Please specify number of beads: "))
    except ValueError:
        print "Input was not an integer."
        try:
            beads = int(raw_input("Please specify number of beads: "))
        except ValueError:
            sys.exit()

    sanity_check(beads)
    long_short_valuess(beads)
    