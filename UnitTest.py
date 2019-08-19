# import unittest
# from time import sleep
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys

# class PythonOrgSearch(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()

#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.python.org")
#         self.assertIn("Python", driver.title)
#         # assert "Python1" in driver.title
#         assert "Python" in driver.title

#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." in driver.page_source
#         sleep(10)

#     def test_search_in_python_org1(self):
#         driver = self.driver
#         driver.get("http://www.python.org")
#         self.assertIn("Python", driver.title)
#         assert "Python" in driver.title
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("python")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source

#     def tear_down(self):
#         self.driver.quit()

# class PythonOrgSearch1(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
    
#     def test_search_in_python_org(self):
#         driver = self.driver
#         driver.get("http://www.python.org")
#         #self.assertIn("Python", driver.title)
#         assert "Python" in driver.title
#         elem = driver.find_element_by_name("q")
#         elem.send_keys("pycon")
#         elem.send_keys(Keys.RETURN)
#         assert "No results found." not in driver.page_source
    
#     def tear_down(self):
#         self.driver.close()


# if __name__ == "__main__":
#     unittest.main()
#     
# #     
# import unittest
# class suiteTest(unittest.TestCase):
#    a = 50
#    b = 40
   
#    def testadd(self):
#       """Add"""
#       result = self.a+self.b
#       print("add test case")
#       self.assertEqual(result,100)

#    @unittest.skipIf(a>b, "Skip over this routine")
#    def testsub(self):
#       """sub"""
#       print("sub test case")

#       result = self.a-self.b
#       self.assertTrue(result == -10)
  
#    @unittest.skipUnless(b == 0, "Skip over this routine")
#    def testdiv(self):
#       """div"""
#       result = self.a/self.b
#       print("div test case")

#       self.assertTrue(result == 1)

#    @unittest.expectedFailure
#    
#    
#    
#    
#    
#    def testmul(self):
#       """mul"""
#       result = self.a*self.b
#       print("mul test case")

#       self.assertEqual(result == 0)

# if __name__ == "__main__":
#     unittest.main()


import unittest
# class SomeTest(unittest.TestCase):
#     def setUp(self):
# #         super(SomeTest, self).setUp()
#         self.mock_data = [1,2,3,4,5]
#     def test(self):
#         print("mock test")
#         self.assertEqual(len(self.mock_data), 5)
#     def tearDown(self):
# #         super(SomeTest, self).tearDown()
#         self.mock_data = []
# if __name__ == "__main__":
#     unittest.main()



def division_function(dividend, divisor):
    return dividend / divisor

class MyTestCase(unittest.TestCase):
    def test_using_context_manager(self):
        with self.assertRaises(ZeroDivisionError):
            x = division_function(1, 0)
if __name__ == '__main__':
    unittest.main()


