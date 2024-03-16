# Vigenère Cipher
# Sophie Chen

'''
This program implements the Vigenère cipher, a cipher that encodes each plaintext letter with a different Caesar cipher. This program shifts only letters in the English alphabet.

This program is run by `python3 vigenere-cipher.py [-e |-d] [key] '[message]'`. To handle spaces correctly, put your message between quotes. [key] should composed of only letters in the English alphabet.

Example commands: python3 vigenere-cipher.py -d abc "Hfnlp Yosnd!"
				  python3 vigenere-cipher.py -e ABC "Hello World!"
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