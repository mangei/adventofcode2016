#advent of code
#2016, 02, 2

# python 02_2.py < input_02.txt
# correct answer: DD483

# --- Part Two ---
#
# You finally arrive at the bathroom (it's a several minute walk from the lobby so visitors can behold the many fancy conference rooms and water coolers on this floor) and go to punch in the code. Much to your bladder's dismay, the keypad is not at all like you imagined it. Instead, you are confronted with the result of hundreds of man-hours of bathroom-keypad-design meetings:
#
    # 1
  # 2 3 4
# 5 6 7 8 9
  # A B C
    # D
#
# You still start at "5" and stop when you're at an edge, but given the same instructions as above, the outcome is very different:
#
#  - You start at "5" and don't move at all (up and left are both edges), ending at 5.
#  - Continuing from "5", you move right twice and down three times (through "6", "7", "B", "D", "D"), ending at D.
#  - Then, from "D", you move five more times (through "D", "B", "C", "C", "B"), ending at B.
#  - Finally, after five more moves, you end at 3.
#
# So, given the actual keypad layout, the code would be 5DB3.
#
# Using the same instructions in your puzzle input, what is the correct bathroom code?


import sys

panel = [
	[None,None,None,None,None,None,None],
	[None,None,None,'1' ,None,None,None],
	[None,None,'2' ,'3' ,'4' ,None,None],
	[None,'5' ,'6' ,'7' ,'8' ,'9' ,None],
	[None,None,'A' ,'B' ,'C' ,None,None],
	[None,None,None,'D' ,None,None,None],
	[None,None,None,None,None,None,None]
]

def get_code():

	cur_pos_x = 3
	cur_pos_y = 3
	
	code = ""
	
	for line in sys.stdin:
		for c in line:
			if c == 'U' and is_valid_move(cur_pos_x, cur_pos_y - 1):
				cur_pos_y -= 1
			elif c == 'D' and is_valid_move(cur_pos_x, cur_pos_y + 1):
				cur_pos_y += 1
			elif c == 'L' and is_valid_move(cur_pos_x - 1, cur_pos_y):
				cur_pos_x -= 1
			elif c == 'R' and is_valid_move(cur_pos_x + 1, cur_pos_y):
				cur_pos_x += 1
	
		code += get_panel_value(cur_pos_x, cur_pos_y)
	
	print("Code", code)

def is_valid_move(x,y):
	return get_panel_value(x,y) is not None

def get_panel_value(x,y):
	return panel[y][x]
	
get_code()