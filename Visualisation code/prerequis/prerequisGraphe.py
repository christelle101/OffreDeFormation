import tabula
import textReader as t
import webbrowser as w
import prerequis as p
from pyvis.network import Network

text = t.text
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

# the liste of edges
edges = p.prerequis

# add edges
for edge in edges:
    id1 = get_module_id(edge[0])
    id2 = get_module_id(edge[1])
    # print(id2)
    net.add_edge(id1, id2, weight=1)

net.show("prerequis.html")
w.open("prerequis.html")
