#! /usr/bin/env python
# -*- coding: utf-8 -*-

import urllib, json
from pprint import pprint

def imdbInfo(filmnavn, mode):
   ting = filmnavn
   ting2 = ting[6:]
   if ('the room' == ting2.strip()):
      return ('Filmen \"The Room\" fra 2003 har scoren 3.3. Scoren burde vært lavere.')
   json_data= urllib.urlopen('http://www.imdbapi.com/?t=' + ting2)

   data = json.load(json_data)
   pprint(data)
   json_data.close()

   try:
      if (mode == 'score'):
         return('Filmen ' + data["Title"] + ' fra ' + data["Year"] + ' har scoren ' + data["imdbRating"])
      elif (mode == 'plot'):
         return(data["Title"] + ": " + data["Plot"])
   except:
      return('Fant ikke film.')

def filmScore(filmen):
   score = ['Verste filmen ever!', 'FILMEN SUGER!!!', 'Veldig dårlig film!', 'OK film da...', 'Grei film..', 'Ganske bra film :)', 'Bra film ass!! :D', 'VELDIG BRA FILM!!!', 'En av de beste filmene jeg har sett! :O']
   return(score[imdben(filmen)-1])
