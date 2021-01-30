#!/bin/bash
#lignes de commandes pour mining spmf

## ------------- FPGrowth itemsets
# minsup: 15%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encode.txt output_spmf_item_fpg_15.txt 0.15

# minsup: 20%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encode.txt output_spmf_item_fpg_20.txt 0.20

# minsup: 25%
java -jar spmf.jar run FPGrowth_itemsets GrandEst_encode.txt output_spmf_item_fpg_25.txt 0.25

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
