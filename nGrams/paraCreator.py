#!/usr/bin/python
def createCipher(input):
	dict = {
	'a':'o',
	'b':'g',
	'c':'h',
	'd':'v',
	'e':'w',
	'f':'i',
	'g':'n',
	'h':'x',
	'i':'d',
	'j':'t',
	'k':'j',
	'l':'p',
	'm':'y',
	'n':'a',
	'o':'u',
	'p':'z',
	'q':'e',
	'r':'m',
	's':'k',
	't':'b',
	'u':'s',
	'v':'f',
	'w':'r',
	'x':'l',
	'y':'c',
	'z':'q'
	}
	answer = ""
	for letter in input:
		if dict.has_key(letter):
			#print(letter)
			#print(dict[letter])
			answer+=dict[letter]
		else:
			print(letter)
	print(input)		#normal text	
	print(answer)		#cipher based on letter frequency
createCipher("thecodeistheanswer")