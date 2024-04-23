#!/bin/bash

for pop in 'CEU' 'GBR' 'TSI' 'FIN'
do
	for i in {1..22};
	do
		plink --vcf vcf_files/chr${i}.vcf.gz --cm-map data/genetic_map_chr${i}_combined_b37.txt ${i} --keep ${pop}_inds.txt --make-bed --out plink_files_${pop}/chr${i}_cm;
	done
done