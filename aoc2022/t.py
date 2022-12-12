# coding=utf-8
""" MiniStringFuck generator by Έρικ Κωνσταντόπουλος, © 2006-2013 """

# Module importing
from sys import stdout, stdin, stderr

# String getting
string = stdin.read()

# Memory freeing #1
#""" # Uncomment this line to disable!
del stdin
#""" # Never modify line 12.

# String checking (ASCII only)
for i in string:
    if ord(i) not in range(256):
         stderr.write('Your string contains non-ASCII characters.')
         exit()

# Memory freeing #2
#""" # Uncomment this line to disable!
del stderr
#""" # Never modify line 23.

# Character storing
char = 0

# Code generating
for i in string:
    while chr(char) != i:
        char += 1
        char %= 256
        stdout.write('+')
    stdout.write('.')
