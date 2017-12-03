#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

def parseDates(diz, k):
  diz[k] = datetime.fromtimestamp(diz[k])
  return diz
