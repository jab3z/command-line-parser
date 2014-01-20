import StringIO
import unittest


from command_parser import ParserResult

class FakeFileWrapper:

	"""File like object."""

	def __init__(self, text):
		self.text = text


	def open(self):
		return StringIO.StringIO(self.text).getvalue().split()


class TestParserResult(unittest.TestCase):


	# def setUp(self):
		# self.parser_result = ParserResult()


	def test_create_parser_result(self):
		fake_file = FakeFileWrapper ('Lorem ipsum dolor sit amet, consectetur adipisicing elit')
		parser_result = ParserResult(input_file=fake_file.open())


	def test_sort_file_with_one_line(self):
		fake_file = FakeFileWrapper('One two, three, for, eleven')
		parser_result = ParserResult(fake_file.open())
		self.assertEqual(['eleven ', 'for ', 'One ', 'three ', 'two '], parser_result.sort_file())


	def test_sort_file_with_two_lines(self):
		fake_file = FakeFileWrapper('One two, three, for,\n eleven, five, ana')
		parser_result = ParserResult(fake_file.open())
		self.assertEqual(['ana ', 'eleven ', 'five ', 'for ',  'One ', 'three ', 'two ' ], parser_result.sort_file())


	@unittest.skip('WIP')		
	def test_if_return_list_sorted(self):
		pass


if __name__ == '__main__':
	unittest.main()
