def get_meta(path, opt='file'):
	idx = 0
	cnt = 0
	enc = 0
	size = len(path)
	if path[size-1] == '/':
		path = path[:size-1]
		size = size-1
	for x in path:	
		if x == '/':	cnt+=1
	for x in path:
		if x == '/':
			enc += 1
			if enc == cnt:
				if opt == 'dir':
					return path[:idx] 
				elif opt == 'file':
					return path[idx+1:size-4]
				else:
					return path[-4:]
		idx += 1
	if opt == 'ext':
		return path[-4:]
	elif opt == 'file':
		return path[:size-4]
	return './'
