#!/bin/bash

for i in {1..22};
do
	plink --vcf vcf_files/chr${i}.vcf.gz --cm-map data/genetic_map_chr${i}_combined_b37.txt ${i} --keep eur_inds.txt --make-bed --out plink_files/chr${i}_cm;
done