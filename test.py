m1 = [[1, 2, 3], [3, 5, 3], [2, 2, 2]]
m2 = [[3, 6, 3], [6, 9, 7], [0, 0, 1]]
#result = [[None, None], [None, None]]
result = []
for i in range(len(m1)):
    result.append([])

print result

for i in range(len(m1)):
    for j in range(len(m1[0])):
        result[i].append(None)

print result

for i in range(len(m1)):
    for j in range(len(m1)):
        result[i][j] = (m1[i][j] +m2[i][j])

print m1, m2, result 
