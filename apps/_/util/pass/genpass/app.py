#!/usr/bin/env python3
##
# !/usr/bin/python3

import os
import sys
import string
import random

argv = sys.argv

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../../../../system')
#print(sys.path)

import azbn as azbnpy

#x = 0
#for i in range(10**10):
#	x += 1
#print(x)

azbn = azbnpy.CreateAzbn()
app = azbnpy.CreateApp()

def randompassword(size):
	spec = '!@#$%&*?^()-=_+.'
	chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + spec
	#size = random.randint(8, 12)
	return ''.join(random.choice(chars) for x in range(size))

def main(_argv):
	
	l = 32
	c = 32
	
	for parameter in _argv:
		if 'l=' in parameter:
			l = int(parameter[parameter.find('=')+1:])
		if 'c=' in parameter:
			c = int(parameter[parameter.find('=')+1:])
	
	#p = randompassword(l);
	
	with open('passwords.txt', 'w') as f:
		for x in range(c):
			p = randompassword(l);
			f.write(p)
			f.write('\n')
	
if __name__ == '__main__':
	main(argv)