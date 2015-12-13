# Logs stored in script.log
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.FileHandler('script.log')
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)

import sys

logger.info(sys.version)

logger.info('Trying Imports')

PythonVersion = sys.version_info[0]

import os
logger.info('Imported os')

sys.dont_write_bytecode = True  # Who likes pyc files

# Import custom modules
try:
    import meta_extract, hash_video, notify
    logger.info('Imported meta_extract, hash_video')
except ImportError, e:
    logger.error('Cannot Import Custom modules')

try:
    logger.info("Trying to import urllib")
    if PythonVersion == 2:
        import urllib2
        logger.info("PythonVersion == 2: Importing urllib2: ")
    elif PythonVersion == 3:
        import urllib.request
        logger.info("PythonVersion == 3: Importing urllib.request")
except Exception, e:
    logger.error("Cannot Import urllib")
    logger.exception(e)

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

    full_url = base_url+'?action=download&hash='+hash_name+'&language=en'
    status_code = '404'
    # Send a get request
    try:
        if PythonVersion == 3:
            req = urllib.request.Request(full_url, None, headers)
            response = urllib.request.urlopen(req)
            status_code = response.getcode()
        elif PythonVersion == 2:
            req = urllib2.Request(full_url, '', headers)
            response = urllib2.urlopen(req)
            status_code = response.getcode()
    except Exception, e:
        logger.error("Error occured while trying to fetch subtitles")

    logger.info(status_code)

    if str(status_code) == '200':
        logger.info('Subtitles Fetched')
        content = response.read()
        sub_name = open(file_name+'.srt', 'wb')
        try:
            sub_name.write(content.encode('ascii', 'ignore'))
            notify.notify("Sub-Downloader: Success!", "Subtitles Found", "The subtitles are stored in a file named " + file_name + ".srt", delay=1, sound=True)
        except Exception, e:
            logger.exception(e)
            sub_name.write(content)
        sub_name.close()
    elif str(status_code) == '404':
        notify.notify("Sub-Downloader: Error!", "Subtitle Not Found", "The subtitles for this file are not available in the database", delay=1, sound=True)
        logger.error('Subtitles not available in Database')
    else:
        logger.error('Bad Request!')
    logger.info('============================')
