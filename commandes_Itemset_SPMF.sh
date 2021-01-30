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

## ------------- APriori itemsets
# minsup: 40%
java -jar spmf.jar run Apriori GrandEst_encode.txt output_spmf_item_ap_40.txt 0.40

# minsup: 50%
java -jar spmf.jar run Apriori GrandEst_encode.txt output_spmf_item_ap_50.txt 0.50

# minsup: 60%
java -jar spmf.jar run Apriori GrandEst_encode.txt output_spmf_item_ap_60.txt 0.60

# minsup: 70%
java -jar spmf.jar run Apriori GrandEst_encode.txt output_spmf_item_ap_70.txt 0.70

# minsup: 80%
java -jar spmf.jar run Apriori GrandEst_encode.txt output_spmf_item_ap_80.txt 0.80

# minsup: 90%
java -jar spmf.jar run Apriori GrandEst_encode.txt output_spmf_item_ap_90.txt 0.90

## ------------- FPClose itemsets
# minsup: 40%
java -jar spmf.jar run Apriori GrandEst_encode.txt output_spmf_item_fpc_40.txt 0.40

# minsup: 50%
java -jar spmf.jar run Apriori GrandEst_encode.txt output_spmf_item_fpc_50.txt 0.50

# minsup: 60%
java -jar spmf.jar run Apriori GrandEst_encode.txt output_spmf_item_fpc_60.txt 0.60

# minsup: 70%
java -jar spmf.jar run Apriori GrandEst_encode.txt output_spmf_item_fpc_70.txt 0.70

# minsup: 80%
java -jar spmf.jar run Apriori GrandEst_encode.txt output_spmf_item_fpc_80.txt 0.80

# minsup: 90%
java -jar spmf.jar run Apriori GrandEst_encode.txt output_spmf_item_fpc_90.txt 0.90







