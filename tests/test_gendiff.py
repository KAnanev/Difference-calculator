from unittest import TestCase
from gendiff.scripts.gendiff import generate_diff


class Test(TestCase):
    def setUp(self) -> None:
        self.data = open('tests/fixtures/answer.txt')
        self.exp = generate_diff(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json'
        )

    def tearDown(self) -> None:
        self.data.close()

    def test_generate_diff(self):
        self.assertIsInstance(self.exp, str)
        self.assertEqual(self.exp, self.data.read())
