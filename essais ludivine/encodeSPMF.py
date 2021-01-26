#!/usr/bin/env python
# coding: utf-8
# Usage : python <File-to-encode> <encoded-file>
# Usage : python <File-to-encode> (write in GrandEst_encoded_for_SPMF.txt)


import pandas
import csv
import sys
import pickle


p=len(sys.argv)
print(p)

if p==3:
    f_out=sys.argv[2]
else:
    f_out="GrandEst_encoded_for_SPMF.txt"
    
# lire fichier CSV
f_in=sys.argv[1]
csv_df = pandas.read_csv(f_in,sep=';',low_memory=False)
    
# éliminer les colonnes des variables non utilisées
list_2_drop = ['ACHLR','AEMM','AEMMR','AGED','AGEREV','AGEREVQ','ANAI','ANARR','ANEM','ANEMR','APAF','ASCEN',
                'BAIN','BATI',
                'CATL','CATPC','CHAU','CHFL','CHOS','CLIM','CMBL','COUPLE','CS2','CS3','CUIS',
                'DEPT','DEROU',
                'EAU','EGOUL','ELEC','EPCI','ETUD',
                'GARL','HLML','ILETUD','ILETUU','ILTUU','ILT',
                'IMMI','INAI','INFAM','INPER','INPERF','IPONDI','IRAN','IRANUU',
                'LIENF','LPRF','LPRM',
                'METRODOM','MOCO',
                'NA38','NA88','NAF08','NAIDT','NAT13','NAT49','NATC','NATN49','NATNC','NUMF','NUMMR',
                'ORIDT',
                'PNAI12','PROF',
                'RECH',
                'SANI','SANIDOM','SFM','STAT','STAT_CONJ',
                'TACTD16','TP','TRANS','TYPC','TYPFC','TYPMD','TYPMR','UR','VOIT','WC']
new_csv_df = csv_df.drop(list_2_drop, axis=1)
# sauvegarder la nouvelle dataframe 
new_csv_df.to_csv(r'GrandEst_filtre.csv',index = None, header=None)

 # transformer le fichier CSV en TXT
with open("GrandEst_filtre.txt","w+") as output_file:
    with open("GrandEst_filtre.csv","r") as input_file:
        [output_file.write(" ".join(row)+'\n') for row in csv.reader(input_file)]
        output_file.close()
        
# Construction du dictionnaire
dico={}
invdico={}
indice=1
f=open("GrandEst_filtre.txt",'r')
for line in f.readlines():
    line=line.rstrip()
    print(line)
    for i,e in enumerate(line.split(' ')):
        a=str(i)+"-"+e
        if a not in dico.keys():
            print(a)
            dico[a]=indice
            invdico[indice]=a
            indice +=1
f.close()

print(dico)


# Construction du fichier de donnees
out=open(f_out,'w')
f=open("GrandEst_filtre.txt",'r')
for line in f.readlines():
    line=line.rstrip()
    l=[]
 #   print line
    for i,e in enumerate(line.split(' ')):
        a=str(i)+"-"+e
        l.append(dico[a])
    l.sort()
    l2=[str(i) for i in l]


#    input("xxx :")
#    out.write
    #out.write("{"+",".join(l2)+"}")
    out.write(" ".join(l2))
    out.write("\n")
f.close()

fichier=open('invdico.dbm', 'wb')
pickle.dump(invdico,fichier)