#!/usr/bin/env python
import sys
import string

# add stopwords (generic and from Shakespeare's time)
stopwords = set(['the', 'and', 'a', 'an', 'its', 'for', 'that', 'thee', 'thy', 'thou', 'thine'])

# create translator to replace punctuation with space
# https://stackoverflow.com/questions/34860982/replace-the-punctuation-with-whitespace/34922745
translator = string.maketrans(string.punctuation, ' '*len(string.punctuation))

# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip().lower()
    # use translator to remove punctuation
    line = line.translate(translator)

    # split the line into words; splits on any whitespace
    words = line.split()

    # output tuples (word, 1) in tab-delimited format
    for word in words:
	if word not in stopwords:
        	print '%s\t%s' % (word, "1")
