## D. Système de Gestion de Base de Données (SGBD)
Un **SGBD** est le logiciel qui permet de stocker, modifier et retrouver les données. C'est le "chef d'orchestre" de la base.

* **Exemples :** MySQL (sites web), Oracle (banques), MongoDB (données flexibles), PostgreSQL.



C'est comme à la bibliothèque, vous ne fouillez pas vous-même les rayons. Vous demandez au **bibliothécaire** (le SGBD) : "Je veux le dossier de Monsieur Martin". C'est lui qui va le chercher pour vous.



## E. Bases de données Relationnelles vs Non Relationnelles

* **Relationnelle (SQL) :** Les données sont rangées dans des tables liées entre elles. Très rigide et sécurisé.
    * *Exemple :* Une application bancaire.
* **Non Relationnelle (NoSQL) :** Les données sont stockées sous forme de documents ou de listes. Très flexible.
    * *Exemple :* Le fil d'actualité d'un réseau social.

La base relationnelle est une comme **armoire à tiroirs** avec des étiquettes fixes. La base non relationnelle est un ensemble de **chemises cartonnées** où l'on peut ajouter des feuilles de tailles différentes à tout moment.



## F. Clé Primaire et Clé Étrangère
* **Clé Primaire :** Un identifiant unique pour chaque ligne (ex: un numéro de client).
* **Clé Étrangère :** C'est la clé primaire d'une table que l'on retrouve dans une autre pour créer un lien (ex: le numéro de client dans une table "Commandes").

On peut utiliser la  **La métaphore de l'identité :** Votre **numéro de carte d'identité** est votre **clé primaire**. Si ce numéro est noté sur votre contrat de bail, il devient une **clé étrangère** pour lier le logement à votre identité.