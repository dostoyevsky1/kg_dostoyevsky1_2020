from sys import argv
from one_to_one import one_to_one


if __name__ == '__main__':
	try:
		s1 = argv[1]
		s2 = argv[2]
		one_to_one(s1,s2)
	except IndexError:
		print('\n' + 'Input must consist of 2 elements' + '\n')
	except Exception as e:
		print(e)
		

	
