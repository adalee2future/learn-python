my_file = open('foo.txt', 'wb')

print my_file.name
print my_file.closed
print my_file.mode
print my_file.softspace

my_file.close()

print my_file.closed