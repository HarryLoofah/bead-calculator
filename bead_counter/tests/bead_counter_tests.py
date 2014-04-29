import unittest
from bead_counter.main import CheckBeadNum
from bead_counter.main import ProcessBeadNum

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
        
    def test_ls_vals_modulo_method_returns_correct_result(self):
        """
        Tests to make sure ls_vals returns modulo findsing
        """
        process = ProcessBeadNum()
        result = process.ls_vals(beads=12)
        self.assertTrue(result % 6 == 0)

if __name__ == '__main__':
    # run all TestCase's in this module
    unittest.main()
