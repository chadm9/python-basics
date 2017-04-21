def letter_histogram(word):
    lyst = word.split(" ")
    histo = {}
    for i in lyst:
        if not histo.has_key(i):
            histo[i] = 1
        else:
            histo[i] += 1
            
    return histo 

paragraph = raw_input("Paragraph: ")
histo  = letter_histogram(paragraph)
lyst = []

for key in histo:
    lyst.append([key, histo[key]])
lyst.sort(key=lambda x: x[1]) 


print "1: " + lyst[-1][0], "\n2: " + lyst[-2][0] + "\n3: " + lyst[-3][0]

