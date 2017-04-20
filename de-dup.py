lyst = [1, 3, 5, 't', 'p', 1, 4, 'p']
duplicate = []
print lyst
for i in range(len(lyst)):
    for j in range(len(lyst)):
        if lyst[i] == lyst[j] and i < j:
            duplicate.append(lyst[j]) 

for element in duplicate:
    lyst.remove(lyst[lyst.index(element)])

print lyst
