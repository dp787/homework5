import pytest
from calculator.calculator import Calculator

@pytest.mark.parametrize("num1, num2, expected", [
    (1, 2, 3),
    (4, 5, 9),
])
def test_add(num1, num2, expected):
    assert Calculator.add(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (5, 3, 2),
    (10, 4, 6),
])
def test_subtract(num1, num2, expected):
    assert Calculator.subtract(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (2, 3, 6),
    (7, 8, 56),
])
def test_multiply(num1, num2, expected):
    assert Calculator.multiply(num1, num2) == expected

@pytest.mark.parametrize("num1, num2, expected", [
    (6, 2, 3),
    (9, 3, 3),
])
def test_divide(num1, num2, expected):
    assert Calculator.divide(num1, num2) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator.divide(1, 0)

def test_display_menu(capsys):
    Calculator.display_menu()
    captured = capsys.readouterr()
    expected_output = (
        "Available Commands:\n"
        "add: Addition\n"
        "subtract: Subtraction\n"
        "multiply: Multiplication\n"
        "divide: Division\n"
        "menu: Display Menu\n"
    )
    assert captured.out == expected_output

if __name__ == "__main__":
    pytest.main()
