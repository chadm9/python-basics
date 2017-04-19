input = raw_input("Enter a string: ")
result = ''
current = ''
previous = ''
for i in range(0, len(input)):
    current = input[i]
    if input[i] == previous: 
        result = result + 4*input[i] 
    else:
        result = result + current 
    previous = current
print result
