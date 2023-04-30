import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_valid_adding(self):
        assert self.calc.adding(self, 2, 2)

    def test_valid_multiply(self):
        assert self.calc.multiply(self, 31, 520)

    def test_valid_division(self):
        assert self.calc.division(self,2, 0.5)

    def test_valid_subtraction(self):
        assert self.calc.subtraction(self, 20, 9)