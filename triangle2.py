height = int(raw_input('Enter the height of your triangle: '))
stars = 1
spaces = height - 1 
for i in range(height):
    print spaces*" " + stars*"*" + spaces*" "    
    stars += 2
    spaces -= 1
