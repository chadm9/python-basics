input = raw_input("Enter some text: ") 

for i in range(3):
    if i != 1:
        print (len(input) + 4)*'*'
    else:
        print "* " + input + " *"
