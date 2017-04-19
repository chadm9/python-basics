bill = float(raw_input("Bill amount? "))
service = raw_input("Level of service? (good/fair/bad) ")
conversion = {'good': 0.2, 'fair': 0.15, 'bad': 0.1}
people = float(raw_input('How many ways to split the check? '))
tip = bill*conversion[service]
total = bill + tip
divided_total = total/people
print "Tip: $%.2f" % (tip)
print "Total: $%.2f" % (total)
print "That will be $%.2f per person" % (divided_total)

