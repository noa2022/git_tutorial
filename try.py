class MameMameError(Exception):
	pass


l = [0, 1, 2, 3, 4, 5]

try:
	l[0]
	raise MameMameError()
except IndexError as ex:
	print("Don't worry: {}".format(ex))
except NameError as ex:
	print(ex)
except MameMameError as ex:
	print('Excuse me')
else:
	print('done')
finally:
	print('clean up')

