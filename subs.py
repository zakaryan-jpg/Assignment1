# subs
 
s = "GGTCCGCCGCTTTGTCCGCCGCGAAGCGTCCGCCGTCCGCCGTCCGCCGTTCCGCCGAATCCGCCGACCTTCTCCGCCGCATGCCATCCGCCGCATCCGCCGCGCTTCCGCCGGTAACCGGTCCGCCGCATCCGCCGCTTGTCCGCCGTCCGCCGGCTCCGCCGTTCCGCCGCTCCGCCGTCCGCCGTCTATTTCTCCGCCGAAATTCCGCCGGTAAGTATTAGACTCCGCCGTCCGCCGCGGTCCGCCGGCTTCCGCCGGCCCTCCGCCGTAAAAAAATCCGCCGTCCTCCGCCGCAATCCGCCGTCCGCCGTTCCGCCGTCCGCCGCCTCGCTCCGCCGTAGTCCGCCGTCCGCCGTCCGCCGCTCCGCCGAGTACAAACGATCTCCGCCGCGTCCGCCGTCCGCCGTTCTAATTTCCGCCGGGTCCGCCGCCTCCGCCGGTGTCCGCCGATCCGCCGCCATCCGCCGCGATCCGCCGGGCTATCCTCCGCCGTTCCGCCGATGATTCCGCCGCTCAAGGGTCTCCGCCGTATCCGCCGTCCGCCGTCCGCCGCTCCGCCGTGTGACTCCGCCGCCAACGTTCCGCCGACGAATTCCGCCGATCCGCCGTCTTCCGCCGTCCGCCGTGTATTCCGCCGCCTCCGCCGGTTCTCCGCCGGTGCCTAATCCGCCGTCCGCCGCATCCGCCGGTCGCGAGGCTTGCCCCTTCCGCCGGGCTCCGCCGAGTCCGCCGTTCCGCCGTTCCGCCGTTGCCTTTCCGCCGTTCCGCCGCATTTTCCGCCGCTTCCGCCGATCCGCCGGAATCCGCCGTCCGCCGGTACTCCGCCGTCCGCCGTCCGCCGTCATCCGCCGCTTCCGCCGGTCCGCCGTCCGCCGGTCCGCCGGACTCTCCGCCGAACTCCGCCGGTGTTCCGCCGGTCCGCCGACATGATCCGCCGTGCTCCGCCGTCCGCCGTCCGCCGAGTCCGCCGCGCTGCCATCCGCCG"
t = "TCCGCCGTC"

def motif(s, t):
    location = []
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            location.append(i+1)
    location = " ".join (map(str, location))
    return location

print(motif(s, t))