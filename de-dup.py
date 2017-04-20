lyst = [1, 3, 5, 't', 'p', 1, 4, 'p']

for i in range(len(lyst)-1):
    for j in range(len(lyst)-1):
        if lyst[i] == lyst[j] and i != j:
            lyst.remove(lyst.index(lyst[j]))

print lyst
