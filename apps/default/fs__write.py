#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../system')

import azbn as azbnpy

azbn = azbnpy.CreateAzbn()
app = azbnpy.CreateApp()

def main():
	f = open('./hw.txt', 'w')
	try:
		f.write('Hello, World!')
	except Exception:
		print('Ошибка записи в файл')
	else:
		pass
	finally:
		f.close()
	
	#with open(filename, ‘w’) as myfile:
	#	
	
if __name__ == '__main__':
	main()