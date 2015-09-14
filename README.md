# Sub-Downloader for OS X

**Last Update on 14 September 2015:** Removed requests, made installation really easy.

A great way to download Subtitles in just 3 clicks. After installing it you will be able to do something like this:

    
      https://www.youtube.com/watch?v=liR8XFMTtA0&feature=youtu.be
    
## Installation 
  1. First clone this repo in your **home directory**.
         
            cd ~
            git clone https://github.com/bk2dcradle/Sub-Downloader.git
  
  2. Move the `Get Subtitles.workflow` folder.
  
            mv ~/Sub-Downloader/Get\ Subtitles.workflow ~/Library/Services/
  
  3. Done! Now test if the script is working by checking on a movie file **OR** if that doesn't work, confirm by downloading [Sample File from here](http://thesubdb.com/api/samples/dexter.mp4) (Right-Click then Save Video As).
  **Note**: To download Subtitles you should be able to right click and then click on either `Services => Get Subtitles` or `Get Subtitles`.

## Files and their Roles
### 1. hash_video.py
  Contains the algorithm to create the hash value for the movie file. Taken directly from [thesubdb](http://thesubdb.com/)
  
### 2. main_script.py
  This is the script that is called while running the service. Other python scripts act as modules.
  
### 3. meta_extract.py
  Extract file name, directory and extension.
