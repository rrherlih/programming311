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

# def num_array_to_str(n_arr):
# 	s = []
# 	for i in n_arr:
# 		s.append(num_to_letter(i))
# 	return s

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
		c[A[j].get_sort()[d]] = c[A[j].get_sort()[d]] + 1
	for i in range(1, k + 1):
		c[i] = c[i] + c[i - 1]
	b = []
	for h in range(0, len(A)):
		b.append(0)
	for j in range(len(A) - 1, -1, -1):
		b[c[A[j].get_sort()[d]] - 1] = A[j]
		c[A[j].get_sort()[d]] = c[A[j].get_sort()[d]] - 1
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
	else:
		return []

class Word_Group:

	def __init__(self, word):
		self.word = word
		self.sort = str_array_to_nums(slow_sort(str_to_arr(word)))
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
	return len_array

def split_groups(len_groups, target):
	for group in len_groups:
		print("Writing anagrams...")
		if len(group) > 0:
			if 5 < group[0].get_length() < 12:
				group_split(group, target)
			else:
				write_anagrams(group, target)	
		
		
# def write_anagrams(group, target):
# 	while len(group) > 0:
# 		holder = group[0]
# 		a = [holder.get_word()]	
# 		group.remove(holder)	
# 		for j in group:
# 			if str_compare(holder.get_sort(), j.get_sort()) == True:
# 				a.append(j.get_word())
# 				group.remove(j)	
# 		target.write(array_to_string(a) + '\n')	
	
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
	comps = 0
	while len(group) > 0:
		holder = group[0]
		arr = [holder.get_word()]	
		group.remove(holder)
		while True:
			if len(group) == 0:
				break
			elif str_compare(holder.get_sort(), group[0].get_sort()) == True:
				comps += 1
				arr.append(group[0].get_word())
				group.remove(group[0])
			else:
				break
		target.write(array_to_string(arr) + '\n')
	print(comps)

def main():

	w = Group_Array()
	fd = open_file(sys.argv[1])
	count = 0
	while True:
		# if count%10000 == 0:
		# 	print(count)
		# count += 1
		x = fd.readline().strip()
		if not x:
			break
		w.group_append(Word_Group(x))
	if sys.argv[1] == 'dict1':
		target = open('anagrams1', 'w')
	if sys.argv[1] == 'dict2':
		target = open('anagrams2', 'w')

	l = len_org(w.get_group_array(), w.get_max_length())

	for i in l:
		x = sort_sorted(i)
		if len(x) > 0:
			print("Writing anagrams...")
			write_anagrams(x, target)
	
	fd.close()

	# if sys.argv[1] == 'dict1':
	# 	target = open('anagrams1', 'w')
	# if sys.argv[1] == 'dict2':
	# 	target = open('anagrams2', 'w')
	
	# fd = open_file(sys.argv[1])
	# maxl = 2
	# count = 1
	# while count <= maxl:
	# 	print("Words of length {}".format(count))
	# 	w = Group_Array()
	# 	while True:
	# 		x = fd.readline()			
	# 		if not x:
	# 			break
	# 		y = str_to_arr(x)
	# 		if len(y) == count:				
	# 			w.group_append(Word_Group(y))
	# 		if len(y) > maxl:
	# 			maxl = len(y)
	# 	count += 1
	# 	fd.seek(0)
	# 	write_anagrams(sort_sorted(w.get_group_array()), target)	
	
	# fd.close()

if __name__ == '__main__':
    main() 