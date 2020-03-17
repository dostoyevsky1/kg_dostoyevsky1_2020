
def one_to_one(s1: str, s2: str) -> bool:
	try:
		s1, s2 = s1.lower(), s2.lower()
		print(len(set(s1)) == len(set(s2)) == len(set(zip(s1,s2))))
	except Exception as e:
		print(f'Exception occurred {e}')
		raise

	return None
	