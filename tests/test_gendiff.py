from unittest import TestCase
from gendiff.scripts.gendiff import generate_diff


class Test(TestCase):
    def setUp(self) -> None:
        self.data = '''{
 - follow: False
   host: hexlet.io
 - proxy: 123.234.53.22
 - timeout: 50
 + timeout: 20
 + verbose: True
}'''
        self.exp = generate_diff('fixtures/file1.json', 'fixtures/file2.json')

    def test_generate_diff(self):
        self.assertIsInstance(self.exp, str)
        self.assertEqual(self.exp, self.data)
