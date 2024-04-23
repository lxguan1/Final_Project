#!/bin/bash

for i in {1..378}
do
	python3 extract_jackknife.py ${i}
	./plink_jackknife.sh ${i}
	./gcta_jackknife.sh ${i}
done
python3 calculate_sterr.py