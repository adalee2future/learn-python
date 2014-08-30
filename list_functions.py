num_list1 = [1, 3, 2, 6, 2, 3, 4, 5, 1, 2]
num_list2 = [9, 8, 7, 6, 5, 4, 3, 2, 2, 0]
str_list = ['hello', 'hey', 'hello', 'hi', 'hey']

# count
print num_list1.count(2)
print str_list.count('hey')

# cmp
print cmp(num_list1, num_list2)

# extend
num_list1.extend(num_list2)
print num_list1

# index
print str_list.index('hey')

# insert
str_list.insert(3, 'hah')

# pop and push
sp = str_list.pop()
print sp
print str_list
print str_list

# remove
str_list.remove('hello')
print str_list

# reverse
str_list.reverse()
print str_list

# sort
num_list1.sort()
print num_list1