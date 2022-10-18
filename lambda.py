l = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'sat', 'sun']


def change_words(words, func):
	for word in words:
		print(func(word))


change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())

