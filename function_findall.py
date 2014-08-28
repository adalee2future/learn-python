import re

s = 'Hello from csev@umich.edu to cwen@iupui.edu about the meeting@2PM'
# We are using a two-character sequence that matches a non-whitespace character(\S)
lst = re.findall('\S+@\S+', s)
print lst