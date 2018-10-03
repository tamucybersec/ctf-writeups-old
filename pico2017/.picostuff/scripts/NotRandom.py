#!/usr/bin/python -u

# pico2017
# Level 2
# 'SoRandom'
# 20180923
import random,string

s = 'BNZQ:4pg33e44sdu4wu8198y15q685vpx8041'
decflag=''
random.seed('random')

for c in s:
	if c.islower():
		decflag += chr((ord(c)-ord('a')-random.randrange(0,26))%26 + ord('a'))
	elif c.isupper():
		decflag += chr((ord(c)-ord('A')-random.randrange(0,26))%26 + ord('A'))
	elif c.isdigit():
		decflag += chr((ord(c)-ord('0')-random.randrange(0,10))%10 + ord('0'))
	else:
		decflag += c
		
print "Unguessably Randomized Flag: " + decflag
