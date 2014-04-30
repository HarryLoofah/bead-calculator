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

class CheckBeadNum(object):
    """
    Before running full code, check to see that the number entered 
    (total_beads), is greater than 12 and is divisible by 6 or 9.
    """
    # If total_beads is less than 12, print error message and return
    def less_than_12(self, total_beads):
        self.total_beads = total_beads
        # through in the following commented out code for testing (failed)
        #is_less_than_12 = False
        if total_beads < 12:
            #is_less_than_12 = True
            print('Error. Please use more than 12 beads.')
            return
            
    # If total_beads is not divisible by 6 or 9, print error message and return
    def not_divisible_by(self, total_beads):
        self.total_beads = total_beads
        if total_beads % 6 != 0 and total_beads % 9 != 0:
            print('Error. Please use a number that is divisible by 6 or 9')
            return
            
class ProcessBeadNum(object):
    """
    Returns long and short design element values, number of beads to start with
    and number of beads to add on the first row of beads, and if the raw_input
    bead number entered doesn't pass tests (if it is'nt mod 6, 9, or 12), then
    ProcessBeadNum suggests a number of total beads to try instead.
    
    Suggestion is based on which option (either higher bead count or lower) 
    gives the largest number of design element options. Both high and low
    suggestions are returned if design element options are equal.
    """
    # Returns long and short side of design elements available depending on
    # whether the number of beads entered in raw_input is mod 6, 9, 0r 12.
    def ls_vals(self, total_beads):
        return total_beads % 6 == 0
    

if __name__ == "__main__":
    beads = raw_input("Please specify number of beads: ").isdigit()
    bead_count = CheckBeadNum()
    bead_count.less_than_12(beads)
    bead_count.not_divisible_by(beads)
    

