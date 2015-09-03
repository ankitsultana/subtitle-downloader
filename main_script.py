# Logs stored in script.log
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('script.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info('Trying Imports')

try:
    import sys, os, re
    logger.info('Imported sys, os and re')
except ImportError, e:
    logger.error('Cannot Import sys, os or re')

sys.dont_write_bytecode = True	# Who likes pyc files

# Import custom modules
try:
    import meta_extract, hash_video
    logger.info('Imported meta_extract, hash_video')
except ImportError, e:
    logger.error('Cannot Import Custom modules')

# Import requests... may not be present already
try:
    import requests
    logger.info('Imported requests')
except ImportError, e:
    logger.error('Cannot Import Requests')

if __name__ == '__main__':
	base_url = 'http://api.thesubdb.com/'

	# Use meta_extract module... Part of this bundle
        logger.info('Extracting Meta Data from File Name')
        try:
            dir_name = meta_extract.get_meta(sys.argv[1], 'dir')
            file_name = meta_extract.get_meta(sys.argv[1], 'file')
            exten = meta_extract.get_meta(sys.argv[1], 'ext')
            logger.info("File Name: " + file_name)
            logger.info("Directory: " + dir_name)
            logger.info("Extension: " + exten)
            logger.info('Extracted Meta Data')
        except Exception, e:
            logger.exception(e)

	# Want subs in the same directory as the video files
        try:
	    os.chdir(dir_name)
        except Exception, e:
            logger.error('Cannot Change Directory')
            logger.exception(e)

	# Unique hash created using the algorithm provided by thesubdb 
	hash_name = str(hash_video.get_hash(file_name+exten))

	# Change User-Agent
	headers = {'User-Agent': 'SubDB/1.0 (Sub-Downloader/1.0; http://www.github.com/bk2dcradle/Sub-Downloader)'}

	# Send a get request using requests
	resp = requests.get(base_url+'?action=download&hash='+hash_name+'&language=en', headers=headers)

        logger.info(resp.status_code)

	if str(resp.status_code) == '200':
            logger.info('Subtitles Fetched')
            content = resp.text
            sub_name = open(file_name+'.srt', 'wb')
            sub_name.write(content.encode('ascii', 'ignore'))
            sub_name.close()
	elif str(resp.status_code) == '404':
            logger.error('Subtitles not available in Database')
	else:
            logger.error('Bad Request!')

        logger.info('\n')
