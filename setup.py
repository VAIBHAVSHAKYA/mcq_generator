# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:23:07 2022

@author: SUDHA-RAJESH
"""
from pprint import pprint
import main

qg = main.QGen()

txt=inp['i am vaibhav']

output = qg.predict_mcq(payload,txt)
print (output)
