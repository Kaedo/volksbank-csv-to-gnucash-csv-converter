#!/bin/bash
python3 parse-vb-csv.py *.csv | sort -n -t"." -k3 -k2 -k1
