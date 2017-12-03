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
aplay = "aplay -r 10000 {}"

meteofile = 'messages/99_meteo.wav'

reboot = True
msgs = {
  'messages/01.wav': "Buongiorno!",
  'messages/02_bus.wav': "Pietro, hai preso il biglietto dell'autobus?",
  'messages/03_fra.wav': "Francesco, ti sei messo il giubotto?",
  'messages/04_ali.wav': "Alice, hai preso la testa?",
  'messages/05_mad.wav': "Ciao Maddi!",
  }
