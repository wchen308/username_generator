"""
Wechat Random Username generator
1. start with a letter
2. len: 6-20
3. valid character: number, letter, _, -
"""

import random
import string


def UsernameGenerator():
	len_username = random.randint(6, 20)
	
	valid_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
	'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
	'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
	'_', '-']
	
	username = random.choice(string.ascii_lowercase)
	for i in range(len_username - 1):
		random_char = valid_char[random.randint(0, len(valid_char) - 1)]
		username = username + random_char

	return username

print(UsernameGenerator())