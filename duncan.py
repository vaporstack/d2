import os
import json

class Duncan(object):
	def __init__(self):
		self.data = {}

		dfile = "data/data.json"
		data = {}
		if os.path.exists(dfile):
			with open(dfile) as f:
				data = json.loads(f.read())
		else:
			data = {}
		self.data = data
		self.dfile = dfile

	def greet(self, author, channel, text):
		return "Hello, %s" % author

	def grab(self, author, channel, text):
		return "Unfortunately .grab is not implemented yet. (workin on it)"

	def _list(self):
		funcs = dir(self)
		funcs = [x for x in funcs if "_" not in x]
		funcs = [x for x in funcs if x != "data" and x != "dfile" and x != "stop"]
		return funcs

	def list(self, author, channel, text):
		return "Commands: " + ", ".join(self._list())

	def stop(self):
		# 	write stuff

		with open(self.dfile, 'w') as f:
			f.write(json.dumps(self.data))

