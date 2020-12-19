

# créer une api

"""

1. lire le document
2. enregistrer le document dans un dictionnaire
3. servir le document:
    - flask

"""



# un csv --> une librarie python3 qui lit du csv -- librairie standard (core) python3


import csv

class myClass:
    name = ""
    age = 0
    hobbies = []
    def __init__(self, var1, var2, var3):
        self.name = var1
        self.age = var2
        self.hobbies = var3
    def __getitem__(self, key):
        return self[key]


my_list = []

# lire le document && enregistrer le document dans un dictionnaire  

with open('Matrice-des-interacteurs2.csv', 'r') as f:
    reader = csv.reader(f, delimiter=';')
    for row in reader:
        #print(row)
        my_list.append(myClass(row[0], row[1], row[2:]))

#print(my_list)
#print(my_list[0].name)
  
#3. servir le document:
    #- flask
    #- récupérer n'importe quelle combinaison ligne/colonne


my_list = [

    {
        "name": "toto",
        "age": 2
    },
    {
        "name": "toto2",
        "age": 3
    }

]

from flask import Flask
app = Flask(__name__)

#print(my_list[0]['name'])

@app.route('/')
def welcome():
    return 'welcome to my api'

@app.route('/<poz>')
def process1(poz=0):
    return str(my_list[int(poz)])

@app.route('/<poz>/<prop>')
def process2(poz=0, prop='name'):
    return str(my_list[int(poz)][prop])

app.run(host='0.0.0.0', port=80)
