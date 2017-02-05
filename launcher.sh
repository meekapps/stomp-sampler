#!/bin/sh
# launcher.sh
# execute sampler_sampler.py on startup
#
# to install:
# go to root directory: cd
# create logs directory: mkdir logs
# open crontab: sudo crontab -e
# add script to crontab by adding the following line:
# @reboot sh /home/pi/projects/stomp-sampler/launcher.sh >/home/pi/logs/cronlog 2>&1


cd /home/pi/projects/stomp-sampler
sudo python stomp_sampler.py
cd /
