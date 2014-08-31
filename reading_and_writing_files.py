# write
my_file = open('foo.txt', 'wb')
my_file.write('Python is a great language.\nYeah, it is great!!')
my_file.close()

# read
my_file = open('foo.txt', 'r+')
content = my_file.read(10)
print content
content = my_file.read(10)
print content

# tell
position = my_file.tell()
print position

# seek 
position = my_file.seek(0, 0)
content = my_file.read(10)
print content
