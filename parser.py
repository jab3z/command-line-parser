import argparse, sys, os

def output_file(filename, content):
	'''
		str, list -> None
		
		Outputs a file with given content and the name given if
		the file does not exists, otherwise prints an error message.

	'''

	if os.path.exists(filename):
		sys.stdout.write('The file already exists, cannot be created!\n')
		return
	else:
		output_file = file('{}'.format(filename), 'wt')
		[output_file.write(i) for i in content]
		output_file.close()


def sort_file(input_file):
	'''
		file -> list

		Read the input file in a list and return the sorted version of it.
	'''

	return sorted([line for line in input_file])


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

	with args.sort as f:
		sorted_file = sort_file(f)


	if args.reversed:
		if args.output:
			output_file(args.output, reversed(sorted_file))
		else:
			[sys.stdout.write(item) for item in reversed(sorted_file)]

	elif args.output:
		output_file(args.output, sorted_file)

	else:
		[sys.stdout.write(item) for item in sorted_file]

if __name__ == '__main__':
	main()