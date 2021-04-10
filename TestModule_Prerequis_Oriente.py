# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 08:17:29 2021

@author: yawoumi

Graphe Modules-Prérequis
"""

from graphviz import Digraph
import pandas as pd

#Fonction qui crée des noeuds dans un graphe avec une couleur spécifique
#selon le semestre
def Nodes_Semestres(G,module,NumSem):
    if(NumSem == 5): couleur = 'palegreen'
    if(NumSem == 6): couleur = 'paleturquoise'
    if(NumSem == 7): couleur = 'papayawhip'
    if(NumSem == 8): couleur = 'snow2'
    if(NumSem == 9): couleur = 'sandybrown'
    
    if((int(module[4]) == NumSem)):
        G.node(module, title=module, color = couleur, style='filled')

    
#Création de mon graphe
G = Digraph(comment='Graphe Module-Prerequis')

#Récupération de mes données de mon fichier excel
prerequis_data = pd.read_csv("Module_Prerequis.csv", sep=';')

#Ensemble des modules prerequis
sources = prerequis_data['Source'] 
#Ensemble des modules filles
targets = prerequis_data['Target']

edge_data = zip(sources, targets)

for e in edge_data:
    src = e[0]
    dst = e[1]

    #Ajout des noeuds:
    #Si semestre 5
    Nodes_Semestres(G,src,5)
    Nodes_Semestres(G,dst,5)
    
    #Si semestre 6
    Nodes_Semestres(G,src,6)
    Nodes_Semestres(G,dst,6)
    
    #Si semestre 7
    Nodes_Semestres(G,src,7)
    Nodes_Semestres(G,dst,7)
    
    #Si semestre 8
    Nodes_Semestres(G,src,8)
    Nodes_Semestres(G,dst,8)
    
    #Si semestre 9
    Nodes_Semestres(G,src,9)
    Nodes_Semestres(G,dst,9)
    
    #Ajout des arcs:
    G.edge(src, dst)

#On génére un fichier de type png du graphe obtenu
G.format = 'png'
G.render('GraphTest', view = True)

