#!/usr/bin/env python
# coding: utf-8
# Usage : python decode_SPMF.py file-to-decode
import argparse
import sys
import pickle


def decode(a, d):
    inv_map = {v: k for k, v in d.items()}
    for k,v in inv_map.items():
        if 'TYPL' in v:
            inv_map[k] = v.replace('\n', '')
    s = ''
    l = a.split()
    # print(l)
    for i in l:
        if i != ' ' and int(i) in inv_map.keys():
            s = s + inv_map[int(i)] + ' '
    # print(s)
    return s


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--fichier', type=str,
                        help='Fichier en entrée: résultats de spmf')
args = parser.parse_args()
if len(sys.argv) <= 1:
    print("Vous devez spécifier le fichier de données en entrée.")
    exit(1)
else:
    results = args.fichier
    f = open(results, 'r')
    # Construction du dictionnaire
    dic = open('dictionnaire.pickle', 'rb')
    d = pickle.load(dic)
    name_output_file = 'decode_'+results
    res = open(name_output_file, 'w')
    for l in f.readlines():
        r = l.split("#")
        #   print r
        aa = r[0].split(' ==> ')
        if len(aa) == 1:
            rdec = decode(aa[0], d)
            res.write(rdec + '# ' + '# '.join(r[1:]) + '\n')
        elif len(aa) == 2:
            rdec0 = decode(aa[0], d)
            rdec1 = decode(aa[1], d)
            res.write(rdec0 + '==> ' + rdec1 + '# ' + '# '.join(r[1:]) + '\n')
        else:
            print('!!!!! ligne non conforme')
    res.close()