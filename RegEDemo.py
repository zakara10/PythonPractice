import re
p = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print(p.findall('Call me 123-123-1212 or 121-121-1212'))
