import io
import unittest

from command_parser import ParserResult

class FakeFileWrapper:
	"""docstring for FakeFileWrapper"""
	def __init__(self, text):
		self.text = text

	def open(self):
		return io.StringIO(self.text)


class TestParserResult(unittest.TestCase):

	def test_if_file_has_one_line():
		pass
		
	def test_if_return_list_sorted():
		pass
