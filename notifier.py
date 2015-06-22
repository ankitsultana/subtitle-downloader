import os

def notify(message):
	t = ' -title SubDownloader'
	m = '-message '+message
	os.system('terminal-notifier '+m+t)
