# Caesar Cipher
# Sophie Chen

'''
This program implements the Caesar cipher, a well-known substitution cipher that shifts each letter in the plaintext down the alphabet a fixed number of times. This program shifts only letters in the English alphabet.

This program is run by `python3 caesar-cipher.py [-e |-d] [shift] d'[message]'`. To handle spaces correctly, put your message between quotes. [shift] should be an integer from 0 to 25, inclusive.

Example commands: python3 hill-cipher.py -d 7 'Olssv Dvysk!'
				  python3 hill-cipher.py -e 7 'Hello World!'
'''

# Setup
import sys

def encrypter():
	pass

def decrypter():
	pass

# Main
def main():
	'''
	The main functionality.
	'''

	if (len(sys.argv) < 3 or len(sys.argv) > 4):
		print("Usage: python3 caesar-cipher.py [-e\|-d] [message] [shift]")
		exit(1)
	
	if (sys.argv[1] != "-e" and sys.argv[1] != "-d"):
		print("Usage: python3 caesar-cipher.py [-e\|-d] [message] [shift]")
		exit(1)

	if (sys.argv[3] !=):
		print("Shift parameter must be an integer between 0 and 25")
		exit(1)
	
	if (sys.argv[1] == "-e"):
		print(encrypter(sys.argv[2], sys.argv[3]))
	else:
		print(decrypter(sys.argv[2], sys.argv[3]))

main()