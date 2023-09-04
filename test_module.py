import unittest # import the unittest module
from arithmetic_arranger import arithmetic_arranger # import the function to be tested


# the test case
class UnitTests(unittest.TestCase): # define a class that inherits from unittest.TestCase
    def test_arrangement(self): # define a method that tests the arrangement of the problems
        actual = arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]) # call the function with four problems and store the result in actual
        expected = "    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----" # define the expected output as a string
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]') # use the assertEqual method to compare the actual and expected outputs and provide a custom error message

        actual = arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]) # call the function with five problems and store the result in actual
        expected = "  11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------" # define the expected output as a string
        self.assertEqual(actual, expected, 'Expected different output when calling "arithmetic_arranger()" with ["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]') # use the assertEqual method to compare the actual and expected outputs and provide a custom error message

    def test_too_many_problems(self): # define a method that tests the error handling for too many problems
        actual = arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]) # call the function with six problems and store the result in actual
        expected = "Error: Too many problems." # define the expected output as a string
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with more than five problems to return "Error: Too many problems."') # use the assertEqual method to compare the actual and expected outputs and provide a custom error message

    def test_incorrect_operator(self): # define a method that tests the error handling for incorrect operator
        actual = arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]) # call the function with a problem that uses the "/" operator and store the result in actual
        expected = "Error: Operator must be '+' or '-'." # define the expected output as a string
        self.assertEqual(actual, expected, '''Expected calling "arithmetic_arranger()" with a problem that uses the "/" operator to return "Error: Operator must be '+' or '-'."''') # use the assertEqual method to compare the actual and expected outputs and provide a custom error message

    def test_too_many_digits(self): # define a method that tests the error handling for too many digits
        actual = arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]) # call the function with a problem that has a number over four digits long and store the result in actual
        expected = "Error: Numbers cannot be more than four digits." # define the expected output as a string
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with a problem that has a number over four digits long to return "Error: Numbers cannot be more than four digits."') # use the assertEqual method to compare the actual and expected outputs and provide a custom error message

    def test_only_digits(self): # define a method that tests the error handling for non-digit characters
        actual = arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]) # call the function with a problem that contains a letter character in the number and store the result in actual
        expected = "Error: Numbers must only contain digits." # define the expected output as a string
        self.assertEqual(actual, expected, 'Expected calling "arithmetic_arranger()" with a problem that contains a letter character in the number to return "Error: Numbers must only contain digits."') # use the assertEqual method to compare the actual and expected outputs and provide a custom error message

    def test_solutions(self): # define a method that tests the optional solutions argument
        actual = arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49"], True) # call the function with four problems and a second argument of True and store the result in actual
        expected = "   32         1      45      123\n- 698    - 3801    + 43    +  49\n-----    ------    ----    -----\n -666     -3800      88      172" # define the expected output as a string
        self.assertEqual(actual, expected, 'Expected solutions to be correctly displayed in output when calling "arithmetic_arranger()" with arithemetic problems and a second argument of `True`.') # use the assertEqual method to compare the actual and expected outputs and provide a custom error message

if __name__ == "__main__":
    unittest.main() # run the test case
