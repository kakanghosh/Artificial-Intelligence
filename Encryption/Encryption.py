securityCode = {}
matrixList = []
encodedMatrix = []
pattern = [
    [1,2,3],
    [1,1,2],
    [0,1,2]
]
#This method with Initialize the securityCode like 'A':1, 'B':2... 'Z':26
def initializeCode():
    code = 1
    for i in range(65,91):
        securityCode[chr(i)] = code
        code += 1
#This method will find the character against a values
def findChar(value):
    for key in securityCode:
        if securityCode[key] is value:
            return key
#This method will find the value against a character
def findValue(keyvalue):
    for key in securityCode:
        if key is keyvalue:
            return securityCode[key]
#Matrix Multiplication
def matrixMultiplication(mat1,mat2):
    mat = []
    for i in range(len(mat1)):
        total = 0
        for j in range(len(mat2)):
            total += mat1[i][j]*mat2[j]
        mat.append(total)
    return mat

def isInvertable():
    # total = 0
    # total += pattern[0][0]* (pattern[1][1]*pattern[2][2] - pattern[2][1]*pattern[1][2])
    # total -= pattern[0][1]* (pattern[1][0]*pattern[2][2] - pattern[2][0]*pattern[1][2])
    # total += pattern[0][2]* (pattern[1][0]*pattern[2][1] - pattern[2][0]*pattern[1][1])
    # if total is not 0:
    #     return True
    # else:
    #     return False
    for i in range(len(pattern)):
        for j in range(len(pattern[i])):
            if i is 0:
                print(pattern[i][j], '', end='')
        print()

#Encryption
def encryption(word):
    print('Message:',word)
    counter = 3
    start = 0
    end = 3
    matrix = []
    for c in word:
        matrix.append(findValue(c))
    #print(matrix)
    while start < len(matrix):
        temp = matrix[start:end]
        if len(temp) is counter:
            matrixList.append(temp)
        else:
            for i in range(0,counter-len(temp)):
                temp.append(0)
            matrixList.append(temp)
        start += 3
        end += 3

    for mat in matrixList:
        encodedMatrix.append(matrixMultiplication(pattern,mat))

    print('Original Matrix:',matrixList)
    print('Encrypted Matrix:',encodedMatrix)

#decryption
def decryption():
    isInvertable()

#MAIN FUNCTION
initializeCode()
encryption('CRYPTOGRAPHY')
decryption()