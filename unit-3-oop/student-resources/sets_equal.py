def set_equality(set1, set2):
	if len(set1) != len(set2):
		return False
	else:
		for item in set1:
			if item not in set:
				return False
	return True
