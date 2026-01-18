# Hello Veille – Fondamentaux de la donnée et des bases de données

## Introduction – Comprendre la donnée pour mieux la valoriser

Dans un contexte où la donnée est devenue un actif stratégique pour les entreprises, comprendre sa nature, sa qualité et les systèmes qui la manipulent est un prérequis pour tout professionnel évoluant dans les métiers de la data, de la BI ou de l'ingénierie analytique.

Cette veille s'inscrit dans le projet **Hello DBMS+** et a pour objectif de poser des bases solides, à la fois **conceptuelles et pratiques**, sur les notions fondamentales liées à la donnée : sa définition, ses formes, ses critères de qualité, les systèmes de stockage et de gestion, ainsi que les principes de modélisation et d'interrogation via le langage SQL.

L'approche adoptée est volontairement **pédagogique mais rigoureuse**. Chaque concept est expliqué de manière accessible, à l'aide de métaphores simples, d'exemples concrets et de schémas visuels, afin de rendre ces notions compréhensibles même pour un lecteur non technique. Cette démarche reflète une compétence clé dans les environnements data : la capacité à **faire le lien entre des concepts techniques et des enjeux métiers**.

Ce travail ne se limite pas à une recherche théorique. Il constitue un socle de compréhension mobilisé ensuite dans les autres livrables du projet : modélisation de données, requêtes SQL, analyses exploratoires et application web pédagogique. Il illustre une vision transversale de la donnée, depuis sa définition jusqu'à son exploitation dans un système réel.

---

## La donnée : fondation de tous les systèmes data

### A. Qu’est-ce qu’une donnée ? Sous quelle forme peut-elle se présenter ?

### 1. Définition d’une donnée
Une **donnée** est un fait brut, une observation ou une mesure qui, prise isolément, **n’a pas de signification**.  
Elle devient une **information** lorsqu’elle est traitée, contextualisée et interprétée afin d’aider à la prise de décision.

**Exemple :**
- Données : `25`, `Paris`, `01/01/2025`
- Information : *« La température à Paris était de 25°C le 1er janvier 2025. »*

La donnée constitue la **matière première** des métiers liés à la data, à l’intelligence artificielle et à la business intelligence.

---

### 2. Les différentes formes de données

#### a) Données structurées
- Organisées sous forme de lignes et de colonnes
- Stockées dans des bases de données relationnelles
- Faciles à interroger avec le langage SQL

**Exemples :**
- Tables clients
- Transactions de ventes
- Bases comptables

```text
ID_Client | Nom   | Âge | Pays
101       | Aida  | 23  | France
```

---

#### b) Données semi-structurées
- Organisation partielle grâce à des balises ou clés
- Structure flexible

**Exemples :**
- Fichiers JSON
- Fichiers XML
- Logs applicatifs

```json
{
  "nom": "Aida",
  "competences": ["Data", "IA"],
  "etudiante": true
}
```

---

#### c) Données non structurées
- Aucune structure prédéfinie
- Nécessitent des traitements spécifiques pour être exploitées

**Exemples :**
- Textes libres
- Images
- Vidéos
- Sons
- Publications sur les réseaux sociaux

> 📌 Plus de **80 % des données mondiales** sont non structurées.

---

## B. Les critères de mesure de la qualité des données

La qualité des données est essentielle pour garantir la **fiabilité des analyses** et des modèles d’intelligence artificielle.

### Principaux critères de qualité

#### 1. Exactitude (*Accuracy*)
La donnée doit représenter fidèlement la réalité.  
Une erreur de saisie peut fausser toute une analyse.

---

#### 2. Complétude (*Completeness*)
Toutes les informations nécessaires doivent être présentes.  
Exemple : un client sans adresse e-mail rend certaines actions impossibles.

---

#### 3. Cohérence (*Consistency*)
La même donnée doit être identique dans tous les systèmes.  
Exemple : un client ne peut pas avoir deux dates de naissance différentes selon la base consultée.

---

#### 4. Actualité (*Timeliness*)
Les données doivent être à jour et disponibles au bon moment.  
Des données obsolètes entraînent de mauvaises décisions.

---

#### 5. Validité (*Validity*)
Les données doivent respecter des règles et des formats définis.

**Exemples :**
- Adresse e-mail valide
- Âge strictement positif

---

#### 6. Unicité (*Uniqueness*)
Une donnée ne doit pas être dupliquée.  
Les doublons faussent les indicateurs et les statistiques.

---

### Tableau récapitulatif

| Critère | Description |
|-------|-------------|
| Exactitude | Donnée correcte |
| Complétude | Donnée complète |
| Cohérence | Donnée identique partout |
| Actualité | Donnée récente |
| Validité | Respect des règles |
| Unicité | Absence de doublons |

---

## C. Data Lake, Data Warehouse et Lakehouse

Ces trois architectures définissent la manière dont les données sont **stockées, organisées et exploitées**.

---

### 1. Data Warehouse

#### Définition
Un **Data Warehouse** est une base de données dédiée à l’analyse décisionnelle.  
Il contient des données **structurées, nettoyées et transformées**.

- Schéma à l’écriture (*schema-on-write*)
- Forte performance pour les requêtes analytiques
- Utilisé par les analystes et décideurs

#### Cas d’usage
- Tableaux de bord
- Indicateurs de performance (KPI)
- Reporting financier

#### Schéma simplifié

```text
Systèmes opérationnels
        ↓
      ETL
        ↓
   Data Warehouse
        ↓
     BI / Reporting
```

**Avantages :** données fiables, performance élevée  
**Limites :** faible flexibilité

---

### 2. Data Lake

#### Définition
Un **Data Lake** stocke les données **brutes**, quel que soit leur format.

- Schéma à la lecture (*schema-on-read*)
- Très grande capacité de stockage
- Coût réduit
- Principalement utilisé par les data scientists

#### Cas d’usage
- Machine Learning
- Big Data
- Analyse exploratoire

#### Schéma simplifié

```text
Sources (IoT, logs, images, applications)
                 ↓
              Data Lake
                 ↓
      IA / Analyse avancée
```

**Avantages :** flexibilité, scalabilité  
**Limites :** risque de *Data Swamp* sans gouvernance

---

### 3. Lakehouse

#### Définition
Le **Lakehouse** combine les avantages du **Data Lake** et du **Data Warehouse**.

- Données structurées et non structurées
- Schéma hybride
- Transactions fiables (ACID)
- Plateforme unique pour BI et IA

#### Cas d’usage
- Analytique unifiée
- IA et reporting sur les mêmes données

#### Schéma simplifié

```text
Sources de données
        ↓
     Lakehouse
      ↙     ↘
   BI       IA / ML
```

---

#### Tableau comparatif

| Critère | Data Warehouse | Data Lake | Lakehouse |
|------|---------------|----------|----------|
| Type de données | Structurées | Toutes | Toutes |
| Schéma | Écriture | Lecture | Hybride |
| Coût | Élevé | Faible | Moyen |
| BI | Excellent | Limité | Excellent |
| IA / ML | Limité | Excellent | Excellent |

---
## Les systèmes de gestion de bases de données

### D. Système de Gestion de Base de Données (SGBD)

Un SGBD est le logiciel qui permet de stocker, modifier et retrouver les données. C’est l’intermédiaire entre l’utilisateur et la base de données. Il garantit la sécurité, la cohérence et la performance des accès aux données.

Exemples de SGBD :
MySQL (applications web),
PostgreSQL (analytique et applications complexes),
Oracle (systèmes bancaires),
MongoDB (données flexibles).

Métaphore :
Dans une bibliothèque, vous ne fouillez pas vous-même les rayons. Vous demandez au bibliothécaire. Le SGBD joue ce rôle.
C'est comme à la bibliothèque, vous ne fouillez pas vous-même les rayons. Vous demandez au bibliothécaire (le SGBD) : "Je veux le dossier de Monsieur Martin". C'est lui qui va le chercher pour vous.

### E. Bases de données relationnelles et non relationnelles
Base de données relationnelle (SQL)

Les données sont organisées en tables liées entre elles par des relations.
Structure rigide, forte cohérence et contraintes strictes.

Exemple : système bancaire.

Base de données non relationnelle (NoSQL)

Les données sont stockées sous forme de documents, clés-valeurs ou graphes.
Très flexible, adaptée aux grands volumes et aux données hétérogènes.

Exemple : réseau social.

#### Métaphore :
La base relationnelle est une armoire à tiroirs étiquetés.
La base non relationnelle est un ensemble de dossiers souples.
---

## Les fondements de la modélisation des données

### F. Clé primaire et clé étrangère

Clé primaire : identifiant unique d’une ligne dans une table.
Clé étrangère : clé primaire d’une autre table utilisée pour créer une relation.

Métaphore :
Le numéro de carte d’identité est une clé primaire.
Lorsqu’il apparaît sur un contrat, il devient une clé étrangère.

(Sections G à L conservées intégralement)

### H. Les propriétés ACID

ACID est un acronyme qui définit les quatre propriétés essentielles garantissant la fiabilité des transactions dans une base de données.

#### A - Atomicité (Atomicity)

**Principe :** "Tout ou rien"

Une transaction est indivisible. Soit toutes les opérations réussissent, soit aucune n'est appliquée.

**Exemple concret :** Imaginons un virement bancaire de 100€ du compte A vers le compte B :
1. Débiter 100€ du compte A
2. Créditer 100€ au compte B

Si l'étape 2 échoue (panne électrique), l'atomicité garantit que l'étape 1 est annulée. On ne peut pas avoir un compte débité sans que l'autre soit crédité.

#### C - Cohérence (Consistency)

**Principe :** Les données restent valides

La base de données passe d'un état cohérent à un autre état cohérent, en respectant toutes les règles définies (contraintes, déclencheurs, etc.).

**Exemple concret :** Si une règle stipule qu'un compte ne peut pas être négatif, la cohérence garantit qu'aucune transaction ne violera cette règle.

#### I - Isolation (Isolation)

**Principe :** Les transactions sont indépendantes

Plusieurs transactions simultanées s'exécutent comme si elles étaient seules, sans s'influencer mutuellement.

**Exemple concret :** Si deux personnes consultent et modifient le même compte simultanément, l'isolation empêche qu'elles lisent des données "sales" (en cours de modification par l'autre).

#### D - Durabilité (Durability)

**Principe :** Les données sont permanentes

Une fois qu'une transaction est validée (commit), les modifications sont définitivement enregistrées, même en cas de panne système.

**Exemple concret :** Si vous validez un achat en ligne et que le serveur plante une seconde après, votre commande reste enregistrée.

---

## Concevoir une base de données : méthodes et modélisation

### I. Les méthodes Merise et UML

Il s'agit de méthodologies de modélisation permettant de concevoir et de documenter des systèmes d'information.

#### MERISE (Méthode d'Étude et de Réalisation Informatique pour les Systèmes d'Entreprise)

**Origine :** Méthode française développée dans les années 1970-1980

**Utilité :** Concevoir des bases de données et des systèmes d'information en séparant :
- Les **données** (ce que l'on stocke)
- Les **traitements** (ce que l'on fait avec)

**Les 3 niveaux de Merise :**

1. **Niveau conceptuel** : QUOI ? (vision métier)
   - MCD (Modèle Conceptuel de Données)
   - MCT (Modèle Conceptuel de Traitements)

2. **Niveau logique/organisationnel** : QUI, OÙ, QUAND ?
   - MLD (Modèle Logique de Données)
   - MOT (Modèle Organisationnel de Traitements)

3. **Niveau physique** : COMMENT ?
   - MPD (Modèle Physique de Données)

**Langage associé :** Merise génère principalement du **code SQL** pour créer les tables et structures de bases de données relationnelles.

**Cas d'utilisation concret :** Conception d'une base de données pour une bibliothèque

**Exemple de MCD (Modèle Conceptuel de Données) :**

```
┌─────────────┐              ┌─────────────┐
│   LECTEUR   │              │    LIVRE    │
├─────────────┤              ├─────────────┤
│ id_lecteur  │              │ id_livre    │
│ nom         │   emprunter  │ titre       │
│ prenom      │─────(0,N)────│ auteur      │
│ email       │   (0,5)      │ ISBN        │
└─────────────┘              └─────────────┘
                  │
                  │ date_emprunt
                  │ date_retour
                  ▼
            [EMPRUNT]
```

**Transformation du MCD en tables SQL (MPD) :**

```
Table: LECTEUR                    Table: LIVRE
┌─────────────┐                  ┌─────────────┐
│ id_lecteur  │ (PK)             │ id_livre    │ (PK)
│ nom         │                  │ titre       │
│ prenom      │                  │ auteur      │
│ email       │                  │ ISBN        │
└─────────────┘                  └─────────────┘
       │                                │
       │                                │
       └────────────┬───────────────────┘
                    │
            Table: EMPRUNT
            ┌─────────────┐
            │ id_emprunt  │ (PK)
            │ id_lecteur  │ (FK)
            │ id_livre    │ (FK)
            │ date_emprunt│
            │ date_retour │
            └─────────────┘
```

**Légende MCD :**
- Les rectangles = Entités (objets métier)
- Les losanges = Relations (associations)
- **(0,N)** et **(0,5)** = **Cardinalités** : définissent combien de fois une entité peut être associée à une autre. Notation (minimum, maximum). Exemples : (0,1) = zéro ou un, (1,1) = exactement un, (0,N) = zéro à plusieurs, (1,N) = un à plusieurs.
- PK = Primary Key (clé primaire)
- FK = Foreign Key (clé étrangère)

#### UML (Unified Modeling Language)

**Origine :** Standard international développé dans les années 1990

**Utilité :** Modéliser des systèmes orientés objet (logiciels, applications) avec **13 types de diagrammes** différents regroupés en 3 catégories :
- **Diagrammes structurels** (classes, objets, composants, déploiement...)
- **Diagrammes comportementaux** (cas d'utilisation, activités, états...)
- **Diagrammes d'interaction** (séquence, communication, timing...)

**Langages associés :** UML génère du **code orienté objet** dans des langages comme **Python, Java, C++, C#, JavaScript, PHP**, etc.

**Cas d'utilisation concret :** Modélisation d'un système de gestion de bibliothèque

**Exemple : Diagramme de classes UML**

```
┌─────────────────────────┐              ┌─────────────────────────┐
│       Lecteur           │              │         Livre           │
├─────────────────────────┤              ├─────────────────────────┤
│ - id: int               │              │ - id: int               │
│ - nom: string           │   emprunte   │ - titre: string         │
│ - email: string         │─────1..*─────│ - auteur: string        │
│ - livresEmpruntes: List │     0..5     │ - disponible: boolean   │
├─────────────────────────┤              ├─────────────────────────┤
│ + emprunter(livre)      │              │ + estDisponible(): bool │
│ + retourner(livre)      │              │ + reserver(): bool      │
│ + getNbEmprunts(): int  │              │ + liberer(): void       │
└─────────────────────────┘              └─────────────────────────┘
```

**Transformation en structure orientée objet :**

```
Application orientée objet
┌─────────────────────────────────────┐
│                                     │
│  Objet: lecteur1                    │
│  ┌───────────────────────┐          │
│  │ id = 1                │          │
│  │ nom = "Dupont"        │          │
│  │ livresEmpruntes = []  │──────┐   │
│  └───────────────────────┘      │   │
│                                 │   │
│  Méthodes disponibles:          │   │
│  • lecteur1.emprunter(livre)    │   │
│  • lecteur1.retourner(livre)    │   │
│                                 │   │
│                                 ▼   │
│  Objet: livre1                      │
│  ┌───────────────────────┐          │
│  │ id = 1                │          │
│  │ titre = "1984"        │          │
│  │ disponible = true     │          │
│  └───────────────────────┘          │
│                                     │
│  Méthodes disponibles:              │
│  • livre1.estDisponible()           │
│  • livre1.reserver()                │
│                                     │
└─────────────────────────────────────┘
```

**Légende diagramme de classes :**
- `-` = attribut privé (accessible uniquement dans la classe)
- `+` = méthode publique (accessible de l'extérieur)
- `1..*` = multiplicité (un lecteur emprunte 1 à plusieurs livres)
- `0..5` = un livre peut être emprunté par 0 à 5 lecteurs maximum

#### Différences conceptuelles entre Merise et UML

| Critère | Merise | UML |
|---------|--------|-----|
| **Paradigme** | Approche systémique (données + traitements séparés) | Approche orientée objet (données + comportements encapsulés) |
| **Philosophie** | Séparer les données des traitements | Regrouper données et méthodes dans des classes |
| **Cible principale** | Conception de bases de données relationnelles | Modélisation de logiciels et applications |
| **Langage généré** | SQL (tables, requêtes) | Python, Java, C++, C#, etc. (classes) |
| **Notation relations** | Cardinalités (0,N) | Multiplicités (0..*) |
| **Démarche** | Descendante : du général (conceptuel) au particulier (physique) | Plus flexible : plusieurs vues complémentaires |
| **Nombre de modèles** | 3 niveaux principaux (MCD, MLD, MPD) | 13 types de diagrammes différents |
| **Zone géographique** | Principalement utilisé en France | Standard international |
| **Point fort** | Structure des données persistantes | Architecture complète d'une application |

#### Complémentarité Merise et UML

Dans la pratique, les deux méthodes sont souvent utilisées ensemble dans un projet.

**Schéma de complémentarité :**

```
            PROJET COMPLET
            ══════════════
                  │
        ┌─────────┴─────────┐
        │                   │
    MERISE              UML
    (Données)      (Application)
        │                   │
        ▼                   ▼
  Tables SQL         Classes POO
 ┌──────────┐      ┌──────────┐
 │ Lecteur  │      │ Lecteur  │
 │ Livre    │◄─────│ Livre    │
 │ Emprunt  │ lit  │          │
 └──────────┘      └──────────┘
   (stockage)      (traitement)
```

**Workflow typique :**

1. **Merise** → Conception de la structure de la base de données (SQL)
   - Créer les tables
   - Définir les relations
   - Assurer la cohérence des données

2. **UML** → Conception de l'application (Python/Java/C++) qui utilise cette base
   - Créer les classes
   - Définir les comportements
   - Gérer les interactions

**Exemple concret :**
- Merise crée les tables `Lecteur`, `Livre`, `Emprunt` dans PostgreSQL/MySQL
- UML crée les classes Python `Lecteur` et `Livre` qui effectuent des requêtes sur ces tables

**En résumé :**
- **Merise + SQL** = Structure et persistance des données
- **UML + POO** = Logique applicative et comportements
- **Les deux ensemble** = Application complète fonctionnelle

---

### J. Définition du langage SQL & commandes de base

**SQL** = Structured Query Language (Langage de Requête Structuré)

Il s'agit d'un langage standardisé utilisé pour gérer et manipuler des bases de données relationnelles. SQL permet de :
- Créer et modifier la structure des bases de données
- Interroger les données (recherche, filtrage)
- Insérer, modifier et supprimer des données
- Gérer les droits d'accès et la sécurité

#### Les commandes SQL les plus utilisées

#### Les 4 catégories de commandes SQL

SQL se divise en 4 sous-langages selon le type d'opération :

| Catégorie | Objectif | Commandes principales |
|-----------|----------|----------------------|
| **DQL** - Data Query Language | Interroger les données | `SELECT` |
| **DML** - Data Manipulation Language | Manipuler le contenu | `INSERT`, `UPDATE`, `DELETE` |
| **DDL** - Data Definition Language | Définir la structure | `CREATE`, `ALTER`, `DROP` |
| **DCL** - Data Control Language | Gérer les droits | `GRANT`, `REVOKE` |

#### SELECT - Interroger les données

```sql
-- Sélection simple
SELECT nom, prenom FROM clients;

-- Avec condition
SELECT * FROM produits WHERE prix > 50;

-- Avec tri
SELECT * FROM clients ORDER BY nom ASC;

-- Avec limitation
SELECT * FROM produits LIMIT 10;
```

**Fonctions d'agrégation courantes :**

```sql
SELECT COUNT(*) FROM commandes;        -- Compter
SELECT AVG(prix) FROM produits;        -- Moyenne
SELECT SUM(montant) FROM ventes;       -- Somme
SELECT MAX(prix), MIN(prix) FROM produits;  -- Max/Min

-- Groupement
SELECT ville, COUNT(*) 
FROM clients 
GROUP BY ville 
HAVING COUNT(*) > 10;
```

#### INSERT - Insérer des données

```sql
INSERT INTO clients (nom, prenom, email) 
VALUES ('Martin', 'Julie', 'julie@mail.fr');
```

#### UPDATE - Modifier des données

```sql
UPDATE produits 
SET prix = prix * 1.1 
WHERE categorie = 'Electronique';
```

**Attention :** Toujours utiliser `WHERE` pour éviter de modifier toutes les lignes.

#### DELETE - Supprimer des données

```sql
DELETE FROM commandes 
WHERE date < '2023-01-01';
```

**Attention :** Toujours utiliser `WHERE` pour éviter de supprimer toutes les lignes.

#### CREATE - Créer des structures

```sql
CREATE TABLE produits (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    prix DECIMAL(10,2),
    stock INT DEFAULT 0
);
```

#### ALTER - Modifier la structure

```sql
ALTER TABLE produits ADD COLUMN description TEXT;
```

#### DROP - Supprimer définitivement

```sql
DROP TABLE produits;  -- Opération irréversible
```

### L. Les différentes jointures SQL

Les jointures permettent de combiner des données de plusieurs tables en fonction d'une relation commune.

#### Tables d'exemple

```
Table: CLIENTS                    Table: COMMANDES
┌────┬─────────┬────────┐        ┌────┬───────────┬─────────┐
│ id │ nom     │ ville  │        │ id │ client_id │ montant │
├────┼─────────┼────────┤        ├────┼───────────┼─────────┤
│ 1  │ Dupont  │ Paris  │        │ 1  │ 1         │ 100     │
│ 2  │ Martin  │ Lyon   │        │ 2  │ 1         │ 200     │
│ 3  │ Bernard │ Nice   │        │ 3  │ 2         │ 150     │
└────┴─────────┴────────┘        └────┴───────────┴─────────┘
```

#### 1. INNER JOIN (Jointure interne)

**Principe :** Retourne uniquement les lignes qui ont une correspondance dans les deux tables.

```sql
SELECT clients.nom, commandes.montant
FROM clients
INNER JOIN commandes ON clients.id = commandes.client_id;
```

**Résultat :**

```
┌─────────┬─────────┐
│ nom     │ montant │
├─────────┼─────────┤
│ Dupont  │ 100     │
│ Dupont  │ 200     │
│ Martin  │ 150     │
└─────────┴─────────┘
```

Note : Bernard n'apparaît pas car il n'a aucune commande.

**Représentation ensembliste :** Intersection (A ∩ B)

#### 2. LEFT JOIN (Jointure gauche)

**Principe :** Retourne toutes les lignes de la table de gauche, avec ou sans correspondance dans la table de droite.

```sql
SELECT clients.nom, commandes.montant
FROM clients
LEFT JOIN commandes ON clients.id = commandes.client_id;
```

**Résultat :**

```
┌─────────┬─────────┐
│ nom     │ montant │
├─────────┼─────────┤
│ Dupont  │ 100     │
│ Dupont  │ 200     │
│ Martin  │ 150     │
│ Bernard │ NULL    │
└─────────┴─────────┘
```

Note : Bernard apparaît avec NULL car il n'a aucune commande.

**Représentation ensembliste :** A + (A ∩ B)

#### 3. RIGHT JOIN (Jointure droite)

**Principe :** Retourne toutes les lignes de la table de droite, avec ou sans correspondance dans la table de gauche.

**Représentation ensembliste :** (A ∩ B) + B

#### 4. FULL OUTER JOIN (Jointure complète)

**Principe :** Retourne toutes les lignes des deux tables, avec ou sans correspondance.

Note : Non supporté directement par MySQL. Il est nécessaire d'utiliser une UNION de LEFT et RIGHT JOIN.

**Représentation ensembliste :** Union complète (A ∪ B)

#### 5. CROSS JOIN (Produit cartésien)

**Principe :** Combine chaque ligne de la première table avec chaque ligne de la seconde table.

**Résultat :** Pour 3 clients et 3 commandes, on obtient 9 lignes (3 × 3).

Attention : Cette opération génère rapidement un très grand nombre de lignes.

#### 6. SELF JOIN (Auto-jointure)

**Principe :** Joindre une table avec elle-même.

**Cas d'usage typique :** Table employés avec une hiérarchie (employé/manager).

```sql
SELECT e1.nom AS employe, e2.nom AS manager
FROM employes e1
LEFT JOIN employes e2 ON e1.manager_id = e2.id;
```
## 9. Lexique simplifié
ACID : Propriétés garantissant la fiabilité des transactions.
Atomicité : Transaction indivisible.
Cohérence : Respect des règles métiers.
Isolation : Transactions indépendantes.
Durabilité : Données persistantes après validation.

Base de données : Ensemble structuré de données persistantes.
Data Lake : Stockage de données brutes.
Data Warehouse : Base optimisée pour l’analyse décisionnelle.
Lakehouse : Architecture hybride entre Lake et Warehouse.

SGBD : Logiciel de gestion des bases de données.
SQL : Langage standard d’interrogation des bases relationnelles.
Clé primaire : Identifiant unique.
Clé étrangère : Lien entre deux tables.
Jointure : Opération reliant plusieurs tables.
Merise : Méthode de modélisation orientée données.
UML : Langage de modélisation orienté objet.
```
