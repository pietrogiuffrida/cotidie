#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#https://home.openweathermap.org/api_keys
weather_key = "5ecc57e0157570e7f2e65e4979bf0ddb"
bologna = '6541998'
params = "&lang=it&units=metric"
baseweatherurl = "http://api.openweathermap.org/data/2.5"

weather = "{0}/weather?id={1}&appid={2}{3}".format(baseweatherurl, bologna, weather_key, params)
forecast = "{0}/forecast?id={1}&appid={2}{3}".format(baseweatherurl, bologna, weather_key, params)

pico = "pico2wave -l=it-IT -w={}"
aplay = "aplay -s15 {}"

aplay = "play {} tempo 1.3"

meteofile = 'messages/99_meteo.wav'

reboot = True
mattino = {
  'messages/01.wav': "Buongiorno!",
  'messages/02_a.wav': "Alice, hai preso le chiavi?",
  'messages/02_bus.wav': "Pietro, hai preso il biglietto dell'autobus?",
  'messages/03_fra.wav': "Francesco, ti sei messo il giubotto e il cappello?",
  'messages/05_mad.wav': "Ciao Maddi! Hai preso il termos e il pranzo?",
  }

pomeriggio = {
  'messages/01.wav': "Buontornati!",
  'messages/03_fra.wav': "Francesco, com'è andata a scuola?",
  'messages/05_mad.wav': "Ciao Lucìa Antonella! Tutto bene? Che si dice?",
  }

nonna = {
  'messages/01.wav': "Ciao nonna Enza! Sono tornati quei mostri dei tuoi nipoti!",
  'messages/02.wav': "Cantami o diva, del pelide achille, l'ira funesta, che infiniti addusse lutti agli achei, molte anzitempo all'orco generose travolse alme d'eroi",
  }



msgs = mattino
meteo = True
