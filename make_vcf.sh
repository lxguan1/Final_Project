#!/bin/bash

for i in {1..22};
do
	./plink2 --haps data/ALL_1000G_phase1integrated_v3_chr${i}_impute.hap.gz --legend data/ALL_1000G_phase1integrated_v3_chr${i}_impute.legend.gz ${i} --sample data/ALL_1000G_phase1integrated_v3.sample --export vcf bgz --out vcf_files/chr${i};
done