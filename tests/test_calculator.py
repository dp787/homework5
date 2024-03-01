import pytest
from calculator.calculator import Calculator
import multiprocessing

# Define your test functions as usual

def test_add(num1, num2, expected):
    assert Calculator.add(num1, num2) == expected

def test_subtract(num1, num2, expected):
    assert Calculator.subtract(num1, num2) == expected

# ... other test functions ...

# Define a wrapper function to run tests in parallel
def run_tests(test_function, test_parameters):
    results = []
    for params in test_parameters:
        result = test_function(*params)
        results.append(result)
    return results

# Define a function to run tests using multiprocessing
def run_tests_parallel(test_function, test_parameters):
    with multiprocessing.Pool() as pool:
        results = pool.starmap(run_tests, [(test_function, test_parameters)])
    return results

# Specify the test parameters
test_params_add = [(1, 2, 3), (4, 5, 9), (-1, -2, -3)]
test_params_subtract = [(5, 3, 2), (10, 4, 6), (-5, -3, -2)]

# Run tests in parallel
def test_parallel_execution():
    results_add = run_tests_parallel(test_add, test_params_add)
    results_subtract = run_tests_parallel(test_subtract, test_params_subtract)

    # Print or handle the results as needed
    print("Results for addition:", results_add)
    print("Results for subtraction:", results_subtract)

# Ensure this block is executed when the script is run directly
if __name__ == "__main__":
    test_parallel_execution()

