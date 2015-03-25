#!/usr/bin/env python3

import sys
import words

def open_file(filename):
	return(open(filename))

def slow_sort(word):
	for i in range(0, len(word)):
		for j in range(i + 1, len(word)):
			if word[i] > word[j]:
				holder = word[i]
				word[i] = word[j]
				word[j] = holder
	return(word)

def str_to_arr(word):
	a = []
	for c in word:
		if c >= 'a' and c <= 'z':
			a.append(c)
	return a

def arr_to_str(a):
	s = ''
	for i in a:
		s = s + i
	return s

def str_array_to_nums(s_arr):
	n = []
	for i in s_arr:
		n.append(letter_to_num(i))
	return n

def word_to_nums(word):
	return count_sort_w(str_array_to_nums((str_to_arr(word))), 26)
	# return str_array_to_nums(slow_sort(str_to_arr(word)))

def letter_to_num(l):
	return(ord(l) - 96)

def num_to_letter(n):
	return(chr(n + 96))

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

def radix_sort(A, d):
	arr = A
	for i in range(d - 1, -1, -1):
		arr = count_sort(arr, 26, i)
	return arr

def sort_sorted(group):
	if len(group) > 0:
		rad = radix_sort(group, group[0][2])
		return rad
	else:
		return []

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

def len_org(arr, mx):
	len_array = []
	for j in range(0, mx + 1):
		len_array.append([])
	for i in arr:
		len_array[i[2]].append(i)
	return len_array
	
def array_to_string(arr):
	s = ''
	for i in arr:
		s = s + ' ' + i
	return s

def str_compare(word1, word2):
	if len(word1) != len(word2):
		return False
	for c in range(0, len(word1)):
		if word1[c] != word2[c]:
			return False
	return True

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

def usage():
	print('Usage: python3 {} [dictionary]'.format(sys.argv[0]))
	sys.exit()

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

def main():
	if len(sys.argv) != 2:
		usage()
	else:
		if sys.argv[1] == 'dict1':
			target = open('anagrams1', 'w')
		if sys.argv[1] == 'dict2':
			target = open('anagrams2', 'w')
		fd = open_file(sys.argv[1])
		anagrams(fd, target)	

if __name__ == '__main__':
    main() 