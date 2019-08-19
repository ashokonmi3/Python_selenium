import unittest
from Test_Suite import PythonOrgSearch
from Test_Suite2 import PythonOrgSearch1
 
# get all tests from SearchText and HomePageTest class
sanityTest = unittest.TestLoader().loadTestsFromTestCase(PythonOrgSearch)
loadTest = unittest.TestLoader().loadTestsFromTestCase(PythonOrgSearch1)
print (sanityTest)
print(type(sanityTest))
# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([sanityTest, loadTest])
 
# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)