import nltk
import os
import platform
import requests
import bs4
from nltk.corpus import wordnet
from googletrans import Translator

def wikiscrap(searchword):
	print(searchword)
	res = requests.get('http://en.wikipedia.org/wiki/' + ''.join(searchword))
	res.raise_for_status()
	wiki = bs4.BeautifulSoup(res.text, "html.parser")
	for i in wiki.select('p'):
		print(i.getText())

def translate():
	lang = input("Enter Language code: ")
	word = input("Enter your sentence: ")
	translator = Translator()
	translated = translator.translate(word, dest=lang)	
	print("Translation: ", translated.text)

def about_word():
	synonyms = []
	antonyms = []
	word = input("Enter your word to get more info on it: ")
	
	for syn in wordnet.synsets(word):
		for l in syn.lemmas():
			synonyms.append(l.name())
			if l.antonyms():
				antonyms.append(l.antonyms()[0].name())

				
	print("\n")
	d = syn.definition()
	print("DEFINITION: ",d.capitalize())
	
	print("\n")
	expressions = syn.examples()
	print("EXPRESSIONS: ")
	c = 1
	for x in expressions:
		print("   ",c,"."," ",x.capitalize(),sep='')
		c+= 1
	
	print("\n")
	c = 1
	print("SYNONYMS: ")
	for x in set(synonyms):
		x = x.replace('_',' ')
		print("   ",c,"."," ",x.capitalize(),sep='')
		c+= 1
		
	print("\n")
	c = 1
	print("ANTONYMS: ")
	if len(antonyms)!= 0:
		for x in set(antonyms):
			print("   ",c,"."," ",x.capitalize(),sep='')
			c+= 1
	else:
		print("   ","Sorry, I couldn't find any antonyms for",word)

def comp_words():
	word1 = input("Enter first word: ")
	word2 = input("Enter second word: ")
	w1 = wordnet.synset('%s.n.01' % word1)
	w2 = wordnet.synset('%s.n.01' % word2)
	print(w1.path_similarity(w2))

q = False
while (q != True):
	s = input(" > ")
	s = s.lower()
	s = s.strip()
	if (s[ :7] == "search "):
		searchword = s[7: ]
		wikiscrap(searchword)
	elif (s == "translate" or s == "t"):
		translate()
	
	elif (s == "dictionary" or s == "d"):
		about_word()

	elif (s == "compare" or s == "c"):
		comp_words()

	elif (s == "exit" or s == "quit"):
		os._exit(0)
	
	elif s == "clear":
		if platform.system() == "Windows":
			os.system('cls')
		elif platform.system() == "Linux":
			os.system('clear')
		else:
			os.system('clear')
	
	else:
		continue

	print("\n")
