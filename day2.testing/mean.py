#!/usr/bin/python

import sys

x = []
for line in open(sys.argv[1]):
	if line.strip() == "":
		continue

	try:
		num = float(line)
		x.append(num)
	except ValueError:
		pass

print "average is", sum(x) /float(len(x))
