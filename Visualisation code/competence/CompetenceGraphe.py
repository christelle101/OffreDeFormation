import tabula
import webbrowser as w
from textReader import text, list_Module_court

from competenceExtractor import df, competence_spe_info
from pyvis.network import Network

text = text
p_competence = df["UE"]
# i create a network
net = Network(height='100%', width='100%', bgcolor='#222222', font_color='white')


# the list of subject in the coursework
def list_module_plus_id():
    subjects = list_Module_court(text)
    liste = []
    compteur = 0
    for subject in subjects:
        liste.append((compteur, subject))
        compteur += 1
    return liste


def get_module_id(module):
    subjects = list_module_plus_id()
    for node in subjects:
        if module == node[1]:
            return node[0]


# add nodes
liste_subjects = list_module_plus_id()
for node in liste_subjects:
    net.add_node(node[0], label=node[1])

# skill nodes
net.add_node(100, size=50, label="IDU", color="#00ff1e")
net.add_node(200, size=50, label="TC", color="#00ff1e")


# add skill information
def list_skill_info():
    skill_info = competence_spe_info()
    compteur = 500
    liste = list()
    for items in skill_info.items():
        for item in items[1]:
            liste.append((compteur, item))
            compteur += 1
    return liste


def get_skill_id(p_skill):
    skills = list_skill_info()
    for skill in skills:
        if skill[1] == p_skill:
            return skill[0]


# test
# print(list_skill_info())
for skll in list_skill_info():
    if skll[1][0] == "I":
        net.add_node(skll[0], size=25, label=skll[1], color="#EAEBE3")
        net.add_edge(skll[0], 100, weight=1)
    elif skll[1][0] == "T":
        net.add_node(skll[0], size=25, label=skll[1], color="#EAEBE3")
        net.add_edge(skll[0], 200, weight=1)


import edgecompetence
net.show("prerequis.html")
# w.open("prerequis.html")
print("ok")
