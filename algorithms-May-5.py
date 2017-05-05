

def algorithm1():
    sum = 0
    for i in range(1, 1001):

        if i % 3 == 0 or i % 5 ==0:
            sum += i

    print sum





def algorithm2():
    sum = long(0)
   # for n in range(1, 9):

    n = 200
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
        print a
        if a % 2 == 0:

            sum += a
        if a > 4000000:
            break

    return sum


def algorithm3():
    lyst = []
    i = 1
    while i < 600851475143:
        if 600851475143%i == 0:
            lyst.append(i)
            print i
        if i > 600851475143/2:
            break
        i += 2

    print lyst





def algorithm4():

    i = 1
    while i < 600851475143:
        if 600851475143%i == 0:
            a = 600851475143/i

            value = 3

            while value < a:
                if a % value == 0:
                    break
                if value > a/2:

                    return a
                value += 2



        i += 2



#algorithm3()
print algorithm4()