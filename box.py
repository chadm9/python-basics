width = int(raw_input("Enter the width of your box: ")) 
height = int(raw_input("Enter the height of your box: "))   

for i in range(height):
    if i == 0 or i == height - 1:
        print width*'*'
    else:
        print "*" + (width - 2)*" " + "*"
