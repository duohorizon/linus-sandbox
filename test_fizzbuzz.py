import unittest

from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_n_1(self):
        self.assertEqual(fizzbuzz(1), ["1"])

    def test_n_3_contains_fizz(self):
        result = fizzbuzz(3)
        self.assertEqual(result, ["1", "2", "Fizz"])
        self.assertIn("Fizz", result)

    def test_n_5_contains_buzz(self):
        result = fizzbuzz(5)
        self.assertEqual(result, ["1", "2", "Fizz", "4", "Buzz"])
        self.assertIn("Buzz", result)

    def test_n_15_contains_fizzbuzz(self):
        result = fizzbuzz(15)
        self.assertEqual(len(result), 15)
        self.assertEqual(result[14], "FizzBuzz")
        self.assertIn("FizzBuzz", result)

    def test_fizzbuzz_only_on_multiples_of_15(self):
        result = fizzbuzz(30)
        indexes = [i + 1 for i, v in enumerate(result) if v == "FizzBuzz"]
        self.assertEqual(indexes, [15, 30])

    def test_zero_and_negative_return_empty(self):
        self.assertEqual(fizzbuzz(0), [])
        self.assertEqual(fizzbuzz(-7), [])


if __name__ == "__main__":
    unittest.main()
