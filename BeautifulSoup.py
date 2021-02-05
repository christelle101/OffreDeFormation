import requests
import csv
from bs4 import BeautifulSoup

url = "http://ead-polytech.univ-savoie.fr/course/index.php?categoryid=257"
response = requests.get(url)
html = BeautifulSoup(response.text, 'html.parser')
cours_html = html.find_all(class_="info")
  
cours = list()
for coursename  in cours_html:
    cours.append(coursename.text)
    

for t in zip(cours):
    print(t)


with open('./resEssai1.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, dialect='excel')
    csv_writer.writerows(zip(cours))
    
   
    
    
    


