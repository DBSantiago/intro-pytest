import pytest

# Pytest classes and methods must start with Test or test


class TestExample:

    @classmethod
    def setup_class(cls):
        print("\n**********Setting up test environment.**********")

    @classmethod
    def teardown_class(cls):
        print("\n**********Tearing down test environment.**********")

    def setup_method(self):
        print("\n*****Setting up test.*****")
        self.num1 = 10
        self.num2 = 20

    def teardown_method(self):
        print("\n*****Tearing down test.*****")

    def test_sum_two_numbers(self):
        assert self.num1 + self.num2 == 30, "Sorry, the sum isn't correct."

    def test_subtract_two_numbers(self):
        assert self.num2 - self.num1 == 10, "Sorry, the subtraction isn't correct."


class TestExample2:

    def test_multiply_two_numbers(self):
        assert 10 * 2 == 20
