import argparse, sys, os

class ParserResult:
	"""docstring for ClassName"""
	

	def __init__(self, input_file, filename=None):
		self.filename = filename
		self._input_file = input_file 


	def output_file(self):
		'''
			str, list -> None
			
			Outputs a file with given content and the name given if
			the file does not exists, otherwise prints an error message.

		'''

		if os.path.exists(self.filename):
			sys.stdout.write('The file already exists, cannot be created!\n')
			return
		else:
			_output_file = file('{}'.format(self.filename), 'wt')
			[_output_file.write(i) for i in self.sort_file()]
			_output_file.close()


	def sort_file(self):
		'''
			file -> list

			Read the input file in a list and return the sorted version of it.
		'''
		with self._input_file as f:
			return sorted([line for line in f])


def main():

	parser = argparse.ArgumentParser(description='''Takes in
									as an argument the name of a file.''')
	parser.add_argument('sort', type=argparse.FileType('r'),
						help='''Output the lines from file 
						in sorted alphabetical order.''')
	parser.add_argument('-r', '--reversed', action='store_true', help='''Output the
						lines in reversed order.''')
	parser.add_argument('-o', '--output', type=str, help='''Output
						the result in a new file''')
	args = parser.parse_args()
	results = ParserResult(args.sort)

	if args.reversed:
		if args.output:
			results.filename = args.output
			results.output_file()
		else:
			[sys.stdout.write(item) for item in reversed(results.sort_file())]

	elif args.output:
		output_file(args.output, sorted_file_)

	else:
		[sys.stdout.write(item) for item in results.sort_file()]

if __name__ == '__main__':
	main()