import cPickle
from random import randint
count = 0
class  Trie(object):
	def __init__(self):
		self.letters = dict()
	def add(self, word):
		if len(word) == 0:
			self.letters["."] = None
			return 
		letter = word[0]
		if not letter in self.letters:
			self.letters[letter] = Trie()
		self.letters[letter].add(word[1:])	
	def phoneNumber(self, number, prefix=''):
		"""number is a string"""
		global count
		count+=1
		if len(number) == 0:
			if '.' in self.letters:
				return [prefix]
			else:
				return []

		digit = number[0]

		output = []
		#fix bd error, doesnt reach end of word
		if digit not in numberMap:
			if '.' in self.letters:
				output+=words.phoneNumber(number[1:],prefix+' ')
		else:
			options = numberMap[digit]
			for option in options:
				if option in self.letters:
					child = self.letters[option]
					output += child.phoneNumber(number[1:],prefix+option)
		return output

def makeTrie():
	f = open("/usr/share/dict/words")
	words = Trie()
	i = 0
	for line in f:
		if i==100000:
			break
		words.add(line.strip().lower())
		i+=1
	return words
def saveTrie():
	words = makeTrie()
	f = open("myPickle","w")
	f.write(cPickle.dumps(words))
	f.close()
def loadTrie():
	f = open("myPickle","r")
	words = cPickle.loads(f.read())
	f.close()
	return words
words = makeTrie()
numberMap = {
	'2' : 'abc',
	'3' : 'def',
	'4' : 'ghi',
	'5' : 'jkl',
	'6' : 'mno',
	'7' : 'pqrs',
	'8' : 'tuv',
	'9' : 'wxyz'
}
worst = 0
for i in range(1000):
	number = randint(10**6,10**7)
	worst+=3**len(str(number))
	words.phoneNumber(str(number))
print worst/1000
print count/1000