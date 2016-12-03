#advent of code
#2016, 01, 2

# python 01_2.py < input_01.txt
# correct answer: 136

#--- Day 1: No Time for a Taxicab ---
#
#--- Part Two ---
#
#Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the first location you visit twice.
#
#For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.
#
#How many blocks away is the first location you visit twice?


import sys

# view_point (N=0, E=1, S=2, W=3)
view_point = 0

# current position
pos_x = 0
pos_y = 0

visited_points = [(0,0)]

def go_santa(input):
	global view_point, pos_x, pos_y
	entries = parse_input(input)
	
	for entry in entries:
	
		print(entry)
		(direction, amount) = entry
		
		if(direction == 'R'):
			view_point = (view_point + 1) % 4
		elif(direction == 'L'):
			view_point = (view_point - 1) % 4
		
		if view_point == 0: #N
			log_trace_point(1, 0, amount)
			move_x(amount)
		elif view_point == 2: #S
			log_trace_point(-1, 0, amount)
			move_x(-amount)
		elif view_point == 1: #E
			log_trace_point(0, 1, amount)
			move_y(amount)
		elif view_point == 3: #W
			log_trace_point(0, -1, amount)
			move_y(-amount)
		else:
			raise Exception("unknown view_point: " + view_point)
			
		print (pos_x, pos_y)
	
	distance = abs(pos_x) + abs(pos_y)
	
	print("-----------------")
	print("x", pos_x, "y", pos_y)
	print("distance", distance)

def move_x(amount):
	global pos_x
	pos_x += amount
	
def move_y(amount):
	global pos_y
	pos_y += amount

def log_trace_point(x_change, y_change, amount):
	cur_x = pos_x
	cur_y = pos_y
	for i in range(amount):
		cur_x += x_change
		cur_y += y_change
		cur_point = (cur_x, cur_y)
		if cur_point in visited_points:
			print (visited_points)
			distance = abs(cur_x) + abs(cur_y)
			raise Exception("visited point: " + str(cur_x) + " " + str(cur_y) + " distance: " + str(distance))
		visited_points.append(cur_point)
	
def parse_input(input):
	input_entries = input.split(", ")
	return map(parse_entry, input_entries)
	
def parse_entry(entry):
	return (entry[0:1], int(entry[1:]))
	

input = sys.stdin.readline()
print("input: ", input)
go_santa(input)