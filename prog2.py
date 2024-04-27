#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# prog1.py
#
# Author: Mauricio Matamoros
# License: MIT
#
# Finds the longest word in the input string
#
# ## ###############################################################
import sys

def find_longest_word(line):
	words = line.split(" ")
	longest = words[0]
	for word in words:
		if len(word) > len(longest):
			longest = word
	return longest

def main(argv):
	if len(argv) < 2:
		return
	line = " ".join(argv[1:])
	print("Line is:", line)
	longest = find_longest_word(line)
	print("Longest is:", longest)

if __name__ == '__main__':
	main(sys.argv)
