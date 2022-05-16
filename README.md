# InternetSpeedTest
needed a simple script to track my internet speed and
track when my ISP does maintenance.

to use, install the modules in the "requirements.txt" 
folder by going into the main directory where the 
files are and typing in:
pip install -r requirements.txt
into the terminal.

i took it a step forward and made this script run every
30 minutes via crontab.
to do so, open up a terminal again and enter:

crontab -e
30 * * * * cd InternetSpeedTest && python InternetSpeedTest.py

SAVE AND EXIT

sudo chmod +x InternetSpeedTest.py
sudo reboot
