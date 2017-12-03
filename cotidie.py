#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import requests
import RPi.GPIO as GPIO
import subprocess
import logging
import os
from time import sleep
from config import *
from lib import *


logging.basicConfig(
  format='%(asctime)s\t%(levelname)s\t%(message)s',
  filename="cotidie.log",
  level=logging.INFO,
  #level=logging.DEBUG,
  )

logging.info("*"*20 + " NUOVA ESECUZIONE " + "*"*20)


# ** * ** * ****  ** * ** * ****  ** * ** * ****  ** * ** * ****
# Messaggi standard
# ** * ** * ****  ** * ** * ****  ** * ** * ****  ** * ** * ****

if reboot == True:
  for msg in msgs:
    # 2 synthetize
    cmd = pico.format(msg).split()
    cmd.append(msgs[msg])
    status = run(cmd, testo="pico")
    if status != 0:
      os._exit(1)


# ** * ** * ****  ** * ** * ****  ** * ** * ****  ** * ** * ****
# Messaggi meteo
# ** * ** * ****  ** * ** * ****  ** * ** * ****  ** * ** * ****

now = datetime.now()

# 1 forecast
status, previsioni_oggi = prevedi(forecast, delta=12)

if os.path.exists(metofile):
  os.remove(metofile)

# 2 synthetize
cmd = pico.format(metofile).split()
cmd.append(previsioni_oggi)
status = run(cmd, testo="pico")
if status != 0:
  os._exit(1)


# ** * ** * ****  ** * ** * ****  ** * ** * ****  ** * ** * ****
# Play
# ** * ** * ****  ** * ** * ****  ** * ** * ****  ** * ** * ****

for msg in list(msgs) + [meteofile]:
  cmd = aplay.format(msg).split()
  status = run(cmd, testo="aplay")
  if status != 0:
    os._exit(1)
  sleep(1.5)

## 4 remove
#cmd = remove.format(filename).split()
#status = run(cmd, testo="remove")
#if status != 0:
  #os._exit(1)


# ** * ** * ****  ** * ** * ****  ** * ** * ****  ** * ** * ****

logging.info("*"*20 + " ESCO NORMALMENTE " + "*"*20)
