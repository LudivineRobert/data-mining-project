#!/bin/bash
#lignes de commandes pour mining spmf

## ------------- FPGrowth itemsets
# minsup: 40%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encode.txt output_spmf_item_fpg_40.txt 0.40

# minsup: 50%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encode.txt output_spmf_item_fpg_50.txt 0.50

# minsup: 60%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encode.txt output_spmf_item_fpg_60.txt 0.60

# minsup: 70%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encode.txt output_spmf_item_fpg_70.txt 0.70

# minsup: 80%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encode.txt output_spmf_item_fpg_80.txt 0.80

# minsup: 90%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encode.txt output_spmf_item_fpg_90.txt 0.90
