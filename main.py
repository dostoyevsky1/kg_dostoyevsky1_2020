from one_to_one import one_to_one
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('s1')
parser.add_argument('s2')
parser.add_argument('-w','--whitespace', action = 'store_false')


if __name__ == '__main__':
	args = parser.parse_args()

	try:
		one_to_one(args.s1, args.s2, args.whitespace)
	except Exception as e:
		print(f'Exception occurred {e}')
		raise
		

	
