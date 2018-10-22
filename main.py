# Load libraries
import typing
from efficient_apriori import apriori
import argparse

# Command line Arguments
parser = argparse.ArgumentParser(description='Apriori.')
parser.add_argument('-n', help='Normalize data', default=False)
args = parser.parse_args()
normalize = bool(args.n)

# Get all available items
file = open("../xyz.data", "r")
lines: typing.List[str] = file.readlines()

# Removing special characters
for i in range(len(lines)):
    lines[i] = lines[i] \
        .replace("Ç", "C") \
        .replace("Ã", "A") \
        .replace("Õ", "O") \
        .replace("Á", "A") \
        .replace("É", "E") \
        .replace("Ú", "U") \
        .replace("Â", "A") \
        .replace("\n", "")

data = list(map(lambda x: x.split(" "), lines))

# Attempting some normalization
if normalize:
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j].startswith("PAPEL_HIG"):
                data[i][j] = "PAPEL_HIG"
            if data[i][j].startswith("VELA"):
                data[i][j] = "VELA"
            if data[i][j].startswith("TRIGO"):
                data[i][j] = "TRIGO"
            if data[i][j].startswith("TORRADA"):
                data[i][j] = "TORRADA"
            if data[i][j].startswith("TOALHA_PAPEL"):
                data[i][j] = "TOALHA_PAPEL"
            if data[i][j].startswith("SCLIXO"):
                data[i][j] = "SCLIXO"
            if data[i][j].startswith("SCLIXO"):
                data[i][j] = "SCLIXO"
            # ... The list could go on...

items = sorted(set(" ".join(list(map(lambda x: " ".join(x), data))).split(" ")))

# running alg
itemsets, rules = apriori(data,
                          min_confidence=0.3,  # Min chance of B when A
                          min_support=0.02)  # Min % of transactions containing item

for rule in sorted(rules, key=lambda r: r.lift):
    print(rule)
