import sys
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("-c","--checkm", help="check summary output")
parser.add_argument("-q","--quast", help="quast summary output")
parser.add_argument("-n","--N50", default = 40000, help="N50 treshold", type = int)
parser.add_argument("-a","--completness", default = 95, help="completness treshold", type = float)
parser.add_argument("-b","--contamination", default = 5, help="contamination treshold", type = float)

args = parser.parse_args()

checkm_summary = args.checkm
quast_summary = args.quast

if args.N50: #If value is given
    N50 = args.N50

if args.completness:
    comp = args.completness

if args.contamination:
    cont = args.contamination

with open(quast_summary) as f1, open(checkm_summary) as f2:
    f1.readline()
    quast_filtered = []
    checkm_filtered = []
    #f2.readline()
    for line in f1:
        line_l = line.split("\t")
        if float(line_l[-6]) >= N50:
            quast_filtered.append(line_l[0])

    for line in f2:
        for line in f2:
            line_l = line.split("\t")
            if float(line_l[-3]) >= comp and float(line_l[-2]) <= cont:
                checkm_filtered.append(line_l[0])

diff_set = set(quast_filtered) - set(checkm_filtered) #Shouldn't this be the other way around

seqs_pass = quast_filtered + list(diff_set) #Why do this (maybe beacuse I cannot merge both sets). Then you should try with set.intersection()

for i in seqs_pass:
    print(i)

f1.close()
f2.close()
#print(os.listdir("sequences"))

