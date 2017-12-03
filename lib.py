#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
import subprocess
import logging
import requests


def parseDates(diz, k):
  diz[k] = datetime.fromtimestamp(diz[k])
  return diz


def run(cmd, testo=""):
  logging.debug('Processo {0} {1}'.format(testo, cmd))
  p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  p.communicate()
  if p.returncode != 0:
    logging.error('Stderr {}'.format(p.stderr))
    logging.error('Stdout {}'.format(p.stdout))
    logging.error('Cmd {0} {1}'.format(testo, cmd))
    return 1
  return 0


def prevedi(url, now, delta):

  logging.debug('Previsioni {}'.format(url))
  txt_oggi = "Previsioni: {0}. Temperatura minima {1}, massima {2}"
  r = requests.get(url)
  if r.status_code != 200:
    logging.error('Impossibile connettersi')
    return 1, ""

  previsioni = r.json()
  previsioni = [i for i in previsioni['list']]
  previsioni = [parseDates(i, 'dt') for i in previsioni]
  previsioni = [i for i in previsioni if i['dt'] < now + timedelta(hours=delta)]
  minima = min([i['main']['temp_min'] for i in previsioni])
  minima = round(minima, 1)
  massima = max([i['main']['temp_max'] for i in previsioni])
  massima = round(massima, 1)

  condizioni = []
  for d in [i['weather'] for i in previsioni]:
    for j in d:
      if j['description'] not in condizioni:
        condizioni.append(j['description'])
  condizioni = ', '.join(condizioni)
  return 0, txt_oggi.format(condizioni, minima, massima)
