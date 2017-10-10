#!/usr/bin/python3

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../system')
#print(sys.path)

import azbn as azbnpy

#x = 0
#for i in range(10**10):
#	x += 1
#print(x)

azbn = azbnpy.CreateAzbn()
app = azbnpy.CreateApp()

def main():
	
	#print(azbn('test'))
	#azbn['test'] = 27
	#print(azbn['test'])
	#print(azbn('test'))
	help(azbn.echo)

if __name__ == '__main__':
	main()