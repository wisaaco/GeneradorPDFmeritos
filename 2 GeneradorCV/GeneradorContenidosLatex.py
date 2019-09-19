#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 16:18:20 2019

@author: isaaclera
"""

#creating structure latex

import os
import codecs
import unicodedata
import re
from shutil import copyfile


localPath = "temp"
fileID = 0

def toLatex(f,text):
    f.write(text+"\n"+"\\newpage")

def includePDF(f,pdf):
    toLatex(f,"\includepdf[pages=-,pagecommand={}]{%s}"%pdf)

root = "../1 OrganizacionCV"
f = open("content.tex",'w')
    
for path, subdirs, files in sorted(os.walk(root)):
    print path
    lastDir =  os.path.basename(os.path.normpath(path))
    ##
    # Atención: la codificación del nombre del path está testeado sobre OS High Sierra y Windows 10
    ###
    #MAC/Windows filenames coding
    lastDir = unicodedata.normalize('NFC', unicode(lastDir, 'utf-8')).encode('utf-8')
    me =  re.search('[a-zA-Z]',lastDir)
    lastDir  =  lastDir[lastDir.find(me.group()):]

    level = path.count("/")-2
    if level>=0:
        t1 = "\\"+"sub"*level+"section{%s}"%lastDir
        
        toLatex(f,t1)
        for name in files:
            if name.endswith(".pdf"): 
                filepath = path+"/"+name
                print os.path.join(path, name)
                copyfile(os.path.join(path, name), "temp/%i.pdf"%fileID)
                includePDF(f,"temp/%i.pdf"%fileID)
                fileID+=1
        
f.close()    
