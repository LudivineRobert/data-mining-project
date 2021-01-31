#!/usr/bin/env python
# coding: utf-8

f = 'decode_output_asr_sup20_conf20.txt'

def resultats_decroissant(file):
    with open(file, 'r') as f:
        data = {}
        lines = f.readlines()
        for i in lines:
            if i != '\n':
                conf = float(i.split('CONF: ')[1][:-1])
                data[i] = conf
        decreased = {k: v for k, v in sorted(data.items(), key=lambda item: item[1])}
    str = ''
    for k in decreased.keys():
        str += k
    print(str)


def resultats_paritems(file):
    with open(file, 'r') as f:
        data = {}
        lines = f.readlines()
        for i in lines:
            if i != '\n':
                if 'DIPL15' in i: # a modifier en fonction de l'item que vous voulez observer
                    print(i)


if __name__ == '__main__':
    #resultats_decroissant(f)
    resultats_paritems(f)
