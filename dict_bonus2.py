def letter_histogram(word):
    histo = {}
    for i in word:
        if not histo.has_key(i):
            histo[i] = 1
        else:
            histo[i] += 1
            
    return histo 

list1 = [1,45,65,4,45,"Jim",1,"Jim",3,4,1,1,'True',3,45,4,1,"The Beetles",9]
conversion = {1: 'one', 2: 'two', 3: 'three', 4: 'four' , 5: 'five'}
histo  = letter_histogram(list1)
dikt = {'one':[], 'two': [], 'three': [], 'four': [], 'five': [] } 
lyst = []
for key in histo:
    lyst.append([key, histo[key]])
lyst.sort(key=lambda x: x[1]) 




for i in lyst:
    dikt[conversion[i[1]]].append(i[0])

#dikt = sorted(dikt)

print dikt 
