#!/usr/bin/env python

"""
bead-calculator
============

A simple Python script to help peyote stitch beadworkers start their projects.
BeadCalculator checks to make sure the number of beads used in a project will
work out mathematically and lets the beadworker know what design elements
will be possible for the number of starting beads entered.

##To Use:

1. Measure the object that you'll be beading by stringing beads and wrapping
thread around the object.
2. Enter the number of beads from the initial measurement around the object.
3. BeadCalculator tells you if that number of beads will work, and if it doesn't,
BeadCalculator suggests an alternative number or numbers to start with.

BeadCalculator also tells the beadworker how many beads to string, how many to add
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
        print 'Error. Please use more than 12 beads.'
        return
    # If beads is not divisible by 6 or 9, print error message and return
    if beads % 6 != 0 and beads % 9 != 0:
        print 'Please pick a number that is divisible by 6 or 9'
        return
def long_short_values(beads):
    """
    Returns short and long side of design elements depending on
    whether the number of beads entered in raw_input is mod 6, 9, or 12.
    If number of beads entered is not mod 6 or 9, find the higher and
    lower values that match the above criteria and suggest those numbers to
    the user. Also show the new list values so that the user can see which
    option woulo offer more design choices.
    """
    check_list = {
        6: (3, 5),
        9: (4, 7),
        12: (5, 9)
        }
    pass_list = [v for k, v in check_list.iteritems() if int(beads) % k == 0]
    if len(pass_list) != 0 and beads >= 12:
        # If the list contains values, print sorted(pass_list).
        print "You can use these short/long design elements:\n {0}" \
        .format(sorted(pass_list))
        # Suggest starting bead number and number of beads to add.
        # These formulas are based on the specific 'three drop' peyote
        # stitch pattern used (as opposed to the simpler 'two drop.'
        suggested = beads
        beads_to_add = suggested/3
        starting_number = beads_to_add*2
        print 'Start with {0} beads then add {1}.' \
        .format(str(starting_number), str(beads_to_add,))
    if len(pass_list) == 0:
        # If list contains no values, find next usable number higher than beads.
        higher_list = pass_list
        high_bead = beads
        while len(higher_list) == 0:
            # Iterate, then check that the new number matches modulo criteria.
            high_bead += 1
            higher_list = \
            [v for k, v in check_list.iteritems() if int(high_bead) % k == 0]
            if len(higher_list) != 0 and beads >= 12:
                # Print a message with the suggested higher number
                # and a list of short and long values when a usable
                # lower number is found.
                print "Try %s beads instead" % high_bead
                print "Which gives you these design options:\n {0} " \
                .format(sorted(higher_list))
    if len(pass_list) == 0:
        # If list contains no values, find next usable number lower than beads.
        lower_list = pass_list
        low_bead = beads
        # Added >12 in line below to avoid low numbers.
        while len(lower_list) == 0 and low_bead > 12:
            # Iterate, then check if the new number matches modulo criteria.
            low_bead -= 1
            lower_list = \
            [v for k, v in check_list.iteritems() if int(low_bead) % k == 0]
            if len(lower_list) != 0:
                # Print a message with the suggested lower number
                # and a list of long and short values when a usable
                # lower number is found.
                print "Or, try {0} beads." .format(low_bead)
                print "Which gives you these design options:\n {0} " \
                .format(sorted(lower_list))

if __name__ == "__main__":
    import sys
    # Force the user to input a valid integer.
    try:
        BEAD_INPUT = int(raw_input("Please specify number of beads: "))
    except ValueError:
        print "Input was not an integer."
        try:
            BEAD_INPUT = int(raw_input("Please specify number of beads: "))
        except ValueError:
            sys.exit()

    sanity_check(BEAD_INPUT)
    long_short_values(BEAD_INPUT)
