# reverse dna, copy

dna = "ACTTGCTAATCGATAATCGG"

compl_dna=[]
for element in dna:
    if element == "A":
        compl_dna.append("T")
    elif element == "C":
        compl_dna.append("G")
    elif element == "G":
        compl_dna.append("C")
    else:
        compl_dna.append("A")
      

compl_dna = compl_dna[::-1]
result = ''.join(compl_dna)
print(result)
