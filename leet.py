translation = {'A': '4', 'E': '3', 'G': '6', 'I': '1', 'O': '0', 'S': '5', 'T': '7'}
input = raw_input("Enter a string: ").upper()
result = ''
for i in range(0, len(input)):
    if not translation.has_key(input[i]): 
        result = result + input[i] 
    else:
        result = result + str(translation[input[i]])
print result
