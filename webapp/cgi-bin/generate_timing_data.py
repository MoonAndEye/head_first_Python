# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 23:53:48 2016

@author: Moon
"""

import cgi
import athletemodel
import yate
import glob

form_data = cgi.FieldStorage()
athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Best time data"))

print(yate.para("Time data for " + athlete_name.name))

