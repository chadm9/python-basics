input = raw_input("Enter a string: ")
result = ''
for i in range(len(input)-1, -1, -1):
    result = result + input[i] 
print result
