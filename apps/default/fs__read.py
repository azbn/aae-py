#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../system')

import azbn as azbnpy

azbn = azbnpy.CreateAzbn()
app = azbnpy.CreateApp()

def main():
	f = open('./hw.txt', 'r')
	try:
		str = f.read();
		print(str);
		
		#days_file.readlines()

		#with open("test.txt") as file_handler:
		#	for line in file_handler:
		# 		print(line)

		#l = [line.strip() for line in f]
		
	except Exception:
		print('Ошибка чтения')
	else:
		pass
	finally:
		f.close()

if __name__ == '__main__':
	main()