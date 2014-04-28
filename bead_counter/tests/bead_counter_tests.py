import unittest
from bead_counter import beads # throwing an error...4/27
from bead_counter.sanity_check import less_than_12

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
            
    def test_total_beads_is_not_an_int(self):
        """
        Tests to make sure raw input is a whole integer.
        """
        actual_bead_number = beads
        expected = ValueError
        self.assertEqual (actual_bead_number, expected)
        #self.assertRaises(ValueError)
        
    def test_total_beads_is_more_than_twelve(self):
        """
        Tests to make sure raw input is greater than 12.
        """
        sanity = less_than_12(14)
        self.assertTrue(sanity)
        
    def test_total_beads_is_not_divisible_by_six_or_nine(self):
        pass

if __name__ == '__main__':
    # run all TestCase's in this module
    unittest.main()
