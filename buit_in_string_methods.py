sentence = "this is a string example. Just for FUN!"
s_alnum = "12345qwerasd"
s_alpha = "helloman"
s_digit = "123456787654"
s_upper = '123SAD5T6?>,'
s_u = u'123gu'   # unicode object
s_u_num = u'43679098' # unicode object
space1 = '           '
space2 = ' '
nothing = ''
book = "Gone With The Wind"
string_list = ['hello', 'hey', 'Oh', 'my', 'god']
string_tuple = tuple(string_list) # string_tuple = ('hello', 'hey', 'Oh', 'my', 'god')
hello = 'hello'

# capitalize
print sentence.capitalize()  # sentence = "this is a string example. Just for FUN!"

# center
print sentence.center(40, '-') # sentence = "this is a string example. Just for FUN!"

# count
print sentence.count('i') # sentence = "this is a string example. Just for FUN!"
print sentence.count('is')
print sentence.count('is', 3, len(sentence))

# encode and decode
encoded = sentence.encode('base64', 'strict') 
print encoded

decoded = encoded.decode('base64', 'strict')
print decoded

# endwith
print sentence.endswith("for")  # return false
print sentence.endswith("for", 0, 34) 

# expandtabs
sentence2 = "This is \ta string example.\t Just for fun \t!"
print sentence2    
print sentence2.expandtabs()  # default 8
print sentence2.expandtabs(2)
print sentence2.expandtabs(4)
print sentence2.expandtabs(8)
print sentence2.expandtabs(16)

# find and index
print sentence.find('for')    # sentence = "this is a string example. Just for FUN!"
print sentence.index('for')
print sentence.find('for', 0, 10)
print sentence.index('for', 0, 10)
print sentence.find('for', 15)
print sentence.index('for', 15)

# isalnum
# This method returns true if all characters in the string are alphanumeric
# and there is at least one character, false otherwise.
print s_alpha.isalnum()
print sentence.isalnum()
print s_alnum.isalnum()  # s_alnum = "12345qwerasd"
print s_digit.isalnum()

# isalpha
print s_alpha.isalpha()
print s_alnum.isalpha()  # s_alnum = "12345qwerasd"

# isdigit
print s_digit.isdigit()
print sentence.isdigit()

# islower
# checks whether all the case-based characters (letters) of the string are lowercase
print sentence.islower()
print s_alnum.islower()   # s_alnum = "12345qwerasd"

#isupper
print sentence.isupper()
print s_upper.isupper()

# isnumeric
# checks whether the string consists of only numeric characters.
# This method is present only on unicode objects
print s_u.isnumeric()      # s_u = u'123gu' is unicode object
print s_u_num.isnumeric()  # s_u_num = u'43679098' is unicode object

# isdecimal
# checks whether the string consists of only decimal characters.
# This method are present only on unicode objects
print s_u.isdecimal()      # s_u = u'123gu' is unicode object
print s_u_num.isdecimal()  # s_u_num = u'43679098' is unicode object

# isspace
# checks whether the string consists of whitespace
print sentence.isspace() # sentence = "this is a string example. Just for FUN!"
print space1.isspace()   # space1 = '           '
print space2.isspace()   # space2 = ' '
print nothing.isspace()  # nothing = ''

# istitile and title
# istitle checks whether all the case-based characters in the string
# following non-casebased letters are uppercase 
# and all other case-based characters are lowercase
print book.istitle()     # book = "Gone With The Wind"
print sentence.istitle() # sentence = "this is a string example. Just for FUN!"
print sentence.title()

# join
separator = ' - '
print separator.join(string_list)   # string_list = ['hello', 'hey', 'Oh', 'my', 'god']
print separator.join(string_tuple)  # string_tuple = ('hello', 'hey', 'Oh', 'my', 'god')
print separator.join(hello)         # hello = 'hello'

# ljust and rjust
# ljust returns the string left justified in a string of lengthwidth.
# Padding is done using the specified fillchar (default is a space). 
# The original string is returned if width is less than len(s)
print hello.ljust(10)
print hello.ljust(10, '-')
print hello.rjust(10, '-')
# lower, upper and swapcase
print sentence.lower()
print sentence.upper()
print sentence.swapcase()

# lstrip, rstrip and strip
ss = '          This is what?      '
tt = '**********This is what?------'
print ss.lstrip()
print tt.lstrip('*')
print ss.rstrip()
print tt.rstrip('-')
print ss.strip()

# max and min
print max(sentence)  # sentence = "this is a string example. Just for FUN!"
print min(sentence)
print min(hello)     # hello = 'hello'

# replace
print sentence.replace('is', 'was')  # sentence = "this is a string example. Just for FUN!"
print sentence.replace('is', 'was', 1)

# rfind and rindex
# rfind() returns the last index where the substring str is found,
# or -1 if no such index exists, optionally restricting the search to string[beg:end]
rindex() returns the last index where the substring str is found,
# or raises an exception if no such index exists,
# optionally restricting the search to string[beg:end]
sentence3 = 'Here is my favorite fruit, here is my best friend.'
print sentence3.rfind('is')
print sentence3.rfind(hello)   # hello = 'hello'
print sentence3.rindex('is')
print sentence3.rindex(hello)

# split
print sentence.split()    # sentence = "this is a string example. Just for FUN!"

# splitlines
paragraph = '''Hello!
This is Ada.
Nice to meet you all.'''

paragraph.splitlines()

# startswith
print sentence.startswith('this')

# zfill
# The method zfill() pads string on the left with zeros to fill width
print hello.zfill(10)








































































