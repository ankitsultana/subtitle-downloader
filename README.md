# Sub-Downloader for OS X 

**Last Update:** Made creation of `services` automated. Now it `install.sh` does it all.

A great way to download Subtitles in just 3 clicks. After installing it you will be able to do something like this:

    
      https://www.youtube.com/watch?v=liR8XFMTtA0&feature=youtu.be
    

## Installation
  
  1. Clone this repo in your home directory, (copy-paste in terminal):
    
    ```
      cd ~ 
      git clone http://github.com/bk2dcradle/Sub-Downloader
    ```
    
  2. Install [requests](https://github.com/kennethreitz/requests.git) for python either by running the ```install.sh``` script or do it yourself. **In the latter case you don't need to run** ```install.sh```.
     To run ```install.sh``` simply copy-paste this in terminal:
     ```
      cd ~/Sub-Downloader
      chmod +x install.sh
      ./install.sh
     ```
  3. Finally create a ```service``` in ```Automator```. Its really painless. Head over to the [wiki](https://github.com/bk2dcradle/Sub-Downloader/wiki/Winding-up-by-creating-a-Service):

## Files and their Roles
### 1. hash_video.py
  Contains the algorithm to create the hash value for the movie file. Taken directly from [thesubdb](http://thesubdb.com/)
  
### 2. install.sh
  Bash script to install [requests](https://github.com/kennethreitz/requests.git). You can install it yourself, or in case you already have it installed, you don't need to run this.
  
### 3. main_script.py
  This is the script that is called while running the service. Other python scripts act as modules.
  
### 4. meta_extract.py
  Extract file name, directory and extension.
  
### 5. notifier.py
  Doesn't work as of now, but fix coming soon!
