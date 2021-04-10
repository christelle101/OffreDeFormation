import tabula
import textReader as t
import webbrowser as w
import competenceExtractor as c
from pyvis.network import Network

text = t.text
df = tabula.read_pdf('Referentiel_Competences_IDU_2021_2025.pdf', pages='all')[2]
p_competence = df["UE"]

# i create a network
net = Network(height='100%', width='100%', bgcolor='#222222', font_color='white')


# the list of subject in the coursework
def list_module_plus_id():
    subjects = t.list_Module_court(text)
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
    skill_info = c.competence_spe_info()
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

# set edges
net.add_edge(get_module_id("LANG501a"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("LANG501a"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("LANG501a"), get_skill_id("TC-3.3"), weight=1)

net.add_edge(get_module_id("SHES501a"), get_skill_id("TC-1.1"), weight=1)
net.add_edge(get_module_id("SHES501a"), get_skill_id("TC-1.2"), weight=1)
net.add_edge(get_module_id("SHES501a"), get_skill_id("TC-1.5"), weight=1)
net.add_edge(get_module_id("SHES501a"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("SHES501a"), get_skill_id("TC-2.3"), weight=1)
"""
net.add_edge(get_module_id("SHES505"), get_skill_id("TC-1.1"), weight=1)
net.add_edge(get_module_id("SHES505"), get_skill_id("TC-1.2"), weight=1)
net.add_edge(get_module_id("SHES505"), get_skill_id("TC-1.4"), weight=1)
net.add_edge(get_module_id("SHES505"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("SHES505"), get_skill_id("TC-4.1"), weight=1)
net.add_edge(get_module_id("SHES505"), get_skill_id("TC-4.3"), weight=1)
net.add_edge(get_module_id("SHES505"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("SHES505"), get_skill_id("TC-3.1"), weight=1)
net.add_edge(get_module_id("SHES505"), get_skill_id("TC-3.3"), weight=1)

net.add_edge(get_module_id("DDRS501"), get_skill_id("IDU-3.2"), weight=1)
net.add_edge(get_module_id("DDRS501"), get_skill_id("TC-1.1"), weight=1)
net.add_edge(get_module_id("DDRS501"), get_skill_id("TC-3.1"), weight=1)
net.add_edge(get_module_id("DDRS501"), get_skill_id("TC-3.2"), weight=1)
net.add_edge(get_module_id("DDRS501"), get_skill_id("TC-3.3"), weight=1)
net.add_edge(get_module_id("DDRS501"), get_skill_id("TC-3.4"), weight=1)

net.add_edge(get_module_id("EASI501a"), get_skill_id("IDU-3.2"), weight=1)

net.add_edge(get_module_id("INFO501a"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("INFO501a"), get_skill_id("IDU-1.2"), weight=1)
net.add_edge(get_module_id("INFO501a"), get_skill_id("TC-1.3"), weight=1)

net.add_edge(get_module_id("INFO502a"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("INFO502a"), get_skill_id("IDU-2.2"), weight=1)
net.add_edge(get_module_id("INFO502a"), get_skill_id("IDU-2.3"), weight=1)

net.add_edge(get_module_id("MATH500a"), get_skill_id("IDU-2.3"), weight=1)
net.add_edge(get_module_id("MATH500a"), get_skill_id("TC-1.3"), weight=1)

net.add_edge(get_module_id("MATH501a"), get_skill_id("IDU-2.3"), weight=1)
net.add_edge(get_module_id("MATH501a"), get_skill_id("TC-1.3"), weight=1)

net.add_edge(get_module_id("EASI541b"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("EASI541b"), get_skill_id("IDU-4.1"), weight=1)

net.add_edge(get_module_id("ISOC531"), get_skill_id("IDU-3.1"), weight=1)
net.add_edge(get_module_id("ISOC531"), get_skill_id("TC-1.4"), weight=1)
net.add_edge(get_module_id("ISOC531"), get_skill_id("TC-1.5"), weight=1)
net.add_edge(get_module_id("ISOC531"), get_skill_id("TC-2.2"), weight=1)
net.add_edge(get_module_id("ISOC531"), get_skill_id("TC-2.2"), weight=1)

net.add_edge(get_module_id("MATH531"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("MATH531"), get_skill_id("IDU-1.2"), weight=1)

net.add_edge(get_module_id("PROJ531"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("PROJ531"), get_skill_id("TC-1.4"), weight=1)
net.add_edge(get_module_id("PROJ531"), get_skill_id("TC-3.2"), weight=1)
net.add_edge(get_module_id("PROJ531"), get_skill_id("TC-1.1"), weight=1)
net.add_edge(get_module_id("PROJ531"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("PROJ531"), get_skill_id("TC-2.2"), weight=1)
net.add_edge(get_module_id("PROJ531"), get_skill_id("IDU-2.3"), weight=1)
net.add_edge(get_module_id("PROJ531"), get_skill_id("IDU-4.1"), weight=1)

# semestre 7
net.add_edge(get_module_id("LANG701a"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("LANG701a"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("LANG701a"), get_skill_id("TC-3.3"), weight=1)

net.add_edge(get_module_id("LANG702a"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("LANG702a"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("LANG702a"), get_skill_id("TC-3.3"), weight=1)

net.add_edge(get_module_id("SHES703a"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("SHES703a"), get_skill_id("TC-2.2"), weight=1)
net.add_edge(get_module_id("SHES703a"), get_skill_id("TC-2.3"), weight=1)

# net.add_edge(get_module_id("SHES704a"), get_skill_id("TC-2.2"), weight=1)
# net.add_edge(get_module_id("SHES704a"), get_skill_id("TC-3.2"), weight=1)
# net.add_edge(get_module_id("SHES704a"), get_skill_id("TC-3.4"), weight=1)
# net.add_edge(get_module_id("SHES704a"), get_skill_id("TC-4.3"), weight=1)
# net.add_edge(get_module_id("SHES704a"), get_skill_id("TC-4.4"), weight=1)

net.add_edge(get_module_id("DATA731a"), get_skill_id("IDU-2.1"), weight=1)
net.add_edge(get_module_id("DATA731a"), get_skill_id("IDU-2.2"), weight=1)

net.add_edge(get_module_id("INFO731a"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("INFO731a"), get_skill_id("IDU-2.3"), weight=1)
net.add_edge(get_module_id("INFO731a"), get_skill_id("IDU-4.1"), weight=1)
net.add_edge(get_module_id("INFO731a"), get_skill_id("IDU-4.2"), weight=1)

net.add_edge(get_module_id("MATH741c"), get_skill_id("IDU-2.1"), weight=1)
net.add_edge(get_module_id("MATH741c"), get_skill_id("IDU-2.2"), weight=1)
net.add_edge(get_module_id("MATH741c"), get_skill_id("IDU-2.3"), weight=1)

net.add_edge(get_module_id("INFO732a"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("INFO732a"), get_skill_id("IDU-1.2"), weight=1)
net.add_edge(get_module_id("INFO732a"), get_skill_id("IDU-1.3"), weight=1)
net.add_edge(get_module_id("INFO732a"), get_skill_id("IDU-2.3"), weight=1)
net.add_edge(get_module_id("INFO732a"), get_skill_id("IDU-4.1"), weight=1)
net.add_edge(get_module_id("INFO732a"), get_skill_id("TC-3.2"), weight=1)

net.add_edge(get_module_id("INFO743c"), get_skill_id("IDU-2.3"), weight=1)
net.add_edge(get_module_id("INFO743c"), get_skill_id("IDU-4.1"), weight=1)
net.add_edge(get_module_id("INFO743c"), get_skill_id("IDU-4.2"), weight=1)
net.add_edge(get_module_id("INFO743c"), get_skill_id("TC-1.3"), weight=1)

net.add_edge(get_module_id("PROJ731a"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("PROJ731a"), get_skill_id("IDU-1.2"), weight=1)
net.add_edge(get_module_id("PROJ731a"), get_skill_id("IDU-4.1"), weight=1)

net.add_edge(get_module_id("DATA732a"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("DATA732a"), get_skill_id("IDU-2.1"), weight=1)

net.add_edge(get_module_id("INFO734a"), get_skill_id("IDU-1.1"), weight=1)

net.add_edge(get_module_id("ISOC731a"), get_skill_id("IDU-2.3"), weight=1)
net.add_edge(get_module_id("ISOC731a"), get_skill_id("IDU-3.2"), weight=1)
net.add_edge(get_module_id("ISOC731a"), get_skill_id("IDU-4.2"), weight=1)
net.add_edge(get_module_id("ISOC731a"), get_skill_id("TC-1.2"), weight=1)
net.add_edge(get_module_id("ISOC731a"), get_skill_id("TC-1.3"), weight=1)
net.add_edge(get_module_id("ISOC731a"), get_skill_id("TC-3.2"), weight=1)

# Semestre 9
net.add_edge(get_module_id("LANG901a"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("LANG901a"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("LANG901a"), get_skill_id("TC-3.3"), weight=1)
net.add_edge(get_module_id("LANG902a"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("LANG902a"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("LANG902a"), get_skill_id("TC-3.3"), weight=1)
net.add_edge(get_module_id("PROJ901a"), get_skill_id("TC-1.3"), weight=1)
net.add_edge(get_module_id("PROJ901a"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("PROJ901a"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("PROJ901a"), get_skill_id("TC-4.1"), weight=1)
net.add_edge(get_module_id("PROJ901a"), get_skill_id("TC-4.2"), weight=1)
net.add_edge(get_module_id("PROJ901a"), get_skill_id("TC-4.3"), weight=1)
net.add_edge(get_module_id("PROJ901a"), get_skill_id("TC-1.1"), weight=1)
net.add_edge(get_module_id("PROJ901a"), get_skill_id("TC-1.2"), weight=1)
net.add_edge(get_module_id("PROJ901a"), get_skill_id("TC-1.5"), weight=1)
net.add_edge(get_module_id("PROJ901a"), get_skill_id("TC-4.4"), weight=1)
net.add_edge(get_module_id("SHES901a"), get_skill_id("TC-2.2"), weight=1)
net.add_edge(get_module_id("SHES901a"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("SHES901a"), get_skill_id("TC-3.4"), weight=1)
net.add_edge(get_module_id("SHES901a"), get_skill_id("TC-1.1"), weight=1)
net.add_edge(get_module_id("SHES901a"), get_skill_id("TC-1.5"), weight=1)
net.add_edge(get_module_id("INFO931"), get_skill_id("IDU-2.2"), weight=1)
net.add_edge(get_module_id("INFO931"), get_skill_id("IDU-4.1"), weight=1)
net.add_edge(get_module_id("INFO931"), get_skill_id("TC-1.2"), weight=1)
net.add_edge(get_module_id("INFO931"), get_skill_id("TC-1.4"), weight=1)
net.add_edge(get_module_id("INFO931"), get_skill_id("IDU-3.1"), weight=1)
net.add_edge(get_module_id("INFO931"), get_skill_id("IDU-3.2"), weight=1)
net.add_edge(get_module_id("INFO932"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("INFO932"), get_skill_id("IDU-1.2"), weight=1)
net.add_edge(get_module_id("INFO932"), get_skill_id("IDU-1.3"), weight=1)
net.add_edge(get_module_id("INFO932"), get_skill_id("IDU-4.1"), weight=1)
net.add_edge(get_module_id("PROJ931"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("PROJ931"), get_skill_id("IDU-2.3"), weight=1)
net.add_edge(get_module_id("PROJ931"), get_skill_id("IDU-3.1"), weight=1)
net.add_edge(get_module_id("DATA931"), get_skill_id("IDU-1.3"), weight=1)
net.add_edge(get_module_id("DATA931"), get_skill_id("IDU-2.1"), weight=1)
net.add_edge(get_module_id("DATA931"), get_skill_id("IDU-2.3"), weight=1)
net.add_edge(get_module_id("DATA931"), get_skill_id("IDU-3.1"), weight=1)
net.add_edge(get_module_id("DATA931"), get_skill_id("IDU-4.1"), weight=1)
net.add_edge(get_module_id("DATA931"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("ISOC931"), get_skill_id("TC-1.2"), weight=1)
net.add_edge(get_module_id("ISOC931"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("ISOC931"), get_skill_id("TC-3.3"), weight=1)
net.add_edge(get_module_id("ISOC931"), get_skill_id("TC-4.1"), weight=1)
net.add_edge(get_module_id("PROJ932"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("PROJ932"), get_skill_id("IDU-1.2"), weight=1)
net.add_edge(get_module_id("PROJ932"), get_skill_id("IDU-1.3"), weight=1)
net.add_edge(get_module_id("PROJ932"), get_skill_id("IDU-2.1"), weight=1)
net.add_edge(get_module_id("PROJ932"), get_skill_id("IDU-4.1"), weight=1)

# Semestre 10
net.add_edge(get_module_id("PROJ001"), get_skill_id("TC-3.1"), weight=1)
net.add_edge(get_module_id("PROJ001"), get_skill_id("TC-3.2"), weight=1)
net.add_edge(get_module_id("PROJ001"), get_skill_id("TC-3.3"), weight=1)
net.add_edge(get_module_id("PROJ001"), get_skill_id("TC-3.4"), weight=1)
net.add_edge(get_module_id("PROJ001"), get_skill_id("TC-1.1"), weight=1)
net.add_edge(get_module_id("PROJ001"), get_skill_id("TC-1.2"), weight=1)
net.add_edge(get_module_id("PROJ001"), get_skill_id("TC-1.3"), weight=1)
net.add_edge(get_module_id("PROJ001"), get_skill_id("TC-1.4"), weight=1)
net.add_edge(get_module_id("PROJ001"), get_skill_id("TC-1.5"), weight=1)
net.add_edge(get_module_id("PROJ001"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("PROJ001"), get_skill_id("TC-2.2"), weight=1)
net.add_edge(get_module_id("PROJ001"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("PROJ001"), get_skill_id("TC-4.3"), weight=1)
net.add_edge(get_module_id("PROJ001"), get_skill_id("TC-4.4"), weight=1)

# semestre 6
net.add_edge(get_module_id("LANG601a"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("LANG601a"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("LANG601a"), get_skill_id("TC-3.3"), weight=1)

net.add_edge(get_module_id("PROJ601a"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("PROJ601a"), get_skill_id("TC-2.2"), weight=1)
net.add_edge(get_module_id("PROJ601a"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("PROJ601a"), get_skill_id("TC-3.3"), weight=1)

net.add_edge(get_module_id("SHES601a"), get_skill_id("TC-3.2"), weight=1)
net.add_edge(get_module_id("SHES602a"), get_skill_id("TC-3.2"), weight=1)

net.add_edge(get_module_id("INFO631a"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("INFO631a"), get_skill_id("IDU-1.2"), weight=1)

net.add_edge(get_module_id("MATH641c"), get_skill_id("IDU-2.1"), weight=1)
net.add_edge(get_module_id("MATH641c"), get_skill_id("IDU-2.3"), weight=1)

net.add_edge(get_module_id("PROJ631a"), get_skill_id("IDU-2.1"), weight=1)
net.add_edge(get_module_id("PROJ631a"), get_skill_id("IDU-2.1"), weight=1)
net.add_edge(get_module_id("PROJ631a"), get_skill_id("IDU-4.1"), weight=1)
net.add_edge(get_module_id("PROJ631a"), get_skill_id("TC-4.1"), weight=1)
net.add_edge(get_module_id("PROJ631a"), get_skill_id("TC-4.2"), weight=1)

net.add_edge(get_module_id("INFO632"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("INFO632"), get_skill_id("IDU-4.1"), weight=1)

net.add_edge(get_module_id("INFO641c"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("INFO641c"), get_skill_id("IDU-4.1"), weight=1)

net.add_edge(get_module_id("INFO642c"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("INFO642c"), get_skill_id("IDU-4.1"), weight=1)
net.add_edge(get_module_id("INFO642c"), get_skill_id("IDU-2.3"), weight=1)
net.add_edge(get_module_id("INFO642c"), get_skill_id("IDU-2.2"), weight=1)

net.add_edge(get_module_id("ISOC631"), get_skill_id("IDU-2.3"), weight=1)
net.add_edge(get_module_id("ISOC631"), get_skill_id("IDU-2.1"), weight=1)
net.add_edge(get_module_id("ISOC631"), get_skill_id("IDU-4.1"), weight=1)
net.add_edge(get_module_id("ISOC631"), get_skill_id("TC-1.4"), weight=1)

net.add_edge(get_module_id("PROJ632"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("PROJ632"), get_skill_id("IDU-2.1"), weight=1)

net.add_edge(get_module_id("INFO632a"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("INFO632a"), get_skill_id("IDU-4.1"), weight=1)

net.add_edge(get_module_id("ISOC631a"), get_skill_id("IDU-2.1"), weight=1)
net.add_edge(get_module_id("ISOC631a"), get_skill_id("IDU-2.3"), weight=1)
net.add_edge(get_module_id("ISOC631a"), get_skill_id("TC-1.1"), weight=1)

net.add_edge(get_module_id("PROJ632a"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("PROJ632a"), get_skill_id("IDU-2.1"), weight=1)

# semestre 8
net.add_edge(get_module_id("LANG801a"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("LANG801a"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("LANG801a"), get_skill_id("TC-3.3"), weight=1)

net.add_edge(get_module_id("LANG802a"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("LANG802a"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("LANG802a"), get_skill_id("TC-3.3"), weight=1)

net.add_edge(get_module_id("SHES802a"), get_skill_id("TC-1.1"), weight=1)
net.add_edge(get_module_id("SHES802a"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("SHES802a"), get_skill_id("TC-3.1"), weight=1)
net.add_edge(get_module_id("SHES802a"), get_skill_id("TC-3.2"), weight=1)

net.add_edge(get_module_id("SHES803a"), get_skill_id("TC-3.2"), weight=1)

net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-1.1"), weight=1)
net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-1.2"), weight=1)
net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-1.3"), weight=1)
net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-1.4"), weight=1)
net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-1.5"), weight=1)
net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-2.1"), weight=1)
net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-2.2"), weight=1)
net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-2.3"), weight=1)
net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-3.1"), weight=1)
net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-3.2"), weight=1)
net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-3.3"), weight=1)
net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-3.4"), weight=1)
net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-4.1"), weight=1)
net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-4.2"), weight=1)
net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-4.3"), weight=1)
net.add_edge(get_module_id("PROJ801"), get_skill_id("TC-4.4"), weight=1)

net.add_edge(get_module_id("DATA831a"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("DATA831a"), get_skill_id("IDU-1.3"), weight=1)

net.add_edge(get_module_id("DATA832a"), get_skill_id("IDU-1.3"), weight=1)
net.add_edge(get_module_id("DATA832a"), get_skill_id("IDU-2.1"), weight=1)
net.add_edge(get_module_id("DATA832a"), get_skill_id("IDU-2.2"), weight=1)
net.add_edge(get_module_id("DATA832a"), get_skill_id("IDU-2.3"), weight=1)
net.add_edge(get_module_id("DATA832a"), get_skill_id("TC-1.2"), weight=1)
net.add_edge(get_module_id("DATA832a"), get_skill_id("TC-3.2"), weight=1)

net.add_edge(get_module_id("INFO831a"), get_skill_id("IDU-1.3"), weight=1)
net.add_edge(get_module_id("INFO831a"), get_skill_id("IDU-2.1"), weight=1)
net.add_edge(get_module_id("INFO831a"), get_skill_id("IDU-2.2"), weight=1)
net.add_edge(get_module_id("INFO831a"), get_skill_id("IDU-3.1"), weight=1)
net.add_edge(get_module_id("INFO831a"), get_skill_id("TC-3.2"), weight=1)

net.add_edge(get_module_id("PROJ831a"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("PROJ831a"), get_skill_id("IDU-2.1"), weight=1)

net.add_edge(get_module_id("INFO832a"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("INFO832a"), get_skill_id("IDU-3.1"), weight=1)

net.add_edge(get_module_id("INFO833a"), get_skill_id("IDU-1.1"), weight=1)
net.add_edge(get_module_id("INFO833a"), get_skill_id("IDU-1.2"), weight=1)
net.add_edge(get_module_id("INFO833a"), get_skill_id("IDU-1.3"), weight=1)
net.add_edge(get_module_id("INFO833a"), get_skill_id("IDU-4.1"), weight=1)
net.add_edge(get_module_id("INFO833a"), get_skill_id("IDU-4.2"), weight=1)

net.add_edge(get_module_id("INFO834a"), get_skill_id("TC-3.2"), weight=1)
net.add_edge(get_module_id("INFO834a"), get_skill_id("TC-1.2"), weight=1)
net.add_edge(get_module_id("INFO834a"), get_skill_id("IDU-4.1"), weight=1)
net.add_edge(get_module_id("INFO834a"), get_skill_id("IDU-2.3"), weight=1)
net.add_edge(get_module_id("INFO834a"), get_skill_id("IDU-1.3"), weight=1)
net.add_edge(get_module_id("INFO834a"), get_skill_id("IDU-1.2"), weight=1)

net.add_edge(get_module_id("ISOC831a"), get_skill_id("TC-3.1"), weight=1)
net.add_edge(get_module_id("ISOC831a"), get_skill_id("TC-3.2"), weight=1)
"""

net.show("prerequis.html")
w.open("prerequis.html")
