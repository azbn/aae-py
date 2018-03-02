#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../system')

import azbn as azbnpy

azbn = azbnpy.CreateAzbn()
app = azbnpy.CreateApp()

def main():
	with open('./hw2.txt', 'w') as f:
		try:
			f.write('Hello, World!')
		except Exception:
			print('Ошибка записи в файл')
		else:
			pass
	
if __name__ == '__main__':
	main()