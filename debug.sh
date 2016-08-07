#!/bin/bash

export LD_LIBRARY_PATH=/home/pi/xunfei/Linux_voice_1.109/libs/RaspberryPi:$LD_LIBRARY_PATH
sudo ldconfig

python /home/pi/jasper-client/jasper.py --debug
