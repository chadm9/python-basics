m1 = [[1, 2], [3, 5]]
m2 = [[3, 6], [6, 9]]
result = [[None, None], [None, None]]
for i in range(0, 2):
    for j in range(0, 2):
        result[i][j] = (m1[i][j] +m2[i][j])

print m1, m2, result 
