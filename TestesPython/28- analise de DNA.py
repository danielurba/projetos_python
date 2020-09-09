sample = ['GTA','GGG','CAC']

def readdna(dnafile):
    dnadata = ""
    with open(dnafile, "r") as f:
        for line in f:
            dnadata += line
    return dnadata

def dnacodons(dna):
    codons = []
    for i in range(0,len(dna), 3):
        if (i + 3) < len(dna):
            codons.append(dna[i:i+3])
    return codons

def matchdna(dna):
    matches = 0
    for codon in dna:
        if codon in sample:
            matches += 1
            return matches
    print(matches)

def iscriminal(dnasample):
    dnadata = readdna(dnasample)
    codons = dnacodons(dnadata)
    nummatches = matchdna(codons)
    if nummatches >= 3:
        print("O codigo foi achado: %s. Investigação continua," % (nummatches))
    else:
        print("supeito liberado")

iscriminal("suspect1.txt")
iscriminal("suspect2.txt")
iscriminal("suspect3.txt")
