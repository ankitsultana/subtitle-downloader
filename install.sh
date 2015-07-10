# Download and install requests (module for python)
# If you know your way around git, Install it yourself.
# 	Here is the url: https://github.com/kennethreitz/requests.git
# Else run this in terminal using instructions in README.md

cd ~/Sub-Downloader

touch logs.txt

# If requests not installed... install it
python -c "import requests" &> logs.txt

if [ $? -eq 0 ]; then
	echo "Requests is installed" >> logs.txt
else
	echo "Requests not installed" >> logs.txt
	echo "You don't have Requests already installed, Do you want to install it?(y/n)"
	echo "(Necessary for using Sub-Downloader)"
	read X
	
	if [ $X = 'y' ]; then
		for i in `seq 1 3`; do
			echo '.'
			sleep 1
		done
		cd ~
		git clone git://github.com/kennethreitz/requests.git
		cd ~/requests
		sudo python setup.py install
		cd ~/Sub-Downloader
	else
		echo "You chose to not install requests. Run this script again if you ever want to install it."
	fi
fi

echo "Moving Get Subtitles.workflow" >> logs.txt
mv "~/Sub-Downloader/Get Subtitles.workflow" "~/Library/Services/"
