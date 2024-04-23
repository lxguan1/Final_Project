#!/bin/bash


for i in {1..22};
do
	plink --vcf ../vcf_files/chr${i}.vcf.gz --cm-map ../data/genetic_map_chr${i}_combined_b37.txt ${i} --keep plink_folders/plink_files_${1}/inds.txt --make-bed --out plink_folders/plink_files_${1}/chr${i}_cm;
done