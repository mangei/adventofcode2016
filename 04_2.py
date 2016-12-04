#advent of code
#2016, 04, 2

# python 04_2.py < input_04.txt > output_04.txt
# (search file manually: zadftbaxq-anvqof-efadmsq northpole-object-storage 482)
# correct answer: 482

# --- Part Two ---
#
# With all the decoy data out of the way, it's time to decrypt this list and get moving.
#
# The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.
#
# To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.
#
# For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.
#
# What is the sector ID of the room where North Pole objects are stored?


import sys
import re
from string import ascii_lowercase
from operator import itemgetter

ord_a = ord("a")
target_room = "northpole-object-storage"
target_room_id = None

for line in sys.stdin:
	matchObj = re.match("^([a-z-]+)-(\d+)\[(.+)\]$", line)
	name = matchObj.group(1)
	sector_id = int(matchObj.group(2))
	checksum = matchObj.group(3)
	
	name_decrypted = ""
	for c in name:
		c_decryped = c
		if c != "-":
			c_decryped = chr((ord(c) - ord_a + sector_id) % 26 + ord_a)
			# optimize this by precalculating the cipher map
		name_decrypted += c_decryped
	
	print(name, name_decrypted, sector_id)
	
	if name_decrypted == target_room:
		target_room_id = sector_id
		
print()
print("target_room_id", target_room_id)