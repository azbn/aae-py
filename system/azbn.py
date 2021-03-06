import os
import sys
import json
import time

class CreateAzbn(object):
	
	TITLE = 'Azbn App Engine for Python'
	VERSION = '0.0.1'
	
	def __init__(self):
		"""Init function"""
		self._mdl = {}
		self._data = {}
	
	def __call__(self, uid):
		"""Get module for azbn"""
		if uid in self._mdl:
			return self._mdl[uid]
		else:
			return self
	
	def load(self, uid, obj):
		"""Create module for azbn"""
		self._mdl[uid] = obj
		return self
	
	def __getitem__(self, uid):
		"""Get item: azbn[]"""
		if uid in self._data:
			return self._data[uid]
		else:
			return None
	
	def __setitem__(self, uid, value):
		"""Set item: azbn[]"""
		self._data[uid] = value
	
	def info(self):
		"""Echo TITLE and VERSION"""
		print(self.TITLE, self.VERSION)
	
	def echo(self, s):
		"""Echo string"""
		print(s)
		return self

	def now(self):
		return time.time()

	def loadJSON(self, uid = ''):
		"""Load JSON from uid-file in common-dir"""
		_path = os.path.dirname(os.path.abspath(__file__)) + '/../common/' + uid + '.json';
		d = {}
		with open(_path) as json_data:
			d = json.load(json_data)
		return d
	
class CreateApp(object):
	
	def __init__(self):
		"""Init function"""
	
	def __call__(self, uid):
		"""Get module for azbn"""
		if uid in self._mdl:
			return self._mdl[uid]
		else:
			return self
