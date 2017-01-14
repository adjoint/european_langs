import difflib
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

f = open("French.txt", "r")
g = open("German.txt", "r")
s = open("Spanish.txt", "r")
p = open("Portuguese.txt", "r")
i = open("Italian.txt", "r")

french = f.readlines()
german = g.readlines()
spanish = s.readlines()
portuguese = p.readlines()
italian = i.readlines()

header_str = "###########################################################################\n"

def findSimilarityToEnglish(language):
	counter = 0
	total = 0
	header_counter = 0
	for line in language:
		if header_counter == 2:
			line = line.strip("\n")
			lst = line.split("\t")
			eng = lst[0].lower()
			fgn = lst[1].lower()
			fgn = fgn.split("[")[0].split("(")[0].split(",")[0].replace(",", "").replace(".", "").replace("\xe4", "")
			similarity = similar(eng, fgn)
			counter += 1
			total += similarity
		else:
			if line == header_str:
				header_counter += 1
	return (similarity/float(counter))*100000

sf = findSimilarityToEnglish(french)
sg = findSimilarityToEnglish(german)
ss = findSimilarityToEnglish(spanish)
sp = findSimilarityToEnglish(portuguese)
si = findSimilarityToEnglish(italian)

print "Similarity of French to English: " + str(sf)
print "Similarity of German to English: " + str(sg)
print "Similarity of Spanish to English: " + str(ss)
print "Similarity of Portuguese to English: " + str(sp)
print "Similarity of Italian to English: " + str(si)