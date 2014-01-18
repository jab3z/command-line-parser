import StringIO
import unittest


from command_parser import ParserResult

class FakeFileWrapper:
	def __init__(self, text):
		self.text = text

	def open(self):
		return StringIO.StringIO(self.text).getvalue().split()


class TestParserResult(unittest.TestCase):

	def test_create_parser_result(self):
		fake_file = FakeFileWrapper ('Lorem ipsum dolor sit amet, consectetur adipisicing elit')
		parser_result = ParserResult(fake_file.open())

	def test_if_file_has_one_line(self):
		fake_file = FakeFileWrapper('Lorem ipsum dolor sit amet, consectetur adipisicing elit')
		parser_result = ParserResult(fake_file.open())
		self.assertEqual(['adipisicing ', 'amet ', 'consectetur ', 'dolor ', 'elit ', 'ipsum ', 'Lorem ', 'sit '], parser_result.sort_file())
		
	def test_if_return_list_sorted(self):
		pass


if __name__ == '__main__':
	unittest.main()