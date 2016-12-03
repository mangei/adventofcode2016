#advent of code
#2016, 01, 1

# python 01_1.py < input_01.txt
# correct answer: 209

#--- Day 1: No Time for a Taxicab ---
#
#Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.
#
#Collect stars by solving puzzles. Two puzzles will be made available on each day in the advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!
#
#You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.
#
#The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.
#
#There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?
#
#For example:
#
# - Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
# - R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
# - R5, L5, R5, R3 leaves you 12 blocks away.
#
#How many blocks away is Easter Bunny HQ?

import sys

def go_santa(input):
	entries = parse_input(input)
	
	# view_point (N=0, E=1, S=2, W=3)
	view_point = 0

	# current position
	pos_x = 0
	pos_y = 0
	
	for entry in entries:
	
		print(entry)
		(direction, amount) = entry
		
		if(direction == 'R'):
			view_point = (view_point + 1) % 4
		elif(direction == 'L'):
			view_point = (view_point - 1) % 4
		
		if view_point == 0: #N
			pos_x += amount
		elif view_point == 2: #S
			pos_x -= amount
		elif view_point == 1: #E
			pos_y += amount
		elif view_point == 3: #W
			pos_y -= amount
		else:
			raise Exception("unknown view_point: " + view_point)
	
	distance = abs(pos_x) + abs(pos_y)
	
	print("-----------------")
	print("x", pos_x, "y", pos_y)
	print("distance", distance)

def parse_input(input):
	input_entries = input.split(", ")
	return map(parse_entry, input_entries)
	
def parse_entry(entry):
	return (entry[0:1], int(entry[1:]))
	

input = sys.stdin.readline()
print("input: ", input)
go_santa(input)