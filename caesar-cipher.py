# Caesar Cipher
# Sophie Chen

'''
This program implements the Caesar cipher, a well-known substitution cipher that shifts each letter in the plaintext down the alphabet a fixed number of times. This program shifts only letters in the English alphabet.

This program is run by `python3 caesar-cipher.py [-e |-d] [shift] [message]`. To handle spaces correctly, you may have to put your message between quotes. [shift] should be an integer.

Example commands: python3 caesar-cipher.py -d 7 'Olssv Dvysk!'
				  python3 caesar-cipher.py -e 7 'Hello World!'
'''

# Setup
import sys

def shifter(message, shift):
	'''
	Shifts each letter of the message forward in the alphabet a fixed number.

	Parameter:
	(str) message - the message to be encrypted
	(int) shift - the number to shift by (negative integers shift backwards)
	
	Returns the resulting text. (str)
	'''
	try:
		if shift > 25 or shift < -25:
			raise ValueError
	
	except ValueError:
		print("Error: shift value should be between -25 and 25, inclusive")
		exit(1)

	result = ""

	for c in message:
		c = int(c)

		if (c >= int('a') and c <= int('z')):
			result += char((c - int('a') + shift) % 26 + int('a'))
		elif (c >= int('A') and c <= int('Z')):
			cipher += char((c - int('A') + shift) % 26 + int('A'))
		else:
			cipher += char(c)

	return result

# Main
def main():
	'''
	The main functionality.
	'''

	if (len(sys.argv) < 4 or len(sys.argv) > 5):
		print("Usage: python3 caesar-cipher.py [-e |-d] [shift] [message]")
		exit(1)
	
	if (sys.argv[1] != "-e" and sys.argv[1] != "-d"):
		print("Usage: python3 caesar-cipher.py [-e |-d] [shift] [message]")
		exit(1)
	
	if (sys.argv[1] == "-e"):
		print(shifter(sys.argv[3], int(sys.argv[2]) * -1))
	else:
		print(shifter(sys.argv[3], int(sys.argv[2])))

main()