# Projet: Data Mining sur les données Grand Est

Ce projet a été réalisé par Ludivine Robert, Asmaa Demny et Cécile Macaire dans le cadre du cours UE901 EC2 de Yannick Toussaint, M2 NLP à l'Université de Lorraine. 

## Prérequis

Pour commencer, veuillez cloner le répertoire par la ligne de commande:

```bash
git clone git@github.com:macairececile/data-mining-project.git
```

Vous aurez également besoin du fichier de données GrandEst au format .txt et de l'archive spmf.jar pour les différents algorithmes à copier dans le même répertoire. 

#### Librairies nécessaires

- pandas
- csv
- pickle

## 1. Encodage du fichier de données pour SPMF

Pour encoder le fichier de données, lancer la commande suivante:

```bash
python encode_SPMF.py -f GrandEst.txt
```
Le fichier _GrandEst_filter.txt_ comprendra les données filtrées, c'est à dire les données provenant des attributs que nous avons fait le choix de garder.
Le fichier encodé _GrandEst_encode.txt_ sera généré ainsi que le dictionnaire comprenant l'encodage _dictionnaire.pickle_.

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

Veuillez à bien avoir le fichier _dictionnaire.pickle_ pour que le décodage puisse de réaliser.
_res.txt_ correspond au fichier à décoder. 

Les fichiers décodés sont déjà disponible dans les dossiers **resultats_decode/Itemset/** et **resultats_decode/AssociationRules/** pour les itemsets fréquents et les règles d'association, respectivement.

## 4. Analyse des résultats
