#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# prog1.py
#
# Author: Yobel Dolores
# License: MIT
#
# Finds the word that occurs the most times in a given text
#
# ## ###############################################################
import os
import re

def rank_words(wc):
	ranked_words = []
	for word in wc:
		ranked_words.append( (word, wc[word]) )
	ranked_words.sort(key=lambda tup : tup[1], reverse=True)
	return ranked_words



def count_words(filepath):
	wordcount = {}
	with open(filepath, "r") as f:
		line = f.readline()
		while line:
			words = re.split(r"\W+", line)
			for word in words:
				if not word:
					continue
				word = word.lower()
				if len(word) >= 4:
					if word in wordcount:
						wordcount[word] +=1
					else:
						wordcount[word] =1
			line = f.readline()
	return wordcount



def main():
	wordcount = count_words("quijote.txt")
	ranked = rank_words(wordcount)
	for i in range(3):
		print('Most used word #{}: "{}" ({})'
			.format(
				i+1,
				ranked[i][0],
				ranked[i][1]
			)
		)



if __name__ == '__main__':
	main()
