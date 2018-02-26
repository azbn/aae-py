#!/usr/bin/env python3

import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../system')

import azbn as azbnpy

azbn = azbnpy.CreateAzbn()
app = azbnpy.CreateApp()

def main():
	try:
		
		#текущий каталог
		#print(os.getcwd())

		#создание каталога
		#os.mkdir('test');

		#создание дерева каталога
		#os.makedirs('ONE/TWO/THREE')
		
		#листинг каталога
		#print(os.listdir('ONE'))

		#инфо о каталоге
		#print(os.stat(os.getcwd()))

		#Переименовать файл|каталог:
		#os.rename('text2.txt', 'xett.txt')

		#удаление каталога
		#os.rmdir('ETXT')

		#Смена текущего каталога:
		#os.chdir('/home')

		#Проверка наличия файла в текущем каталоге:
		#os.path.exists('my_file')

		#Модуль shutil, в отличие от os, позволяет выполнять операции над деревьями данных.
		#Скопировать дерево:
		#shutil.copytree('../python', '../copy-python')
		#shutil.move('../copy-python', 'python-copy')
		#shutil.rmtree('python-copy')

	except Exception:
		print(Exception)
	else:
		pass
	finally:
		pass

if __name__ == '__main__':
	main()