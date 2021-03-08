# OffreDeFormation
## Objectif :
Il s'agit d'un projet dans le cadre du module Proj632.

L' objectif de ce projet est de pouvoir identifier pour les formations ingenieurs les éléments permettant de récupérer les informations permettant de représenter la formation, à travers ses modules, le lien entre les modules et le lien avec les différentes compétences visées.

Le programme va permettre d’extraire les informations nécessaires qui se trouvent sous forme d’un pdf,puis les convertir vers un fichier texte pour pouvoir les manipuler.
Ensuite ,nous procédons à l’insertion de ces données dans la base créée pour ce fait.La base de données contient les tables semestre,module,prérequis,et UE (Unité d’enseignement) .Nous proposons après une représentation visuelle de la formation sous forme d’un graphe.

Le fichier pdf contient les informations suivantes :
Le sommaire - Les modules - les semestres - les prérequis - Les unités d’enseignement.

## Composition du code:
Pour créer la base de données il nous a fallu :

* Un modèle entité association: **ModeleEA.png**.
* Un modèle relationnel: **Modele_Relationnel.png**. 

Puis :
#### BDcreator.py : permet d’implémenter la base de données.
Ce programme utilise la bibliothèque sqlalchemy qui permet de créer les tables semestre, module, prérequis et UE (Unité d’enseignement). Puis l’insertion des données dans ces tables.

 
Pour récupérer les données, il faudra :
### textReader.py:  permet de procéder à l’extraction des données:

* La fonction **sommaire_extracting(fichier)** permet d'extraire les données du sommaire.
* La fonction **UE_module(fichier)**  permet de créer une relation entre les UE et les modules 
* La fonction  **semestre_UE(fichier)** permet de créer une relation entre les semestre et les UE
* La fonction **Module(fichier)** retourne la liste des modules de la formation
* La fonction **attributModule(module, fichier)** retourne les prérequis du modules

Pour convertir les données :
### pdfExtractor.py : permet de convertir un fichier PDF au format TXT.
Il contient les fonctions suivantes :
   * **convert_pdf_to_string(file)** :convertit le pdf en chaîne de caractères.
   * **textCreator( pdfContent)** : crée un fichier à partir des données obtenues afin de faciliter la gestion   des données

Enfin,dans le fichier data.png vous trouverez le graphe qui représente les différents liens entre les semestres, unité d’enseignement et les modules.
