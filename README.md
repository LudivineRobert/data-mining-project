## UE901 EC2 Data Mining - Practical word
## Itemset and Association Rules Mining (données : GrandEst)

**Asmaa DEMNY & Cécile MACAIRE & Ludivine ROBERT**


## Contexte
Ce projet a été réalisé dans le cadre d'un cours de fouille de données au programme du Master 2 en Traitement Automatique des Langues à l'Université de Lorraine (Nancy).

Ce répertoire contient tous les fichiers nécessaires au projet. Vous trouverez ci-dessous une description de base, ainsi que les instructions et commandes d'exécution des scripts d'encodage et de décodage.

## Prérequis

Pour commencer, veuillez cloner le répertoire par la ligne de commande:

```bash
git clone git@github.com:macairececile/data-mining-project.git
```

Vous aurez également besoin du fichier de données ```GrandEst``` au format ```.txt``` et de l'archive ```spmf.jar``` pour les différents algorithmes à copier dans le même répertoire. 

#### Librairies nécessaires

- pandas
- csv
- pickle

## 1. Encodage du fichier de données pour SPMF

Pour encoder le fichier de données, lancer la commande suivante:

```bash
python encode_SPMF.py -f GrandEst.txt
```
Le fichier ```GrandEst_filter.txt``` comprendra les données filtrées, c'est à dire les données provenant des attributs que nous avons fait le choix de garder.
Le fichier encodé ```GrandEst_encode.txt``` sera généré ainsi que le dictionnaire comprenant l'encodage ```dictionnaire.pickle```.

## 2. Mining avec SPMF

Pour extraire les itemsets fréquents, veuillez lancer la ligne de commande suivante:

```bash
sh commandes_Itemset_SPMF.sh
```

Les résultats sont déjà disponibles dans **resultats_spmf/Itemset/**.

Pour extraire les règles d'association, veuillez lancer la ligne de commande suivante:

```bash
sh commandes_AssRules_SPMF.sh
```

Les résultats sont déjà disponibles dans **resultats_spmf/AssociationRules/**.

## 3. Décodage des fichiers générés par SPMF

Afin de décoder les fichiers générés par spmf, lancer la commande suivante:

```bash
python decode_SPMF.py -f res.txt
```

Veuillez à bien avoir le fichier ```dictionnaire.pickle``` pour que le décodage puisse de réaliser.
```res.txt``` correspond au fichier à décoder. 

Les fichiers décodés sont déjà disponible dans les dossiers **resultats_decode/Itemset/** et **resultats_decode/AssociationRules/** pour les itemsets fréquents et les règles d'association, respectivement.

## 4. Analyse des résultats

Enfin, l'étude de certains itemsets et règles d'association se trouve dans le fichier ```DataMining_rapport.pdf```.
