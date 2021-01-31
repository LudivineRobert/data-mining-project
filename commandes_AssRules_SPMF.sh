#!/bin/bash
#lignes de commandes pour les règles d'associations avec SPMF

# minsup 20% minconf 20%
java -jar spmf.jar run FPGrowth_association_rules GrandEst_encode.txt output_asr_sup20_conf20.txt 20% 20%

# minsup 40% minconf 30%
java -jar spmf.jar run FPGrowth_association_rules GrandEst_encode.txt output_asr_sup40_conf30.txt 40% 30%

# minsup 80% minconf 60%
java -jar spmf.jar run FPGrowth_association_rules GrandEst_encode.txt output_asr_sup80_conf60.txt 80% 60%

# minsup 80% minconf 80%
java -jar spmf.jar run FPGrowth_association_rules GrandEst_encode.txt output_asr_sup80_conf80.txt 80% 80%

# minsup 80% minconf 90%
java -jar spmf.jar run FPGrowth_association_rules GrandEst_encode.txt output_asr_sup80_conf90.txt 80% 90%


