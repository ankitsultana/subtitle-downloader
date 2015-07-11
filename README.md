# Sub-Downloader for OS X

**Last Update on 10 July 2015:** Made creation of `services` automated. Now `install.sh` does it all.

A great way to download Subtitles in just 3 clicks. After installing it you will be able to do something like this:

    
      https://www.youtube.com/watch?v=liR8XFMTtA0&feature=youtu.be
    
## Installation (The noob way)
  1. Just go [here](http://bk2dcradle.github.io/Sub-Downloader) and follow the instructions.

## Installation (Using git)
  
  1. Clone this repo in your home directory, (copy-paste in terminal):
    
    ```
      cd ~ 
      git clone http://github.com/bk2dcradle/Sub-Downloader
    ```
    
  2. Run `install.sh` by copying and pasting the code below. This will install [requests](https://github.com/kennethreitz/requests.git) and create a OS X `Service`: 
  
     ```
      cd ~/Sub-Downloader
      chmod +x install.sh
      ./install.sh
     ```
    **OR if you want to do step 2 yourself**
     
     Install [requests](https://github.com/kennethreitz/requests.git) yourself, then create a `service` by following the instructions on [wiki](https://github.com/bk2dcradle/Sub-Downloader/wiki/Winding-up-by-creating-a-Service).
     
  3. Done! Now test if the script is working by checking on a movie file **OR** if that doesn't work, confirm by downloading [Sample File from here](http://thesubdb.com/api/samples/dexter.mp4) (Right-Click then Save Video As).
  **Note**: To download Subtitles you should be able to right click and then click on either `Services => Get Subtitles` or `Get Subtitles`.

## Files and their Roles
### 1. hash_video.py
  Contains the algorithm to create the hash value for the movie file. Taken directly from [thesubdb](http://thesubdb.com/)
  
### 2. install.sh
  Bash script to install [requests](https://github.com/kennethreitz/requests.git) and create a `Service`.
  
### 3. main_script.py
  This is the script that is called while running the service. Other python scripts act as modules.
  
### 4. meta_extract.py
  Extract file name, directory and extension.
  
### 5. notifier.py
  Doesn't work as of now, but fix coming soon!
