import unittest
from tests.home.login_tests import LoginTests
from tests.courses.register_courses_csv_data import RegisterCoursesTestsCSV

#get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(RegisterCoursesTestsCSV)

#create test suite combining all test classes

smokeTest = unittest.TestSuite([tc1, tc2])
unittest.TextTestRunner(verbosity=2).run(smokeTest)
