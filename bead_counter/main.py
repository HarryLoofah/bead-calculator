#!/usr/bin/env python

            
if __name__ == "__main__":
    import sanity_check
    beads = raw_input("Please specify number of beads: ")
    sanity_check.less_than_12(int(beads))
    sanity_check.not_divisible_by(int(beads))

