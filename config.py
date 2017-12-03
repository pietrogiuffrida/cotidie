#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#https://home.openweathermap.org/api_keys
weather_key = "5ecc57e0157570e7f2e65e4979bf0ddb"
bologna = '6541998'
params = "&lang=it&units=metric"
baseweatherurl = "http://api.openweathermap.org/data/2.5"
txt_oggi = "Previsioni: {0}, temperatura minima {1}, massima {2}"

weather = "{0}/weather?id={1}&appid={2}{3}".format(baseweatherurl, bologna, weather_key, params)
forecast = "{0}/forecast?id={1}&appid={2}{3}".format(baseweatherurl, bologna, weather_key, params)

pico = "pico2wave -l=it-IT -w=/tmp/test.wav '{}';aplay /tmp/test.wav;rm /tmp/test.wav"
