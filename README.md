# naoyas

# Libraries

To install required libraries,
$ pip install -r requirements.txt
.
And,
$ pip install git+https://github.com/AmbientDataInc/ambient-python-lib.git
.

# Log Directory
Please create /home/pi/naoyas_log directory.
$ cd
$ mkdir naoyas_log

# CRON
Add this line by using crontab -e

@reboot /home/pi/naoyas/venv392/bin/python3 /home/pi/naoyas/src/naoyas.py 1> /home/pi/naoyas_log/naoyas01-`date +\%Y\%m\%d-\%H\%M\%S`.log 2> /home/pi/naoyas_log/naoyas01_err-`date +\%Y\%m\%d-\%H\%M\%S`.log &



