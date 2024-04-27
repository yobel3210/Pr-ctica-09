#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ## ###############################################################
# prog1.py
#
# Author: Mauricio Matamoros
# License: MIT
#
# Calculates the sine of each input number
#
# ## ###############################################################
import sys
from math import cos

def main(argv):
	for i in range(1, len(argv)):
		a = float(argv[i]) # The angle
		s = cos(a)         # The sine of the angle
		print("cos({}) = {}".format(a, s))

if __name__ == '__main__':
	main(sys.argv)
