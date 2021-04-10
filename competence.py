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


class SkillNode:

    def __init__(self, id_node, label):
        this.id = id_node
        this.label = label

    def getId(self):
        return this.id

    def getLabel(self):
        return this.label


class Edge:

    def __init__(self, id_edge, label):
        this.id = id_edge
        this.label = label

    def getId(self):
        return this.id

    def getLabel(self):
        return this.label


# the list of subject in the coursework
def list_module_plus_id():
    subjects = t.list_Module_court(text)
    liste = []
    compteur = 0
    for subject in subjects:
        liste.append(SkillNode(compteur, subject))
        compteur += 1
    return liste

