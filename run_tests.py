import unittest
import json_tests
import sys, os

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromModule(json_tests)
    sys.stdout = open(os.devnull, 'w')
    unittest.TextTestRunner(verbosity=2).run(suite)
    sys.stdout = sys.__stdout__
