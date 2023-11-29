#!/usr/bin/python3
for letter in range(97, 123):
    if chr(letter) in 'eq':
        continue
    print("{}".format(chr(letter)), end='')
