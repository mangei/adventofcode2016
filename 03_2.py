#advent of code
#2016, 03, 1

# python 03_2.py < input_03.txt
# correct answer: 1921

# --- Part Two ---
#
# Now that you've helpfully marked up their design documents, it occurs to you that triangles are specified in groups of three vertically. Each set of three numbers in a column specifies a triangle. Rows are unrelated.
#
# For example, given the following specification, numbers with the same hundreds digit would be part of the same triangle:
#
# 101 301 501
# 102 302 502
# 103 303 503
# 201 401 601
# 202 402 602
# 203 403 603
#
# In your puzzle input, and instead reading by columns, how many of the listed triangles are possible?

import sys

class Triangle:
	"Triangle class"

	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
	
	def is_valid(self):
		return (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.a + self.c > self.b)

total_count = 0
valid_count = 0
triangle_input = []

for line in sys.stdin:
	triangle_input.append(line.split())
	if len(triangle_input) == 3:
		total_count += 3
		
		triangle1 = Triangle(int(triangle_input[0][0]), int(triangle_input[1][0]), int(triangle_input[2][0]))
		triangle2 = Triangle(int(triangle_input[0][1]), int(triangle_input[1][1]), int(triangle_input[2][1]))
		triangle3 = Triangle(int(triangle_input[0][2]), int(triangle_input[1][2]), int(triangle_input[2][2]))
		
		if triangle1.is_valid():
			valid_count += 1
		if triangle2.is_valid():
			valid_count += 1
		if triangle3.is_valid():
			valid_count += 1
		
		triangle_input = []

print("Total", total_count)
print("Valid", valid_count)