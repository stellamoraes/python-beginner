#! /usr/bin/python3
s= input('Digite uma palavra:')
def both_ends(s):
    if len(s) > 2:
        return s[0:2] + s[-2:]
    else:
        return ' '
print (both_ends(s))