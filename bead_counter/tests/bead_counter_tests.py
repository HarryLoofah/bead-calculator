import unittest
from bead_counter.main import CheckBeadNum
from bead_counter.main import ComputeBeadNum

class SanityCheckTests(unittest.TestCase):
    def setUp(self):
        """
        setUp is called before every test
        """
        
    def tearDown(self):
        """
        tearDown is called at the end of every test
        """
        
    def test_ls_vals_modulo_method_returns_correct_result(self):
        """
        Tests to make sure ls_vals returns modulo findsing
        """
        compute_num = ComputeBeadNum()
        result = compute_num.ls_vals(12)
        self.assertEquals(result, 0)

if __name__ == '__main__':
    # run all TestCase's in this module
    unittest.main()
