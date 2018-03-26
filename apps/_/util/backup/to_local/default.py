#!/usr/bin/env python3

import os
import sys
import re
import time
import json
from ftplib import FTP

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '../../../../../../system')

import azbn as azbnpy

azbn = azbnpy.CreateAzbn()
app = azbnpy.CreateApp()

ftp = FTP()

def __load_config() :
	_path = 'config.json';
	d = {}
	with open(_path) as json_data :
		d = json.load(json_data)
	return d

def nlisting(dest, items) :
	for item in items :
		print(item)

def main() :
	cfg = __load_config()
	if cfg['servers'] :
		if len(cfg['servers']) > 0 :
			for item in cfg['servers'] :
				
				try :
					
					print('connect to ' + item['server'])
					
					ftp.connect(item['server'], item['port'])
					ftp.login(item['user'], item['pass'])
					ftp.cwd(item['path_src'])
					
					items = ftp.nlst();
					
					nlisting(item['path_dest'], items)
					
				except BaseException :
					
					print(BaseException)
					
				finally :
					
					ftp.quit()
				

if __name__ == '__main__' :
	main()