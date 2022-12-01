# Ransomware de 0xM@rt

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

Dans le cadre de ma formation j'ai du développer un malware de type rootkit

le but du malware et communiquer avec une machine distante pour effectuer des actions a distances sur le pc client 



## Pour commencer

Faite attention ce logiciel a été créé dans le but d'apprentissage il ne faut pas l'utiliser a des fin malvaillante  

il se peut qu'il y'est des petit probleme d'encodage car sous windows l'UTF-8 ne fonctionne pas

### Pré-requis

Il faut avoir un fichier file.txt sur la machine distante
ainsi que le fichier client.py


### Installation

* _Pour_ _Windows_ :

  Pour installer python il faut se rendre sur https://www.python.org/downloads/

* _Pour_ _Ubuntu_ :

  Pour installer python il faut utiliser la commande sudo apt-get install python

## Démarrage

Pour lancer le logiciel il faut juste taper *Python3 serveur.py* puis *Python3 client.py* sur la machine distante


## Explication du code 

* _Pour_ _Serveur.py_ :

--------------------------Les imports---------------------

Socket permet de gerer les connexions par socket (permet d'ouvrir des connexion avec des machines)

OS utiliser notament pour ouvrir des fichiers

subprocess permet de lancer de nouveaux processus

time permet de gerer des temps via differente fonctions

json permet de définir un format pour les fichier echange

----------------------Les classes--------------------

L'objectif ici de la classe Shell et de reunir tout les fonctions utile dans notre rootkit 

----------------------Les fonctions--------------------

_init_ est une fonction qui permet d'initialisé la classe

verifications est une fonction qui Permet de veriifier/definir les commandes taper depuis le serveur pour attaquer le client

home est une fonction qui envoie l'instruction 'home' à la victime qui l'interprète. 

command est une fonction pour utilser des commmand dans le shell par exemple :

Ici on verifie si le serveur a taper exit et exit le shell si besoin

```python
 if(SHELL == "exit"):
        SHELL = ""
        return("exit")
 ```

recv_archive pour recevoir un fichier depuis le client via de l'exfiltration de données

----------------------------Socket----------------------

il ne faut pas oublier la partie de gestion des socket pour la connexion réseau et linitialisation des paramètres de bas (PORT, IP)

* _Pour_ _client.py_ :

--------------------------Les imports---------------------

Socket permet de gerer les connexions par socket (permet d'ouvrir des connexion avec des machines)

OS utiliser notament pour ouvrir des fichiers

subprocess permet de lancer de nouveaux processus

time permet de gerer des temps via differente fonctions

json permet de définir un format pour les fichier echange

----------------------Les classes--------------------

L'objectif ici de la classe Client et de reunir tout les fonctions utiles.

----------------------Les fonctions--------------------

_init_ est une fonction qui permet d'initialisé la classe

verifications est une fonction qui permet l'execution des commandes coté client

command est une fonction qui execute l'ordre envoyé par le serveur puis le client répond

send_archive pour envoyer des fichiers sur le serveur 

----------------------------Socket----------------------

il ne faut pas oublier la partie de gestion des socket pour la connexion réseau et linitialisation des paramètres de bas (PORT, IP)

## Auteurs
Listez le(s) auteur(s) du projet ici !
* **0xM@rt** _alias_ [@0xM@rt](https://github.com/0xMart)



