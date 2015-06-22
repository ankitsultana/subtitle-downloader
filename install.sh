# Download and install
#		1. requests
			#	git clone git://github.com/kennethreitz/requests.git
			# python setup.py install
#		2. terminal-notifier
			# brew install terminal-notifier
#	Set home_dir

touch logs.txt
brew help > logs.txt
if [ -s logs.txt ]; then
	echo "File there"
else
	echo "File not there"
	# ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
fi

# If requests not installed... install it
python -c "import requests" &> logs.txt

if [ $? -eq 0 ]; then
	echo "Requests is installed" >> logs.txt
else
	echo "Requests not installed, Installing" >> logs.txt
	for i in 1..3; do
		echo '.'
		sleep 1
	done
	#cd ~
	#git clone git://github.com/kennethreitz/requests.git
	#python setup.py install
fi

# If terminal-notifier not installed... install it
terminal-notifier -help >> logs.txt

if [ $? -eq 0 ]; then
	echo "terminal-notifier already installed!" >> logs.txt
else
	echo "install terminal" >> logs.txt
	#brew install terminal-notifier
fi
