bill = float(raw_input("Bill amount? "))
service = raw_input("Level of service? (good/fair/bad) ")
conversion = {'good': 0.2, 'fair': 0.15, 'bad': 0.1}
tip = bill*conversion[service]
total = bill + tip
print "Tip: $%.2f" % (tip)
print "Total: $%.2f" % (total)


