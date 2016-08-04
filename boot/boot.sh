#!/bin/bash
# This file exists for backwards compatibility with older versions of Jasper.
# It might be removed in future versions.
export LD_LIBRARY_PATH=/home/pi/xunfei/Linux_voice_1.109/libs/RaspberryPi:$LD_LIBRARY_PATH
sudo ldconfig

"${0%/*}/../jasper.py"
