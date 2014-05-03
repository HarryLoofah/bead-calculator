#!/usr/bin/env python

"""
Use this module to clean up the results of main.
For use when run as a script.
"""

from prettytable import PrettyTable
from prettytable import PLAIN_COLUMNS # Simplify the PrettyTable.
from main import ls_vals


pretty_table = PrettyTable(['Short Side', 'Long Side'])

for sides in list:
	pretty_table.add_row(sides)

pretty_table.set_style(PLAIN_COLUMNS)
print pretty_table
