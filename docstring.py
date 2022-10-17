def example_func(param1, param2):
	"""Docstring example that describes overall explanation of its function

	Args:
		param1 (int): The first parameter
		param2 (str): The second parameter

	Returns:
		bool: The return value. True for success, False for otherwise
	
	"""

	print(param1)
	print(param2)
	return True

print(example_func.__doc__)

