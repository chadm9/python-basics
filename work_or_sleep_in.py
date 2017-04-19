day = int(input('Day (0-6)? '))
dayKey = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
if dayKey[day] == 'Saturday' or dayKey[day] == 'Sunday':
    print 'Sleep in'
else:
    print 'Go to work'
