#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import requests
import RPi.GPIO as GPIO
import subprocess
import logging
from config import *
from lib import *

logging.basicConfig(
  format='%(asctime)s\t%(levelname)s\t%(message)s',
  filename="cotidie.log",
  level=logging.INFO,
  #level=logging.DEBUG,
  )

logging.info("*"*20 + " NUOVA ESECUZIONE " + "*"*20)

r = requests.get(forecast)
if r.status_code != 200:
  os._exit(1)

now = datetime.now()
previsioni = r.json()
previsioni = [i for i in previsioni['list']]
previsioni = [parseDates(i, 'dt') for i in previsioni]
previsioni = [i for i in previsioni if i['dt'] < now + timedelta(hours=12)]
minima = min([i['main']['temp_min'] for i in previsioni])
massima = min([i['main']['temp_max'] for i in previsioni])
condizioni = set()
for d in [i['weather'] for i in previsioni]:
  for j in d:
    condizioni.add(j['description'])
condizioni = 'e '.join(condizioni)

oggi = txt_oggi.format(condizioni, minima, massima)
cmd = pico.format(oggi)

subprocess.Popen(cmd)

logging.info("*"*20 + " ESimport RPi.GPIO as GPIO
