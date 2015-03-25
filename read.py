#!/usr/bin/env python3

""" Ryan Herlihy
	CS311 Spring 2015
	Anagrams
"""

import sys
import words

""" Opens dictionary file.
"""
def open_file(filename):
	try:
		return(open(filename))
	except:
		print("Error opening file.")
		sys.exit()

""" Takes a string and returns an array of its characters.
"""
def str_to_arr(word):
	a = []
	for c in word:
		if c >= 'a' and c <= 'z':
			a.append(c)
	return a


""" This function takes an array of characters and creates an array of numbers. Each number
	represents a specific character.
"""
def str_array_to_nums(s_arr):
	n = []
	for i in s_arr:
		n.append(letter_to_num(i))
	return n


""" This function takes a string, converts it to an array of characters, then changes it to
	an array of numbers representing each character. It then sorts this array of numbers using
	count sort.
"""
def word_to_nums(word):
	return count_sort_w(str_array_to_nums((str_to_arr(word))), 26)

"""
	letter_to_num takes a character and assigns it an integer value from 1 to 26.
	num_to_letter takes an integer value and returns a character.
"""
def letter_to_num(l):
	return(ord(l) - 96)

def num_to_letter(n):
	return(chr(n + 96))


""" This count sort takes a word represented as an array of characters, and a k number of
	unique characters (26). It creates a k long array of zeroes then at each index counts
	the number of times the character appears. It then loops through c to represent the 
	number of characters less than or equal to the index of c. The b array is then created and
	the sorted characters are placed into it.
"""
def count_sort_w(A, k):
	c = []
	for i in range(0, k + 1):
		c.append(0)
	for j in range(0, len(A)):
		c[A[j]] = c[A[j]] + 1
	for i in range(1, k + 1):
		c[i] = c[i] + c[i - 1]
	b = []
	for h in range(0, len(A)):
		b.append(0)
	for j in range(len(A) - 1, -1, -1):
		b[c[A[j]] - 1] = A[j]
		c[A[j]] = c[A[j]] - 1
	return(b)


""" count_sort takes an array of tuples, the number of unique characters, and a character index. 
	An array c is initialized and filled with k zeroes. The dth character in each tuple's sorted
	word is taken an used as an index for c and counts how many times that character appears.
	Another loop changes c's elements so that the number in each index represents the number
	of characters less than or equal to the index. The array b is then created and filled with
	zeroes until it is the length of A. Then at each index, b is given the tuple that corresponds
	to the sorted sorted word. In other words, the sorted words of each tuple are sorted
	alphabetically, but instead of placing the sorted words into their correct position in b, the
	tuple of that sorted word is placed in b. This returns an array of the original tuples sorted
	alphabetically by the sorted word by each character.
"""
def count_sort(A, k, d):
	c = []
	for i in range(0, k + 1):
		c.append(0)
	for j in range(0, len(A)):
		c[A[j][1][d]] = c[A[j][1][d]] + 1
	for i in range(1, k + 1):
		c[i] = c[i] + c[i - 1]
	b = []
	for h in range(0, len(A)):
		b.append(0)
	for j in range(len(A) - 1, -1, -1):
		b[c[A[j][1][d]] - 1] = A[j]
		c[A[j][1][d]] = c[A[j][1][d]] - 1
	return(b)


""" radix_sort takes an array of tuples and a number of characters(digits). The array is
	looped as many times as there are characters, and each time the array is sorted by
	the ith character in the tuple's sorted word using count_sort.
"""
def radix_sort(A, d):
	arr = A
	for i in range(d - 1, -1, -1):
		arr = count_sort(arr, 26, i)
	return arr


""" This function takes a array of tuples, and if there are elements in the array, it will
	use radix sort passing the array and the array's tuple's word length.
"""
def sort_sorted(group):
	if len(group) > 0:
		rad = radix_sort(group, group[0][2])
		return rad
	else:
		return []


""" The Group_Array is an array that holds word tuples. When its initialized, an array is
	created and a max_length is initialized that will keep track of the number of characters
	in the longest word.
	get_group_array returns the underlying array.
	group_append appends a tuple to the array, while updating the max_length.
	get_max_length returns the max_length.
"""
class Group_Array:

	def __init__(self):
		self.g_arr = []
		self.max_length = 1

	def get_group_array(self):
		return self.g_arr

	def group_append(self, group):
		if group[2] > 0:
			self.g_arr.append(group)
			if group[2] > self.max_length:
				self.max_length = group[2]

	def get_max_length(self):
		return self.max_length


""" This function takes an Group_Array(array of word tuples) and the number of characters
	in the longest word. A new array is created and an array is appended to it for every
	different length of a word from 0 to the maximum. Every tuple in the Group_Array is
	then appended to the array in len_array at the index of the length of the tuple's word.
	This separates the tuples into arrays by length of word.
"""
def len_org(arr, mx):
	len_array = []
	for j in range(0, mx + 1):
		len_array.append([])
	for i in arr:
		len_array[i[2]].append(i)
	return len_array
	

""" Takes an array and converts it to a string.
"""
def array_to_string(arr):
	s = ''
	for i in arr:
		s = s + ' ' + i
	return s


""" This takes two words then compares each of their characters and returns True is the
	two words are the same.
"""
def str_compare(word1, word2):
	if len(word1) != len(word2):
		return False
	for c in range(0, len(word1)):
		if word1[c] != word2[c]:
			return False
	return True


""" This function takes a group of word tuples organized by the word sorted by letter.
	While there are tuples in the group, an array is created and the word of the first tuple of
	the group is appended. This tuple is then removed from the original group.
	It then compares the sorted word of the tuple just removed from the group and the next
	tuple in the group which is now the first element. If the sorted words are the same
	then the word of the tuple in the orignal group is removed and added to the new array.
	When the sorted words don't match, the loop breaks and the array now containing the anagrams
	is written to the output file.
"""
def write_anagrams(group, target):
	while len(group) > 0:
		holder = group[0]
		arr = [holder[0]]	
		group.remove(holder)
		while True:
			if len(group) == 0:
				break
			elif str_compare(holder[1], group[0][1]) == True:				
				arr.append(group[0][0])
				group.remove(group[0])
			else:
				break
		target.write(array_to_string(arr) + '\n')


""" Usage method prints the program usage.
"""
def usage():
	print('Usage: python3 {} [dictionary]'.format(sys.argv[0]))
	sys.exit()


""" This creates a Group_Array object. Then the function reads each line one at a time.
	It takes the word on each line and creates a tuple containing the word, the word after
	its letters have been sorted, and the length of the word. This tuple then is appended
	to the Group_Array object using group_append.
	Once all words have been read, the word tuples contained in the Group_Array are organized
	by the length of the word using len_org function, which takes the Group_Array and the 
	maximum length of all the words.
	For each group of a certain length, the group is sorted by the second element in the tuple,
	which is the sorted version of the word by letter.
	The group is then passed to write_anagrams after its been sorted so that the anagram
	classes can be written to the output file.
	The dictionary file is then closed.
"""
def anagrams(fd, target):
	w = Group_Array()
	while True:
		x = fd.readline().strip()
		if not x:
			break
		w.group_append((x, word_to_nums(x), len(x)))

	l = len_org(w.get_group_array(), w.get_max_length())

	for i in l:
		x = sort_sorted(i)
		if len(x) > 0:
			print("Writing anagrams...")
			write_anagrams(x, target)
	
	fd.close()


""" This is the main method that runs. It checks whether there is enough arguments
	and if there is, it opens a file to write to. It names the file according to 
	the dictionary inputted. It then opens the dictionary file and sends the opened
	dictionary and the target output file to the function anagrams.
"""
def main():
	if len(sys.argv) != 2:
		usage()
	else:
		if sys.argv[1] == 'dict1':
			target = open('anagram1', 'w')
		if sys.argv[1] == 'dict2':
			target = open('anagram2', 'w')
		fd = open_file(sys.argv[1])
		anagrams(fd, target)	

if __name__ == '__main__':
    main() 