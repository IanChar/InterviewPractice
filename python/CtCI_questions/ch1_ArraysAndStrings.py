
#Implement an algorithm to determine if a string has all unique characters. 
#What if you cannot use additional data structures?
def q1(s):
	if len(s) > 128:
		return False
	#with additional data structures
	char_table = []
	unique = True
	for i in range(128):
		char_table.append(False)
	for char in s:
		if char_table[ord(char)]:
			unique = False
			break
		else:
			char_table[ord(char)] = True
	print "Algorithm with data structure: ", unique

	unique = True
	for i in range(len(s) - 1):
		for j in range(i + 1, len(s)):
			if i == j:
				unique = False
				break
	print "Algorithm without data structure: ", unique, "\n"

def q1_test():
	print "Testing ", '""'
	q1("")
	print "Testing: This should return false"
	q1("This should return false")
	print "Testing: ABCDEFGabcdefg"
	q1("ABCDEFGabcdefg")

#Implement a function that reverses a string
def q2(s):
	if len(s) == 0:
		print ""
		return 
	new_s = ""
	for i in range(len(s) - 1, -1, -1):
		new_s += s[i]
	print new_s

def q2_test():
	print "Testing ", '""'
	q2("")
	print "Testing: This should return false"
	q2("This should return false")
	print "Testing: cat"
	q2("cat")

#Given two strings find out if one is a permutation of the other
def q3(s1, s2):
	if len(s1) != len(s2):
		print "False"
		return False
	#Slower and simpler method on sorting O(2n + 2nlogn + n)
	list1 = []
	list2 = []
	for i in range(len(s1)):
		list1.append(ord(s1[i]))
		list2.append(ord(s2[i]))
	list1.sort()
	list2.sort()
	same = True
	if list1 == list2:		
		print "Method one says True"
	else:
		print "Method one says False"

	#Faster method on char count O(2n)
	char_table = []
	for i in range(128):
		char_table.append(0)
	for i in range(len(s1)):
		char_table[ord(s1[i])] += 1
		char_table[ord(s2[i])] -= 1
	same = True
	for i in range(128):
		if char_table[i] != 0:
			same = False
			break
	print "Method two says ", same

def q3_test():
	print "Testing ", '"" and ""'
	q3("", "")
	print "Testing: True Test and rusT Teet"
	q3("True Test", "rusT Teet")
	print "Testing: abcde and abcdf"
	q3("abcde", "abcdf")

#Write function to replace all spaces with %20
def q4(s):
	#Built in solution 
	print s.replace(" ", "%20")

	#Manual solution cannot do inplace 
	new_string = ""
	for char in s:
		if char == ' ':
			new_string += "%20"
		else:
			new_string += char
	print new_string

def q4_test():
	print "Testing ", '""'
	q4("")
	print "Testing: This should return false"
	q4("This should return false")
	print "Testing: cat"
	q4("cathattat ")

#Implement a method to do string compression 
#For example aaabcccccaa becomes a3b1c5a2
def q5(s):
	if len(s) == 0:
		print ""
		return
	#This method is bad because string concats take O(n^2)
	#So overall time is O(s + k^2) where s is string size 
	#and k is segments in string
	last_char = s[0]
	curr_count = 1
	new_string = last_char
	for i in range(1, len(s)):
		if s[i] == last_char:
			curr_count += 1
		else:
			new_string += str(curr_count)
			last_char = s[i]
			new_string += last_char
			curr_count = 1
	new_string += str(curr_count)
	print new_string

	#Can use a string buffer instead...
	s_buf = []
	s_buf.append(s[0])
	s_buf.append(1)
	for i in range(1, len(s)):
		if s[i] == s_buf[-2]:
			s_buf[-1] += 1
		else:
			s_buf.append(s[i])
			s_buf.append(1)
	for char in s_buf:
		print char,
	print '\n'


def q5_test():
	print "Testing ''"
	q5("")
	print "Testing a"
	q5("a")
	print "Testing aaabcccccaa"
	q5("aaabcccccaa")

#Given an image represented by an nxn matrix, where each pixel in the image
#is 4 bytes, write a method to rotate the image by 90 degrees. Can you do this
#in place?
def q6(arr, n, start = 0):
	#This does not have to be recursive, in fact it is probably a bit slow because of it
	end = n - 1 - start
	if start == 0 and start == end:
		print arr
	if start == end or start > n / 2:
		return
	for i in range(end - start):
		temp = arr[start][start + i]
		arr[start][start + i] = arr[end - i][start]
		arr[end - i][start] = arr[end][end - i]
		arr[end][end - i] = arr[start + i][end]
		arr[start + i][end] = temp
	q6(arr, n, start + 1)
	if start == 0:
		print arr

def q6_test():
	arr1 = [[0 for x in range(1)] for x in range(1)]
	arr2 = [[0 for x in range(2)] for x in range(2)]
	arr2[0][0] = 1
	arr2[0][1] = 2
	arr2[1][0] = 3
	arr2[1][1] = 4
	arr3 = [[0 for x in range(3)] for x in range(3)]
	for i in range(9):
		arr3[i // 3][i % 3] = i + 1
	arr4 = [[0 for x in range(4)] for x in range(4)]
	for i in range(16):
		arr4[i // 4][i % 4] = i + 1

	print "Testing 1x1... "
	q6(arr1, 1)
	print "\n Testing 2x2..."
	q6(arr2, 2)
	print "\n Testing 3x3..."
	q6(arr3, 3)
	print "\n Testing 4x4..."
	q6(arr4, 4)

#Write an algorithm such that if an element in an mxn matrix is 0, 
#its entire row and column are set to 0.
def q7(arr, m, n):
	rows = []
	cols = []
	for i in range(m):
		rows.append(False)
	for i in range(n):
		cols.append(False)
	i = 0
	for i in range(m):
		for j in range(n):
			if arr[i][j] == 0:
				rows[i] = True
				cols[j] = True
	
	for i in range(m):
		if rows[i]:
			for j in range(n):
				arr[i][j] = 0
	for j in range(n):
		if cols[j]:
			for i in range(m):
				arr[i][j] = 0
	print arr

def q7_test():
	arr1 = [[1 for x in range(1)] for x in range(3)]
	arr2 = [[0 for x in range(3)] for x in range(2)]
	arr2[0][0] = 1
	arr2[0][1] = 2
	arr2[0][2] = 3
	arr2[1][0] = 0
	arr2[1][1] = 4
	arr2[1][2] = 5
	arr3 = [[0 for x in range(3)] for x in range(5)]
	for i in range(15):
		if i == 5 or i == 10:
			arr3[i // 3][i % 3] = 0	
		else:
			arr3[i // 3][i % 3] = i + 1
	arr4 = [[0 for x in range(4)] for x in range(3)]
	for i in range(12):
		if i == 5 or i == 0:
			arr4[i // 4][i % 4] = 0	
		else:
			arr4[i // 4][i % 4] = i + 1

	print "Testing 1x1... "
	print arr1
	q7(arr1, 3, 1)
	print "\n Testing 2x2..."
	print arr2
	q7(arr2, 2, 3)
	print "\n Testing 3x3..."
	print arr3
	q7(arr3, 5,3)
	print "\n Testing 4x4..."
	print arr4
	q7(arr4, 3,4)

#If you have isSubstring that checks if one word is a substring of another,
#check if s2 is a rotation of s1 using one call to isSubstring
def isSubstring(s1, s2):
	return s2 in s1

def q8(s1, s2):
	#So tricky had to look in solns but simple
	if len(s1) != len(s2):
		return False
	s1s1 = s1 + s1
	return isSubstring(s1s1, s2)

def q8_test():
	print "waterbottle and erbottlewat?", q8("waterbottle", "erbottlewat")
	print "hatter and terhat?", q8("hatter", "terhat")
	print "parade and rade?", q8("parade", "rade")
	print "spoons and oposns", q8("spoons", "oposns")

if __name__ == '__main__':
	running = True
	while running:
		num = raw_input("Input question to test (type q for quit): ")
		try:
			if str(num) == 'q':
				running = False
				break
			elif int(num) == 1:
				q1_test()
			elif int(num) == 2:
				q2_test()
			elif int(num) == 3:
				q3_test()
			elif int(num) == 4:
				q4_test()
			elif int(num) == 5:
				q5_test()
			elif int(num) == 6:
				q6_test()
			elif int(num) == 7:
				q7_test()
			elif int(num) == 8:
				q8_test()
			else:
				print "Invalid input"
		except:
			print "Invalid input"