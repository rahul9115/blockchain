#1st part of the assignment
def add(a,b):
    return a+b
def normal(add):
    def inner(a,b):
        print(add(a,b))
    return inner
add=normal(add)
add(2,4)
#2nd part of the assignment
def normal1(a,b):
    c=a+b
    return c
receive=lambda a:print(a*2)
receive(normal1(2,3))
#3rd and 4th part of the assignment
def normal2(*args):
    print("{} {} {} {} {}".format(*args))
    return args

list1=normal2(1,2,3,4,5)
list2=tuple(map(lambda a:a*2,list1))
print(list2)    