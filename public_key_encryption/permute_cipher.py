import math

alphabet = 'abcdefghijklmnopqrstuvwxyz'

class permutationCipher:
	def constructSquare(self):
		columns = math.floor(len(message)/2)
		rows = columns
		print(rows,columns)
		permutingSquare = []
		for i in range(0, len(message)):
			permutingSquare.append([])
			for j in range(0, len(message[i])):
				permutingSquare[i].append(())

		return permutingSquare

	def placeLettersInSquare(self,message):
		

	def encodeReverse(self, square):
		encodedMessage = None
		for m in range(len(square)-1, 0, -1):
				for n in range(len(square[m])-1, 0, -1):
					encodedMessage = encodedMessage + square[m][n]
		return encodedMessage
		
def main():
	p = permutationCipher()
	s = p.constructSquare('This is a test')
	print("The permutation square for your message is: ")
	print(s)
	encryptedMsg = p.encodeReverse(s)
	print("Your encrypted message is now ")
	print(encryptedMsg)

main()