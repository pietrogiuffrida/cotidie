#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
#import RPi.GPIO as GPIO
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


if __name__ == "__main__":

  logging.info("*"*20 + " NUOVA ESECUZIONE " + "*"*20)


  # ** * ** * ****  ** * ** * ****  ** * ** * ****  ** * ** * ****
  # Messaggi standard
  # ** * ** * ****  ** * ** * ****  ** * ** * ****  ** * ** * ****

  if reboot == True:
    for msg in msgs:

      if os.path.exists(msg):
        os.remove(msg)

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

  if os.path.exists(meteofile):
    os.remove(meteofile)

  if meteo == True:
    # 1 forecast
    status, previsioni_oggi = prevedi(forecast, now, delta=12)

    # 2 synthetize
    cmd = pico.format(meteofile).split()
    cmd.append(previsioni_oggi)
    status = run(cmd, testo="pico")
    if status != 0:
      os._exit(1)


  # ** * ** * ****  ** * ** * ****  ** * ** * ****  ** * ** * ****
  # Play
  # ** * ** * ****  ** * ** * ****  ** * ** * ****  ** * ** * ****

  msgs = list(msgs)
  msgs.append(meteofile)

  for msg in sorted(msgs):
    cmd = aplay.format(msg).split()
    status = run(cmd, testo="aplay")
    if status != 0:
      os._exit(1)
    sleep(.7)


  # ** * ** * ****  ** * ** * ****  ** * ** * ****  ** * ** * ****

  logging.info("*"*20 + " ESCO NORMALMENTE " + "*"*20)
