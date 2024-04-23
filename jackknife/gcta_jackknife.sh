#!/bin/bash

for i in {1..22};
do
	gcta64 --bfile plink_folders/plink_files_${1}/chr${i}_cm --ld-score --ld-wind 1000 --ld-rsq-cutoff 0 --ld-score-adj --out gcta_folders/gcta_files_${1}/chr${i} --maf 0.00001 --thread-num 22
	rm -r plink_folders/plink_files_${1}/chr${i}_*
done