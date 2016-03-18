# Sub-Downloader for OS X

**New in version 2:** Added notifications to prompt if Subtitles are downloaded or not.

A great way to download Subtitles in just 3 clicks. After installing it you will be able to do something like this:

![Screen Shot](https://raw.githubusercontent.com/bk2dcradle/Sub-Downloader/gh-pages/includes/images/SubDownloaderScreenShot.png)

## Installation

* Run the following command in terminal:

```bash
git clone https://github.com/bk2dcradle/subtitle-downloader.git ~/.utilities/subtitles-downloader --branch master --single-branch
```

* cp the `Get Subtitles.workflow` folder.

```bash
cp -r ~/.utilities/subtitle-downloader/Get\ Subtitles.workflow ~/Library/Services/
```

* Done! Now test if the script is working by checking on a movie file **OR** if that doesn't work, confirm by downloading [Sample File from here](http://thesubdb.com/api/samples/dexter.mp4) (Right-Click then Save Video As).


**Note**: To download Subtitles you should be able to right click and then click on either `Services => Get Subtitles` or `Get Subtitles`.

## Uninstall

subtitle-downloader only touches two directories, one is `~/.utilites/subtitle-downloader` and the other is `~/Library/Services`. To uninstall, do this:

```bash
rm -rf ~/.utilities/subtitle-downloader
rm -rf ~/Library/Services/Get\ Subtitles.workflow
```

###License

MIT. Copyright (c) [Ankit Sultana](http://twitter.com/AnkitSultana)
