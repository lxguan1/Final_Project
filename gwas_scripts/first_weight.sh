#!/bin/bash

# ${1} is the GWAS folder 

mkdir ../${1}/plink_files
mkdir ../${1}/gcta_output

for i in {1..22};
do
	plink --vcf ../vcf_files/chr${i}.vcf.gz --cm-map ../data/genetic_map_chr${i}_combined_b37.txt ${i} --keep ../eur_inds.txt --extract ../${1}/variants.txt --make-bed --out ../${1}/plink_files/chr${i}_cm;
	gcta64 --bfile ../${1}/plink_files/chr${i}_cm --ld-score --ld-wind 1000 --ld-rsq-cutoff 0 --ld-score-adj --out ../${1}/gcta_output/chr${i} --maf 0.00001 --thread-num 22
done