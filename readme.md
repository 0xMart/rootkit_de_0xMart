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
La classe Shell contient des fonctions qui permettent de créé un shell sur le serveur pour pouvoir effectuer des actions sur le client a distance.
----------------------Les fonctions--------------------
_init_ est une fonction qui initialise un shell
verifications est une fonction qui verifie ce que l'on tape dans le shell pour pouvoir ensuite via les conditions executer des actions
home est une fonction qui envoie l'instruction 'home' à la victime qui l'interprète. 
command est une fonction pour utilser des commmand dans le shell
recv_archive pour recevoir un fichier depuis le client
---------------------------------------------------------------
il ne faut pas oublier la partie de gestion des socket pour la connexion réseau

* _Pour_ _client.py_ :

--------------------------Les imports---------------------
Socket permet de gerer les connexions par socket (permet d'ouvrir des connexion avec des machines)
OS utiliser notament pour ouvrir des fichiers
subprocess permet de lancer de nouveaux processus
time permet de gerer des temps via differente fonctions
json permet de définir un format pour les fichier echange
----------------------Les classes--------------------
La classe Client contient des fonctions qui permettent d'initialisité la communication avec le shell sur le serveur pour pouvoir effectuer des actions sur le client a distance.
----------------------Les fonctions--------------------
_init_ est une fonction qui initialise un shell
verifications est une fonction qui verifie ce que l'on tape dans le shell pour pouvoir ensuite via les conditions executer des actions
command est une fonction pour executer des commande taper sur le serveur
send_archive pour envoyer des fichiers sur le serveur 
---------------------------------------------------------------
il ne faut pas oublier la partie de gestion des socket pour la connexion réseau
## Auteurs
Listez le(s) auteur(s) du projet ici !
* **0xM@rt** _alias_ [@0xM@rt](https://github.com/0xMart)



