import os
import json
import random
import datetime
import shutil

def iso():
	return datetime.datetime.now().isoformat()

def str2bool(v):
  return (v.lower() in ("yes", "true", "t", "1"))

class Duncan(object):
	def __init__(self):
		self.data = {}
		ddir = "data"
		if not os.path.exists:
			os.makedirs(ddir)
		dfile = "data/data.json"
		self._prefix = "."


		if not os.path.exists(dfile):
			shutil.copy("data/data.default.json", dfile)

		with open(dfile) as f:
			data = json.loads(f.read())
		#else:
		#	print("file does not exist")
		#	data = {}

		self._debug = False
		if 'debug' in data:
			self._debug = data['debug']
		#self._debug = True
		self.data = data
		self.dfile = dfile


	def debug(self, author, channel, text):
		self._debug = not self._debug
		return("debug: " + str(self._debug))

	def greet(self, author, channel, text):
		return "Hello, %s" % author

	def grab(self, author, channel, text):
		return "Unfortunately .grab is not implemented yet. (workin on it)"

	def dune(self, author, channel, text):
		return random.choice(self.data['quotes']['dune'])

	def decide(self, author, channel, text):
		if text.strip() == '':
			return "you didn't give me any options"

		ch = text.split(",")
		ch = [x.strip() for x in ch]
		return random.choice(ch)


	def last(self, author, channel, text):
		return "UNIMPLEMENTED TRAP"

	def fixme(self, author, channel, text):
		return "https://github.com/vaporstack/d2"

	def _common_list(self, author, channel, text, key, msg):
		if text.strip() == '':
			if key not in self.data:
				return msg

		if text.strip() == '':
			return random.choice(self.data[key])['text']

		if key in self.data:
			arr = self.data[key]
		else:
			arr = []
		rec = {}
		rec['author'] = author
		rec['text'] = text
		rec['timestamp'] = iso()
		arr.append(rec)
		self.data[key] = arr
		return "Added. %s [%d]" % (key, len(arr))

	def lunch(self, author, channel, text):
		return self._common_list(author, channel, text, "lunch", "can't tell you what's for lunch, no lunch options!\n(use `%slunch <some type of meal> to add one" % self._prefix)

	def joke(self, author, channel, text):
		return self._common_list(author, channel, text, "joke", "can't tell you a joke, I don't know any jokes.\n(use `%sjoke <some type of humor> to add one" % self._prefix)


	def _list(self):
		funcs = dir(self)
		funcs = [x for x in funcs if "_" not in x]
		funcs = [x for x in funcs if x != "data" and x != "dfile" and x != "stop"]
		return funcs

	def list(self, author, channel, text):
		return "Commands: " + ", ".join(self._list())

	def stop(self):
		# 	write stuff
		self.data['debug'] = self._debug
		with open(self.dfile, 'w') as f:
			f.write(json.dumps(self.data, indent=4))

