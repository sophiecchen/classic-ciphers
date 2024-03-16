# Hill Cipher
# Sophie Chen

'''
This program implements the Hill cipher, a linear algebra-based polygraphic substitution cipher, for messages with length multiple of 3 with a hard-coded key.

The following scheme is used (must use capital letters)
0 = 'A'
1 = 'B'
...
25 = 'Z'
26 = ' '
27 = '?'
28 = '!'

This program is run by `python3 hill-cipher.py [-e|-d] [message]`. To handle spaces correctly, you may have to put your message between quotes. The message must have a length multiple of 3.

This program was adapted from code originally aimed at decoding a specific text with a given key. As a result, the key currently is hardcoded. This may be changed manually in the code at your discretion.

Example command: python3 hill-cipher.py -d 'IGSFVHIRMG UWW?ZNIQVBEF?RYD!X P?DRSVVQHORJ?HP'

This command should return "THE CELESTIAL RIVER FALLS FROM HEAVEN ON HIGH".
'''

# Setup
import sys

# Matrix Objects
class Matrix():
	'''
	The Matrix class creates a matrix (2d array).
	'''

	def __init__(self, row, column):
		'''
		Initializes a Matrix object with all zeros.

		Parameter:
		(int) row - the number of rows in the matrix
		(int) column - the number of columns in the matrix
		'''
		self._row = row
		self._column = column
		self._matrix = []

		# Initialize to the zero matrix.
		for i in range(self._row):
			rower = []
			for j in range(self._column):
				rower.append(0)
			self._matrix.append(rower)

	def getRow(self):
		'''
		Returns the number of rows in the matrix. (int)
		'''
		return self._row
	
	def getColumn(self):
		'''
		Returns the number of columns in the matrix. (int)
		'''
		return self._column

	def getEntry(self, row, column):
		'''
		Returns an entry in the matrix.

		Parameter:
		(int) row - the row of the entry
		(int) column - the column of the entry
		'''
		return self._matrix[row][column]

	def printMatrix(self):
		'''
		Prints the matrix in a readable format
		'''
		for i in range(self._row):
			print(self._matrix[i])
		print("\n")
	
	def setEntry(self, row, column, value):
		'''
		Sets an entry in the matrix to a value.

		Parameter:
		(int) row - the row of the entry
		(int) column - the column of the entry
		value - the value the entry is set to
		'''
		try:
			self._matrix[row][column] = value 
		except IndexError:
			print("Error: row/column outside of matrix bounds")
			exit(1)

	def setMatrixDown(self, data):
		'''
		Sets the matrix from top to bottom, left to right following given data.

		Parameter:
		(str) data - the data the matrix is set to, each entry getting one character
		'''
		counter = 0

		for j in range(self._column):
			for i in range(self._row):
				self.setEntry(i, j, data[counter:counter+1])
				counter += 1
	
	def multiplyRight(self, matrix):
		'''
		Right multiplies a given matrix to itself.

		ie. returns AB in which self = A and matrix = B

		Parameter:
		(Matrix) matrix - the matrix to right multiply

		Returns the result of the multiplication.
		'''
		try:
			if self._column != matrix.getRow():
				raise ArithmeticError
		except ArithmeticError:
			print("Error: cannot multiply matrices, wrong dimensions")
			exit(1)
		else:
			newMatrix = StringMatrix(self._row, matrix.getColumn())

			for i in range(self._row):
				for j in range(matrix.getColumn()):
					value = 0
					counter = 0

					while (counter < self._column):
						value += self.getEntry(i, counter) * matrix.getEntry(counter, j)
						counter += 1

					newMatrix.setEntry(i, j, value)
			
			return newMatrix
	
	def mod29(self):
		'''
		Takes each entry in the matrix and mod29s it.
		'''
		for i in range(self._row):
			for j in range(self._column):
				self.setEntry(i, j, self.getEntry(i, j)%29)

class KeyMatrix(Matrix):
	'''
	The KeyMatrix class is a child of the Matrix class specific to cryptograhic keys.
	'''

	def __init__(self, row, column):
		'''
		Initializes a KeyMatrix object with all zeros.

		Parameter:
		(int) row - the number of rows in the matrix
		(int) column - the number of columns in the matrix
		'''
		super().__init__(row, column)

	def setMatrixDown(self, array):
		'''
		Sets the matrix from top to bottom, left to right following given data.

		Parameter:
		(array) array - the data the matrix is set to, each entry getting one item in the array
		'''
		counter = 0

		for j in range(self._column):
			for i in range(self._row):
				self.setEntry(i, j, array[counter])
				counter += 1

	def multiplyRows(self, multArr):
		'''
		Multiplies each row by the corresponding value in the array.

		ie. the first row is multiplied by the first entry in the array, and so on...

		Parameter:
		(int array) multArr - the value that each row will be multiplied by
		'''
		try:
			if len(multArr) != self._row:
				raise ValueError
		except ValueError:
			print("Error: array attribute length should be equal to number of rows")
			exit(1)
		else:
			for i in range(self._row):
				for j in range(self._column):
					self.setEntry(i, j, multArr[i]*self.getEntry(i, j))

class StringMatrix(Matrix):
	'''
	The StringMatrix class is a child of the Matrix class specific to cryptographic texts.
	'''

	def __init__(self, row, column):
		'''
		Initializes a StringMatrix object with all zeros.

		Parameter:
		(int) row - the number of rows in the matrix
		(int) column - the number of columns in the matrix
		'''
		super().__init__(row, column)

	def getStringDown(self):
		'''
		Returns the values of the matrix from top to bottom, left to right. (str)
		'''
		string = ""
		for j in range(self._column):
			for i in range(self._row):
				string += self.getEntry(i, j)

		return string

	def messNum(self):
		'''
		Replaces each character in the matrix with its corresponding number.
		'''
		switcher = {
			"A": 0,
			"B": 1,
			"C": 2,
			"D": 3,
			"E": 4,
			"F": 5,
			"G": 6,
			"H": 7,
			"I": 8,
			"J": 9,
			"K": 10,
			"L": 11,
			"M": 12,
			"N": 13,
			"O": 14,
			"P": 15,
			"Q": 16,
			"R": 17,
			"S": 18,
			"T": 19,
			"U": 20,
			"V": 21,
			"W": 22,
			"X": 23,
			"Y": 24,
			"Z": 25,
			" ": 26,
			"?": 27,
			"!": 28
		}

		for i in range(self._row):
			for j in range(self._column):
				self.setEntry(i, j, switcher[self.getEntry(i, j)])

	def numMess(self):
		'''
		Replaces each number in the matrix with its corresponding character.
		'''
		switcher = {
			0: "A",
			1: "B",
			2: "C",
			3: "D",
			4: "E",
			5: "F",
			6: "G",
			7: "H",
			8: "I",
			9: "J",
			10: "K",
			11: "L",
			12: "M",
			13: "N",
			14: "O",
			15: "P",
			16: "Q",
			17: "R",
			18: "S",
			19: "T",
			20: "U",
			21: "V",
			22: "W",
			23: "X",
			24: "Y",
			25: "Z",
			26: " ",
			27: "?",
			28: "!"
		}

		for i in range(self._row):
			for j in range(self._column):
				self.setEntry(i, j, switcher[self.getEntry(i, j)])

# Helper Functions
def invMod(number, moder):
	#a * x ≡ 1 (mod m)

    number = number % moder

    for i in range(1, moder): 
        if ((number * i) % moder == 1): 
            return i

    return 1

def invModArray(arrayer, moder):
	result = []

	for i in arrayer:
		result.append(invMod(i, moder))

	return result

# Crypto Functions
def encrypter(message, key):
	'''
	Encrypts a message, matrix mod 29, with work shown.

	Parameter:
	(str) message - the message to be encrypted (length divisible by 3)
	(int array) key - the 3x3 matrix key, written top to bottom, left to right
	
	Returns the cipher text. (str)
	'''
	try:
		if len(message)%3 != 0:
			raise ValueError
		if len(key) != 9:
			raise ValueError
	
	except ValueError:
		print("Error: message length should be multiple of 3 OR key length should be 9")
		exit(1)
	
	else:
		messMatrix = StringMatrix(3, len(message)//3)
		messMatrix.setMatrixDown(message)
		print("Message Matrix in Characters:")
		messMatrix.printMatrix()
		
		messMatrix.messNum()
		print("Message Matrix in Numbers:")
		messMatrix.printMatrix()

		keyMatrix = KeyMatrix(3, 3)
		keyMatrix.setMatrixDown(key)
		print("Key Matrix:")
		keyMatrix.printMatrix()

		cipherMatrix = keyMatrix.multiplyRight(messMatrix)
		print("Result of Multiplication:")
		cipherMatrix.printMatrix()
		
		cipherMatrix.mod29()
		print("Cipher Matrix Mod 29:")
		cipherMatrix.printMatrix()
		
		cipherMatrix.numMess()
		print("Cipher Matrix in Characters:")
		cipherMatrix.printMatrix()

		return cipherMatrix.getStringDown()

def decrypter(cipher, invKeySimp, invKeyLeft):
	'''
	Decrypts a cipher text, matrix mod 29, with work shown.

	Parameter:
	(str) cipher - the cipher to be decrypted
	(int array) invKeySimp - the "almost" inverse of the 3x3 matrix key, written top to bottom, left to right
	(int array) invKeyLeft - the 3 values left of the augmented array from top to bottom

	ie. if	[1  1 2 | 1 0 0] simplifies to 	[18 0  0 |  75 -6 -15]
			[2 10 5 | 0 1 0]				[0  18 0 |  -1  2  -1]
			[3  1 8 | 0 0 1]				[0  0  9 | -14  1   4]
		
		invKeySimp = [75, -1, -14, -6, 2, 1, -15, -1, 4]
		invKeyLeft = [18, 18, 9]
	
	Returns the message. (str)
	'''
	try:
		if len(cipher)%3 != 0:
			raise ValueError
		if len(invKeySimp) != 9:
			raise ValueError
	
	except ValueError:
		print("Error: cipher length should be multiple of 3 OR simplified key length should be 9")
		exit(1)
	
	else:
		cipherMatrix = StringMatrix(3, len(cipher)//3)
		cipherMatrix.setMatrixDown(cipher)
		print("Cipher Matrix in Characters:")
		cipherMatrix.printMatrix()
		
		cipherMatrix.messNum()
		print("Cipher Matrix in Numbers:")
		cipherMatrix.printMatrix()

		keyMatrix = KeyMatrix(3, 3)
		keyMatrix.setMatrixDown(invKeySimp)
		print("Almost Inverse Key Matrix:")
		keyMatrix.printMatrix()

		invKeyMult = invModArray(invKeyLeft, 29)
		print("Multiply each row by: " + str(invKeyMult) + "\n")
		keyMatrix.multiplyRows(invKeyMult)
		print("Almost Inverse Key Matrix with Inverse Mod29 Multiplication:")
		keyMatrix.printMatrix()
		
		keyMatrix.mod29()
		print("Key Matrix Mod 29:")
		keyMatrix.printMatrix()

		messMatrix = keyMatrix.multiplyRight(cipherMatrix)
		print("Result of Multiplication:")
		messMatrix.printMatrix()
		
		messMatrix.mod29()
		print("Message Matrix Mod 29:")
		messMatrix.printMatrix()
		
		messMatrix.numMess()
		print("Message Matrix in Characters:")
		messMatrix.printMatrix()

		return messMatrix.getStringDown()

# Main
def main():
	'''
	The main functionality.
	'''

	if (len(sys.argv) < 3 or len(sys.argv) > 4):
		print("Usage: python3 hill-cipher.py [-e|-d] [message]")
		exit(1)
	
	if (sys.argv[1] != "-e" and sys.argv[1] != "-d"):
		print("Usage: python3 hill-cipher.py [-e|-d] [message]")
		exit(1)
	
	if (sys.argv[1] == "-e"):
		print(encrypter(sys.argv[2], [1, 3, 2, 2, 7, 5, 1, 4, 8]))
	else:
		print(decrypter(sys.argv[2], [36, -16, 1, -11, 6, -1, 1, -1, 1], [5, 5, 5]))

main()