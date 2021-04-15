# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 08:22:13 2021

@author: Junio
"""
#Import
import requests 
from bs4 import BeautifulSoup
import re

# Expressrion reguliere
'(\s|\w|\-)*(TC|IDU)+'
'^(Semestre)[\-\ [0-9]*]*'
'((UE)s[\-\ [0-9]*])'

# print('--Beginning...\n')
# Entrer le site internet
url = 'http://ead-polytech.univ-savoie.fr/'

# Ouvrir le site internet
getUrl = requests.get(url)

# Parser
# print('--start parsing...\n')
TextGetUrl = BeautifulSoup(getUrl.text, 'html.parser')
#print(TextGetUrl)

# data
specialite = {}
data = {}

# recherche des balises <a>
textA = TextGetUrl.find_all('a')
for text in textA:
    #print(text)
    m = re.search(r'((\s|\w|\-)*(TC|IDU))', str(text))
    r = re.findall(r'((\s|\w|\-)*(TC|IDU))', str(text))
    #print(m)
    if m is not None:
        data.update({str(r[0][0]):text})
        
# traité les repetitions
copyData = data.copy()
listeValues = []
for values in copyData.items():
    if values[0] not in listeValues:
        listeValues.append(values[0])
    else : data.pop(values[0])

# EXTRACTING DATA
donneeS = {} # donnee brute
for ue in data.items():
    if 'UE' in ue[0]:
        ue_value = str(data.get(ue[0]))
        split1 = ue_value.split(' ')[2]
        split2 = split1.split('"')[1]
        module = split2.split(',')
        donneeS.update({ue[0]:module})

#UE
UE = {}
for dataS in donneeS.items():
    #ce sont les initiales de semestre ue competence
    suecom = dataS[0].split('-')
    ue = suecom[1]
    # ue : matiere semestre competence
    UE.update({ue:[dataS[1], suecom[0], suecom[2]]})
print(UE)
# MODULE
# print('--extraction des modules...\n')
Module = list()
for m in donneeS.items():
    for mod in m[1]:
        Module.append(mod)
# print('--extraction des modules terminée--')

# SEMESTRE
semestre = {}