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
	return(arr_to_str(word))

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

def num_array_to_str(n_arr):
	s = []
	for i in n_arr:
		s.append(num_to_letter(i))
	return s

# class Tuple:

# 	def __init__(self, t1, t2):
# 		self.t1 = t1
# 		self.t2 = t2

# 	def get_t1(self):
# 		return self.t1

# 	def get_t2(self):
# 		return self.t2

def letter_to_num(l):
	return(ord(l) - 96)

def num_to_letter(n):
	return(chr(n + 96))

# def count_sort(A, k, d):
# 	c = []
# 	for i in range(0, k + 1):
# 		c.append(0)
# 	for j in range(0, len(A)):
# 		c[A[j][d]] = c[A[j][d]] + 1
# 	for i in range(1, k + 1):
# 		c[i] = c[i] + c[i - 1]
# 	b = []
# 	for h in range(0, len(A)):
# 		b.append(0)
# 	for j in range(len(A) - 1, -1, -1):
# 		b[c[A[j][d]] - 1] = A[j]
# 		c[A[j][d]] = c[A[j][d]] - 1
# 	return(b)
def helper(word):
	return str_array_to_nums(str_to_arr(word))

def count_sort(A, k, d):
	c = []
	for i in range(0, k + 1):
		c.append(0)
	for j in range(0, len(A)):
		c[helper(A[j].get_sort())[d]] = c[helper(A[j].get_sort())[d]] + 1
	for i in range(1, k + 1):
		c[i] = c[i] + c[i - 1]
	b = []
	for h in range(0, len(A)):
		b.append(0)
	for j in range(len(A) - 1, -1, -1):
		b[c[helper(A[j].get_sort())[d]] - 1] = A[j]
		c[helper(A[j].get_sort())[d]] = c[helper(A[j].get_sort())[d]] - 1
	return(b)

def radix_sort(A, d):
	arr = A
	for i in range(d - 1, -1, -1):
		arr = count_sort(arr, 26, i)
	return arr

def sort_sorted(group):
	# arr = []
	# for i in group:
	# 	arr.append(str_array_to_nums(str_to_arr(i.get_sort())))
	if len(group) > 0:
		rad = radix_sort(group, group[0].get_length())
		# sort = []
		# for i in rad:
		# 	sort.append(num_array_to_str(i))
		# return sort
		return rad

class Word_Group:

	def __init__(self, word):
		self.word = arr_to_str(word)
		self.sort = slow_sort(word)
		self.length = len(word)

	def get_word(self):
		return self.word

	def get_sort(self):
		return self.sort

	def get_length(self):
		return self.length

	def to_string(self):
		return "({}, {}, {})".format(self.word, self.sort, self.length)

class Group_Array:

	def __init__(self):
		self.g_arr = []
		self.max_length = 1

	def get_group_array(self):
		return self.g_arr

	def group_append(self, group):
		if group.get_length() > 0:
			self.g_arr.append(group)
			if group.get_length() > self.max_length:
				self.max_length = group.get_length()

	def get_max_length(self):
		return self.max_length

def len_org(arr, mx):
	len_array = []
	for j in range(0, mx + 1):
		len_array.append([])
	for i in arr:
		len_array[i.get_length()].append(i)
	# for x in len_array[8]:
	# 	print(x.to_string())
	return len_array

def split_groups(len_groups, target):
	for group in len_groups:
		print("Writing anagrams...")
		if len(group) > 0:
			if 5 < group[0].get_length() < 12:
				group_split(group, target)
			else:
				write_anagrams(group, target)	
		
		
def write_anagrams(group, target):
	while len(group) > 0:
		holder = group[0]
		a = [holder.get_word()]	
		group.remove(holder)	
		for j in group:
			if str_compare(holder.get_sort(), j.get_sort()) == True:
				a.append(j.get_word())
				group.remove(j)	
		target.write(array_to_string(a) + '\n')	
		
def group_split(group, target):
	a_arr = []
	rest_arr = []
	for i in group:
		if i.get_sort()[0] == 'a':
			a_arr.append(i)
		else:
			rest_arr.append(i)
	write_anagrams(a_arr, target)
	write_anagrams(rest_arr, target)
	
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



def main():
	
	# word_array = []
	# with open(sys.argv[1]) as fd:
	# 	for line in fd:
	# 		x = str_to_arr(fd.readline())
	# 		if len(x) > 0:
	# 			word_array.append(Word_Group(x))
	# len_org(word_array)

	w = Group_Array()
	fd = open_file(sys.argv[1])
	count = 0
	while True:
		count += 1
		x = fd.readline()
		if not x:
			break
		y = str_to_arr(x)
		w.group_append(Word_Group(y))
	if sys.argv[1] == 'dict1':
		target = open('anagrams1', 'w')
	if sys.argv[1] == 'dict2':
		target = open('anagrams2', 'w')

	l = len_org(w.get_group_array(), w.get_max_length())
	# for i in l[1]:
	# 	print(i.get_word())
	# split_groups(l, target)
	
	for i in l:
		for j in range(0, len(i)):
			print(sort_sorted(i)[j].to_string())

	# az_arr = [['d', 'o', 'g'], ['c', 'a', 't'], ['p', 'o', 't'], ['c', 'a', 'n']]
	# z = []
	# for i in az_arr:
	# 	z.append(str_array_to_nums(i))
	# r = radix_sort(z, 3)
	# for i in r:
	# 	print(num_array_to_str(i))
	
	fd.close()

if __name__ == '__main__':
    main() 