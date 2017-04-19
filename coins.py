coins = 0
while True:
    print "You have %d coins" % (coins)
    reponse = raw_input("Would you like a coin? ")
    if  reponse == 'yes':
        coins += 1 
    else:
        print "Bye bye!"
        break
