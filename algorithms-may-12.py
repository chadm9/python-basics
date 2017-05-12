






def algorithm2():
    not_found = True
    candidate = 0
    multiplier = 1
    while not_found:
        candidate = multiplier*20
        for i in range(19, 1, -1):
            #print candidate
            if candidate % i != 0:
                break
            elif i ==2:
                not_found = False
        multiplier += 1

    return candidate


##########################################

def isPalindrome(value):
    b = list(value)
    c = []

    for i in range(len(b)-1, -1, -1):
        c.append(b[i])

    if b == c:
        return True
    else:
        return False


def getPalindromes():
    lyst = []
    for i in range(10000, 1000000):

        if isPalindrome(str(i)):
            lyst.append(str(i))

    return lyst


#print getPalindromes()
def algorithm1():
    palindromes = getPalindromes()

    for i in range(len(palindromes) - 1, 0, -1):
        factors = []

        for j in range(100, 1000):
            if int(palindromes[i])%j == 0:
                factors.append(j)

        for k in range(len(factors) -1, 0, -1):
            if len(str(int(palindromes[i])/factors[k])) > 3:
                break
            elif len(str(int(palindromes[i])/factors[k])) == 3:
                return [palindromes[i], factors[k], int(palindromes[i])/factors[k]]

                #print palindromes[i]
                #print lyst[k]



print algorithm2()
#print algorithm1()







