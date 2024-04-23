#!/bin/bash

for pop in 'CEU' 'GBR' 'TSI' 'FIN'
do
	for i in {1..22};
	do
		gcta64 --bfile plink_files_${pop}/chr${i}_cm --ld-score --ld-wind 1000 --ld-rsq-cutoff 0 --ld-score-adj --out gcta_output_1000_${pop}/chr${i} --maf 0.00001 --thread-num 22
	done
done