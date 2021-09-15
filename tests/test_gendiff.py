from unittest import TestCase
from gendiff.scripts.gendiff import generate_diff


class Test(TestCase):
    def setUp(self) -> None:
        self.open_file = open('tests/fixtures/answer.txt')
        self.data = self.open_file.read()
        self.exp_json = generate_diff(
            'tests/fixtures/file1.json',
            'tests/fixtures/file2.json'
        )
        self.exp_yaml = generate_diff(
            'tests/fixtures/file1.yaml',
            'tests/fixtures/file2.yaml'
        )

    def tearDown(self) -> None:
        self.open_file.close()

    def test_generate_diff(self):
        self.assertIsInstance(self.exp_json, str)
        self.assertEqual(self.exp_json, self.data)
        self.assertIsInstance(self.exp_yaml, str)
        self.assertEqual(self.exp_yaml, self.data)
