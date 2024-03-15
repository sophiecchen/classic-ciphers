# Caesar Cipher
# Sophie Chen

'''
This program implements the Caesar cipher, a well-known substitution cipher that shifts each letter in the plaintext down the alphabet a fixed number of times. This program works exclusively with in capital letters in the English alphabet.
'''

# Setup
import sys

# Main
def main():
	'''
	The main functionality.
	'''

	if (len(sys.argv) < 3 or len(sys.argv) > 4):
		print("Usage: python3 caesar-cipher.py [-e\|-d] [message]")
		exit(1)
	
	if (sys.argv[1] != "-e" and sys.argv[1] != "-d"):
		print("Usage: python3 caesar-cipher.py [-e\|-d] [message]")
		exit(1)
	
	if (sys.argv[1] == "-e"):
		print(encrypter(sys.argv[2], sys.argv[3]))
	else:
		print(decrypter(sys.argv[2], sys.argv[3]))

main()