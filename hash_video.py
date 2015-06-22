import os, hashlib

#Leave untouched
def get_hash(name):
  readsize = 64 * 1024
  with open(name, 'rb') as f:
		size = os.path.getsize(name)
		data = f.read(readsize)
		f.seek(-readsize, os.SEEK_END)
		data += f.read(readsize)
  return hashlib.md5(data).hexdigest()
#Start here
