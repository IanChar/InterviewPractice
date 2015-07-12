import math

# Given staircase with n stairs and a child that can do 1, 2, or 3 steps at a time,
# Find all possible ways that the child can get up the stairs

# DP can be used to speed up nearly to O(n)
def q1(n):
	d = {}
	return staircase(n, d)

def staircase(n, d):
	if n < 1:
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 2
	elif n == 3:
		return 4
	
	if n in d.keys():
		return d[n]
	else:
		ways = staircase(n - 1, d) + staircase(n - 2, d) + staircase(n - 3, d)
		d[n] = ways
		return ways

def q1_test():
	print ""
	print "5:", q1(5)
	print "9:", q1(9)
	print "17:", q1(17)
	print ""

# Given a grid, how many ways are there to get from (0,0) to (x,y)
# FOLLOW UP: what if cannot cross coordinate (w,z)
def q2(coord, coord2 = None):
	#Actual practical math way... Although may be same time if you DP recursion
	s = coord[0] + coord[1]
	ans = math.factorial(s)/(math.factorial(coord[0]) * math.factorial(coord[1]))
	if coord2:
		s2 = coord2[0] + coord2[1]
		ans -= math.factorial(s2)/(math.factorial(coord2[0]) * math.factorial(coord2[1])) * math.factorial(s - s2)/(math.factorial(coord[0] - coord2[0]) * math.factorial(coord[1] - coord2[1]))
	print "Math method says:", ans
	# In the spirit of recursion!
	d = {}
	if coord2:
		ans = grid(coord, d, coord2)
	ans = grid(coord, d)
	print "Recursion method says:", ans
	return ans

def grid(coord, d, coord2 = None):
	if coord[0] < 0 or coord[1] < 0:
		return 0
	if coord2:
		if coord2[0] == 0 and coord2[1] == 0:
			return 0
	if coord[0] == 0 and coord[1] == 0:
		return 1
	if coord in d.keys():
		return d[coord]
	else:
		if coord2:
			ways = grid((coord[0] - 1, coord[1]), d, (coord2[0] - 1, coord2[1])) + grid((coord[0], coord[1] - 1), d, (coord2[0], coord2[1] - 1))
		else:
			ways = grid((coord[0] - 1, coord[1]), d, coord2) + grid((coord[0], coord[1] - 1), d, coord2)
		d[coord] = ways
		return ways

def q2_test():
	print ""
	print "(1,1)\n", q2((1,1))
	print "(3,3)\n", q2((3,3))
	print "(5,8)\n", q2((5,8))
	print "(2,2) excluding (1,1)\n", q2((2,2), (1,1))
	print "(3,3) excluding (1,3)\n", q2((3,3), (1,3))
	print "(6,8) excluding (5,5)\n", q2((6,8), (5,5))
	print ""

# Given a sorted array, find the entry where the index == entry
# Don't think you can do DP on this one
# This is the soln if all values are distinct.
def q3(arr, start = None, end = None):
	if len(arr) == 0:
		return False
	if start is None:
		start = 0
		end = len(arr)
	if start + 1 == end:
		if arr[start] == start:
			return start
		else:
			return False
	mid = (end + start) // 2
	if arr[mid] == mid:
		return mid
	elif arr[mid] < mid:
		return q3(arr, mid + 1, end)
	else:
		return q3(arr, start, mid)

def q3_test():
	test1 = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
	print "Magic entry for", test1, "..."
	print q3(test1)

if __name__ == '__main__':
	running = True
	while running:
		num = raw_input("Input question to test (type q for quit): ")
		if str(num) == 'q':
			running = False
			break
		if int(num) == 1:
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
		elif int(num) == 9:
			q9_test()	
		else:
			print "Invalid input"