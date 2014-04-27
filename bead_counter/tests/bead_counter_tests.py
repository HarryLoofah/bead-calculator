import unittest
from bead_counter.sanity_check import SanityCheck

class SanityCheckTests(unittest.TestCase): 
            
    def test_total_beads_is_an_int(self):
        pass
        
    def test_total_beads_is_more_than_twelve(self):
        sanity = SanityCheck
        result = sanity.less_than_12(14)
        self.assertTrue(result)
        
    def test_total_beads_is_divisible_by_six_and_nine(self):
        pass
