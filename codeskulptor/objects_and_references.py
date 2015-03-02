mylist = ["a", "b", "c"]
yourlist = mylist
print mylist, yourlist
mylist[1] = 42
print mylist, yourlist
mylist = [5, 4, 3, 2, 1]
print mylist, yourlist

def func(alist):
    alist[2] = 100
    return alist

mylist = ["a", "b", "c"]
yourlist = func(mylist)
print mylist, yourlist
