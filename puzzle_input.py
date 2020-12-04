import sys
from os import path

with open(f"{path.basename(sys.argv[0])[:2]}.txt") as f:
    lines = [line.strip() for line in f.readlines()]
    lines_int = [int(line) for line in lines if line.isnumeric()]
