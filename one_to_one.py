def one_to_one(s1: str, s2: str, whitespace_free: bool = True) -> bool:
	"""
	Check for one-to-one character mapping(isomorphism) between two strings.

	Parameters:
		s1 (str): non-empty string [arg1]
		s2 (str): non-empty string [arg2]
		whitespace_free (bool): True or False flag to process whitespace as characters [-w , --whitespace]

	Returns:
		bool: True if one-to-one mapping is present, False otherwise.
	"""

	if not isinstance(s1, str) or not isinstance(s2, str):
		raise TypeError('\n' + 'Input must be a string type' + '\n')
	if len(s1) == 0 or len(s2) == 0:
		raise ValueError('\n' + 'Inputs cannot be empty strings. No isomorphism by default' + '\n')

	if whitespace_free:
		if any([char.isspace() for char in s1+s2]):
			raise ValueError('\n' + 'Inputs must be whitespace-free strings. No isomorphism by default' + '\n')

	if (len(s1) != len(s2)):
		raise ValueError('\n' + 'Inputs must be of equal length. No isomorphism by default' + '\n')

	try:
		s1, s2 = s1.lower(), s2.lower()
		is_isomorphic = len(set(s1)) == len(set(s2)) == len(set(zip(s1,s2)))
		print(is_isomorphic)
	except Exception as e:
		print(f'Exception occurred {e}')
		raise

	return is_isomorphic

