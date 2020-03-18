

def one_to_one(s1: str, s2: str) -> None:
	

	if not isinstance(s1, str) or not isinstance(s2, str):
		raise TypeError('\n' + 'Input must be a string type' + '\n')

	if len(s1) != len(s2):
		raise ValueError('\n' + 'Inputs must be of equal length. No isomorphism by default' + '\n')

	try:
		s1, s2 = s1.lower(), s2.lower()
		print(len(set(s1)) == len(set(s2)) == len(set(zip(s1,s2))))
	except Exception as e:
		print(f'Exception occurred {e}')
		raise

	return None

