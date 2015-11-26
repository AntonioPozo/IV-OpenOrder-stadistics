# -*- coding: utf-8 -*-
import dbm
import sys

db = dbm.open('usuariosBD', 'r')
try:
	print 'keys():', db.keys()
	for k in db.keys():
		print(k, '\t', db.get(k))
finally:
    db.close()