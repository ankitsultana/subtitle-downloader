# Sub-Downloader for OS X

**New in version 2:** Added notifications to prompt if Subtitles are downloaded or not.

A great way to download Subtitles in just 3 clicks. After installing it you will be able to do something like this:

![Screen Shot](https://raw.githubusercontent.com/bk2dcradle/Sub-Downloader/gh-pages/includes/images/SubDownloaderScreenShot.png)
    
## Installation 
  1. First clone this repo in your **home directory**. To do that, do this in terminal:
         
        cd ~
        git clone https://github.com/bk2dcradle/Sub-Downloader.git
  
  2. Move the `Get Subtitles.workflow` folder.
  
        mv ~/Sub-Downloader/Get\ Subtitles.workflow ~/Library/Services/
  
  3. Done! Now test if the script is working by checking on a movie file **OR** if that doesn't work, confirm by downloading [Sample File from here](http://thesubdb.com/api/samples/dexter.mp4) (Right-Click then Save Video As).
  **Note**: To download Subtitles you should be able to right click and then click on either `Services => Get Subtitles` or `Get Subtitles`.

## Uninstall

Sub-Downloader only creates two directories, one is, `~/Sub-Downloader` and the other is `~/Library/Services/Get\ Subtitles.workflow`. Just remove both of them, and you are done!

```bash
rm -rf ~/Sub-Downloader
rm -rf ~/Library/Services/Get\ Subtitles.workflow
```

###License

MIT. Copyright (c) [Ankit Sultana](http://twitter.com/AnkitSultana)
