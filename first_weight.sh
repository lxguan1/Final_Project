#!/bin/bash


for i in {1..22};
do
	plink --vcf vcf_files/chr${i}.vcf.gz --cm-map data/genetic_map_chr${i}_combined_b37.txt ${i} --keep eur_inds.txt --extract <GWASNAME> --make-bed --out <GWASFOLDER>/chr${i}_cm;
done