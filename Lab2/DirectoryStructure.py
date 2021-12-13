import os.path


def print_with_tab(path, depth):
	print("\t" * depth + path)


def dir_structure(directory):
	depth = 0
	last_element_of_dir = directory.split("\\")[-1]
	print_with_tab(last_element_of_dir, depth)
	for element in os.listdir(directory):
		if not os.path.isdir(os.path.join(directory, element)):
			print_with_tab(element, depth + 1)
		else:
			dir_structure(os.path.join(directory, element), depth + 1)


if __name__ == '__main__':
	starting_directory = "../files"
	dir_structure(starting_directory)
