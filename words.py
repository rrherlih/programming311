#!/usr/bin/env python3

import sys

def word_max(word):
	if len(word) == 1:
		return word[0]
	elif len(word) == 2:
		if (word[0] >= word[1]):
			return word[0]
		else:
			return word[1]
	else:
		maxs = ""
		for i in range(0, len(word)//2 + 1):
			if word[i] >= word[len(word) - 1 - i]:
				maxs = maxs + word[i]
			else:
				maxs = maxs + word[len(word) - 1 - i]
		return(word_max(maxs))

def word_min(word):
	if len(word) == 1:
		return word[0]
	elif len(word) == 2:
		if (word[0] <= word[1]):
			return word[0]
		else:
			return word[1]
	else:
		mins = ""
		for i in range(0, len(word)//2 + 1):
			if word[i] <= word[len(word) - 1 - i]:
				mins = mins + word[i]
			else:
				mins = mins + word[len(word) - 1 - i]
		return(word_min(mins))

def main():
	w = sys.argv[1]
	print(word_min(w))

if __name__ == '__main__':
    main()
