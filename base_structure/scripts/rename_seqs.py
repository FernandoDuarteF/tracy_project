import sys
import os

path = sys.argv[1]

files = os.listdir(path)

for name in files:
    new = name.split("_")
    new = new[0:4]
    #n = n[0:4]
    if new[-1:] == ["R1"]:
        new[-1:] = "1"
    else:
        new[-1:] = "2"
    new = "_".join(new) + ".fastq.gz"
    os.rename(path + name, path + new)

