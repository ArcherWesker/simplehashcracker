#!/usr/bin/python
import crypt
import sys

try:

	print ("\033[5;49;31m**************************************************\033[m")
	print ("\033[5;49;31m|\033[m              \033[0;49;31m SIMPLE HASH CRACKER\033[m              \033[5;49;31m|\033[m")
	print ("\033[5;49;31m|\033[m                   \033[0;49;31m by Arch3r\033[m                   \033[5;49;31m|\033[m")
	print ("\033[5;49;31m**************************************************\033[m")

	try:
		hash = input("\033[1;49;37mInsert\033[m \033[1;49;31mHASH:\033[m ")
		salt = input("\033[1;49;37mInsert\033[m \033[1;49;96mSALT:\033[m ")
		file = open(sys.argv[1])

		for i in file:
			i = i.strip()
			passw = crypt.crypt(i,salt)
			if hash == passw:
				print ("\033[1;49;92mHash has been successfully cracked -->\033[m ",i)
				exit(0)
			else:
				print ("\033[1;49;91mCracking the hash...\033[m",i)
	except IndexError:
		print ("\033[0;49;31mERROR: A WORDLIST IS NEEDED.\033[m")
		print ("\033[0;49;31mExample: python3 hashbrute.py <wordlist>\033[m")

except KeyboardInterrupt:
	print ("\n\033[0;49;36mSCRIPT WAS INTERRUPTED BY THE USER.\nSee you soon.\033[m")
