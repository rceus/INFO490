import nltk
from nltk.util import ngrams
string = "I really like python, it's pretty awesome."
string_bigrams = ngrams(string.split(), 2)
for grams in string_bigrams:
	print grams