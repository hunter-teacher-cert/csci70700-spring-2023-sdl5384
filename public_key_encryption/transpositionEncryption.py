transpositionMatrix = []

def setupMatrix(rowsNeeded):
	print("Enter your message to encrypt here.")
	msgToEncrypt = input()

	#remove space in the message
	msgToEncrypt.replace(' ', '')

	charactersInColumn = int(len(msgToEncrypt)/rowsNeeded)

	#create rows of six characters
	for i in range(0,len(msgToEncrypt)-1):
		for j in range(0,charactersInColumn-1):
			if i%5 == 1:
				transpositionMatrix.append([])
				transpositionMatrix[j].append(msgToEncrypt[i])
			else:
				print(j)
				print(i)
				transpositionMatrix[j].append(msgToEncrypt[i])

def printMatrix(matrix):
	for k in range(0,len(matrix)):
		print(matrix[k])

def invertToEncrypt():
	return None

def main():
	setupMatrix(5)
	printMatrix()
	print(transpositionMatrix)

main()