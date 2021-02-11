# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:13:51 2021

@author: Junio
"""
from sqlalchemy import create_engine, MetaData, Table, Column, String, ForeignKey
import textReader as t
donnee = create_engine("sqlite:///test4.csv", echo = True)

meta = MetaData()

# table

Semestre = Table(
    'Semestre', meta,
    Column('nomSemestre', String, primary_key = True)
    )

UE = Table(
    'UE', meta,
    Column('nomUE', String, primary_key = True),
    Column('nomSemestre', String, ForeignKey('Semestre.nomSemestre'))
    )

Module = Table(
    'Module', meta,
    Column('nomModule', String, primary_key=True),
    Column('competence', String),
    Column('nomUE', String, ForeignKey('UE.nomUE'))
    )

Prerequis = Table(
    'Prerequis', meta,
    Column('nomModule', String, ForeignKey('Module.nomModule')),
    Column('nomModule_prerequis', String, ForeignKey('Module.nomModule'))
    )

meta.create_all(donnee)
#####################################################################
conn = donnee.connect()
# insertion dans semestre
text = t.text
semestre_UE = t.semestre_UE(text)
UE_module = t.UE_module(text)
#
liste_semestre = []
for semestre in semestre_UE.items():
    #liste_semestre.append({'Semestre':semestre[0]})
    sem = Semestre.insert().values(nomSemestre= semestre[0])
    conn.execute(sem)
#
liste_UE = []
for termes in semestre_UE.items(): 
    for ue in termes[1]:
        #liste_UE.append({'nomUE':ue,'nomSemestre':termes[0]})
        ue_p = UE.insert().values(nomUE = ue,nomSemestre = termes[0])
        conn.execute(ue_p)

#
UE_modules = t.UE_module(text)
liste_module = []
for modules in UE_modules.items():
    for module in modules[1]:
        consequence = t.attributModule(module, text)[1]
        #liste_module.append({'nomModule':module,'consequence':consequence,'nomUE':modules[0]})
        mod = Module.insert().values(nomModule = module,competence = consequence,nomUE = modules[0])
        conn.execute(mod)
#
relations = t.relation_entre_matiere(text)
liste_rel =[]
for relation in relations.items():
    for prerequis in relation[1]:
        #liste_rel.append({'nomModule':relation[0],'nomModule_prerequis':prerequis})
        pre = Prerequis.insert().values(nomModule = relation[0],nomModule_prerequis = prerequis)
        conn.execute(pre)
#

# conn.execute(sem,liste_semestre)
# conn.execute(ue_p,liste_UE)
# conn.execute(mod,liste_module)
# conn.execute(pre, liste_rel)

