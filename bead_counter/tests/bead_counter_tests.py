import unittest
from bead_counter.main import SanityCheck

class SanityCheckTests(unittest.TestCase):
    def setUp(self):
        """
        setUp is called before every test
        """
        pass
    def tearDown(self):
        """
        tearDown is called at the end of every test
        """
        pass 
        
    def test_total_beads_is_more_than_twelve(self):
        """
        Tests to make sure raw input is greater than 12.
        """
        pass
        
    def test_total_beads_is_not_divisible_by_six_or_nine(self):
        """
        Tests to make sure raw input is divisible by 6 or 9
        """
        pass

if __name__ == '__main__':
    # run all TestCase's in this module
    unittest.main()
