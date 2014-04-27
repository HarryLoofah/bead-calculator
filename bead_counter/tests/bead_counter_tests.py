import unittest
import bead_counter.sanity_check

class SanityCheckTests(unittest.TestCase): 
            
    def test_total_beads_is_an_int(self):
        calc = Calculator()
        result = calc.add(2,2)
        self.assertEqual(4, result)
        
    def test_total_beads_is_more_than_twelve(self):
        pass
        
    def test_total_beads_is_divisible_by_six_and_nine(self):
        pass
