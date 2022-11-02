import pytest

from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator()

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(2, 4) == 6

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(3, 4) == 12

    def test_division_calculate_correctly(self):
        assert self.calc.division(9, 3) == 3

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(7, 5) == 2

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def teardowm(self):
        print('Выполнение метода Teardown')