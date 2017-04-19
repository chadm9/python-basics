alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

key = int(raw_input("Enter the negative shift value "))
input = raw_input("Enter a string: ")

result = ''
for i in range(0, len(input)):
    if input[i] == ' ':
        result = result + ' '
    else:
        result = result + alphabet[alphabet.index(input[i]) + key]
print result
