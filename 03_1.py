#advent of code
#2016, 03, 1

# python 03_1.py < input_03.txt
# correct answer: 1050

# --- Day 3: Squares With Three Sides ---
#
# Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.
#
# Or are they?
#
# The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.
#
# In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.
#
# In your puzzle input, how many of the listed triangles are possible?

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

for line in sys.stdin:
	total_count += 1
	triangle_input = line.split()
	triangle = Triangle(int(triangle_input[0]), int(triangle_input[1]), int(triangle_input[2]))
	if triangle.is_valid():
		valid_count += 1

print("Total", total_count)
print("Valid", valid_count)