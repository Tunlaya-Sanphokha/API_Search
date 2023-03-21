import unittest
from NLP import *



class Unit_test(unittest.TestCase):
        def test_NLP(self):
            obj = NLP()
            obj.save_analysis('en','eversoul','2023-03-19','2023-03-21')
            self.assertIsNotNone(obj)
        
unittest.main()