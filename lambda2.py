l = ['mon', 'Tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']


def change_words(words, func):
	for word in words:
		print(func(word))


sample_func = lambda word: word.lower()

change_words(l, sample_func)

