fullname = 'Chad McKee'
age = 99

myarray = []
myarray.append(fullname)
myarray.append(age)

print myarray

def say_hello():
    print 'Hello'

say_hello()

split_name = fullname.split() 
print split_name

def say_name():
    print 'hello', split_name[0]

say_name()

def my_age(year_born):
    print 2017 - year_born

my_age(1991)


def sum_odd_numbers():
    sum = 0
    for i in range(1, 5001, 2):
        sum += i
    return sum
print sum_odd_numbers()

