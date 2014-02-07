#!/usr/bin/python
import os, re
from os import rename
for filename in os.listdir("."):
    if filename.endswith('png'):
        pieces = filename.split('_')
        if len(pieces[4]) == 1:
            pieces[4] = '0' + pieces[4]
            rename(filename, '_'.join(pieces))
        months = { "January" : "01",
                    "February" : "02",
                    "March" : "03",
                    "April" : "04",
                    "May" : "05",
                    "June" : "06",
                    "July" : "07",
                    "August" : "08",
                    "Septempber" : "09",
                    "October" : "10",
                    "November" : "11",
                    "December" : "12",
        }
        if pieces[3] in months:
            pieces[3] = months[pieces[3]]
            rename(filename, '_'.join(pieces))
            
