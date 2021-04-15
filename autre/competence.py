import this
import tabula
import textReader as t
import webbrowser as w
import prerequis as p
import competenceExtractor as c
from pyvis.network import Network

# the purpose of this script is to build the network of the subjects and
# the link between them
text = t.text
df = tabula.read_pdf('Referentiel_Competences_IDU_2021_2025.pdf', pages='all')[2]
p_competence = df["UE"]
# i create a network
net = Network(height='100%', width='100%', bgcolor='#222222', font_color='white')


class Subject:
    def __init__(self, id_node, label):
        this.id = id_node
        this.label = label

    def getId(self):
        return this.id

    def getLabel(self):
        return this.label


class Skill:
    def __init__(self, id_node, label):
        this.id = id_node
        this.label = label
        this.subjects = []

    def getId(self):
        return this.id

    def getLabel(self):
        return this.label

    def list_subject(self, subject_id):
        this.subjects.append(subject_id)


# the list of subject in the coursework
def list_module_plus_id():
    subjects = t.list_Module_court(text)
    liste = []
    compteur = 0
    for subject in subjects:
        liste.append(Subject(compteur, subject))
        compteur += 1
    return liste


# add skill information
def list_skill_info():
    skill_info = c.competence_spe_info()
    compteur = 500
    liste = list()
    for items in skill_info.items():
        for item in items[1]:
            liste.append(Skill(compteur, item))
            compteur += 1
    return liste

