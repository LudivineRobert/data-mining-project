#!/usr/bin/env python
# coding: utf-8

#### Libraries
import argparse

import pandas as pd
import csv
import pickle
import sys


def encode_file(name_file):
    # éliminer les colonnes des variables non utilisées
    list_2_drop = ['REGION', 'ACHLR', 'AEMM', 'AEMMR', 'AGED', 'AGEREV', 'AGEREVQ', 'ANAI', 'ANARR', 'ANEM', 'ANEMR',
                   'APAF', 'ASCEN',
                   'BAIN',
                   'CATL', 'CATPC', 'CHAU', 'CHFL', 'CHOS', 'CLIM', 'CMBL', 'COUPLE', 'CS2', 'CS3', 'CUIS',
                   'DEPT', 'DEROU',
                   'EAU', 'EGOUL', 'ELEC', 'EPCI', 'ETUD',
                   'GARL', 'HLML', 'ILETUD', 'ILETUU', 'ILTUU', 'ILT',
                   'IMMI', 'INAI', 'INFAM', 'INPER', 'INPERF', 'IPONDI', 'IRAN', 'IRANUU',
                   'LIENF', 'LPRF', 'LPRM',
                   'METRODOM', 'MOCO',
                   'NA38', 'NA88', 'NAF08', 'NAIDT', 'NAT13', 'NAT49', 'NATC', 'NATN49', 'NATNC', 'NUMF', 'NUMMR',
                   'ORIDT',
                   'PNAI12', 'PROF',
                   'RECH',
                   'SANI', 'SANIDOM', 'SFM', 'STAT', 'STAT_CONJ',
                   'TACTD16', 'TP', 'TRANS', 'TYPC', 'TYPFC', 'TYPMD', 'TYPMR', 'UR', 'VOIT', 'WC']
    # Lire le fichier entrée et le convertir en csv
    df = pd.read_csv(name_file, sep=';', low_memory=False)
    df_csv = df.drop(list_2_drop, axis=1)  # on élimine les colonnes non gardées
    txt_filter = df_csv.to_csv(r'GrandEst_filter.txt', index=None, sep=' ', mode='a')
    # Construction du fichier de données encodées
    dict_encode = {}
    indice = 1
    with open('GrandEst_filter.txt', 'r') as f:
        lines = f.readlines()
        values = []
        header = lines[0].split(' ')
        for l in lines[1:]:
            el = l.split(' ')
            enc_l = []
            for i, j in enumerate(el):
                enc = str(header[i]) + '_' + str(j)
                if enc not in dict_encode.keys():
                    dict_encode[enc] = indice
                    indice += 1
                    enc_l.append(indice)
                else:
                    enc_l.append(dict_encode[enc])
            enc_l.sort()
            values.append(enc_l)
        print(dict_encode)
    with open('GrandEst_encode.txt', 'w+') as ff:
        for a in values:
            l2 = [str(i) for i in a]
            ff.write(" ".join(l2))
            ff.write("\n")
    # Enregistrer le dictionnaire d'encodage
    with open('dictionnaire.pickle', 'wb') as handle:
        pickle.dump(dict_encode, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fichier', type=str,
                        help='Fichier en entrée: données GrandEst.txt')
    args = parser.parse_args()
    if len(sys.argv) <= 1:
        print("Vous devez spécifier le fichier de données en entrée.")
        exit(1)
    else:
        encode_file(args.fichier)


