import sys, os, re
sys.dont_write_bytecode = True	# Who likes pyc files

# Import custom modules
import meta_extract, hash_video, notifier

#import requests... may not be present already
import requests

if __name__ == '__main__':
	base_url = 'http://api.thesubdb.com/'

	# Use meta_extract module... Part of this bundle
	dir_name = meta_extract.get_meta(sys.argv[1], 'dir')
	file_name = meta_extract.get_meta(sys.argv[1], 'file')
	exten = meta_extract.get_meta(sys.argv[1], 'ext')

	# Want subs in the same directory as the video files
	os.chdir(dir_name)

	# Unique hash created using the algorithm provided by thesubdb 
	hash_name = str(hash_video.get_hash(file_name+exten))

	# Change User-Agent
	headers = {'User-Agent': 'SubDB/1.0 (Sub-Downloader/1.0; htpp://github.com/bk2dcradle/Sub-Downloader)'}

	# Send a get request using requests
	resp = requests.get(base_url+'?action=download&hash='+hash_name+'&language=en', headers=headers)

	#print resp.status_code

	if str(resp.status_code) == '200':
		content = resp.text
		sub_name = open(file_name+'.srt', 'wb')
		sub_name.write(content.encode('ascii', 'ignore'))
		sub_name.close()
	elif str(resp.status_code) == '404':
		print "Snap! Video not found"
	else:
		print "Bad Request!!"
