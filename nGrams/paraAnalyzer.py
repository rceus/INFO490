def analyze(input):
	dict = {'a':'0'}
	for letter in input:
		letter = letter.lower()
		if dict.has_key(letter):
			number = dict[letter]
			dict[letter]=number+1
		else:
			dict[letter]=1
analyze("hello")