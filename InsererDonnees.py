import mysql.connector

db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "my_db"
)

cur = db.cursor()
#requéte SQL
sql = "INSERT INTO Matiere (idMatiere,nomMatiere,coef,competence,nbHeure) VALUES (%s, %s,%s,%s,%s)"
sql = "INSERT INTO Semestre (idSemestre,nomSemestre,idUE) VALUES (%s,%s,%s)"
sql = "INSERT INTO Competence (idCompetence,nomCompetence) VALUES (%s,%s)"
sql = "INSERT INTO UE (idUE,nomUE,idMatiere) VALUES (%s,%s,%s)"
sql =  "INSERT INTO Specialite (idSpecialite,nomSpecialite) VALUES (%s,%s,%s)"

#les valeurs de la requéte SQL
valueMatiere = [
  (1,'Electricité',3,'',40.5 ),
  (),
  (),
  (),
  (),
  (),
  ()
]

valueSemestre = [(1,'',1)]
valueCompetence = [(1,'')]
valueUE = [(1,'',1)]
valueSpecialite = [(1,'')]

#exécuter le curseur avec la méthode executemany() et transmis la requéte SQL
cur.executemany(sql, valueMatiere ,valueSemestre,valueCompetence,valueUE ,valueSpecialite)
#valider la transaction
db.commit()
#afficher le nombre de lignes insérées
print(cur.rowcount, "lignes insérées.")