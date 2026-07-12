import unittest

from src.main.lab import question1, question2, question3


class TestStartLab(unittest.TestCase):

    def test_question1(self):
        expected = int(3.14159) // 1
        self.assertEqual(question1(), expected)

    def test_question2(self):
        expected = (2 ** 4) - 4
        self.assertEqual(question2(), expected)

    def test_question3(self):
        expected = "String"
        self.assertEqual(question3().strip().lower(), expected.lower())


if __name__ == "__main__":
    unittest.main()