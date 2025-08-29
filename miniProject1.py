#miniProject1

#Global Variables
alphabetDict = {
    'A': 0, 'B': 1, 'C': 2, 'D': 3,
    'E': 4, 'F': 5, 'G': 6, 'H': 7,
    'I': 8, 'J': 9, 'K': 10, 'L': 11,
    'M': 12, 'N': 13, 'O': 14, 'P': 15,
    'Q': 16, 'R': 17, 'S': 18, 'T': 19,
    'U': 20, 'V': 21, 'W': 22, 'X': 23,
    'Y': 24, 'Z': 25
}

#Encryption Function
def encryption(m, K):
    m = letterToNum(m)
    K = letterToNum(K)
    result = m + K % 26
    result = numToLetter(result)
    return result

#Decryption Function
def decryption(m, K):
    result = m - K % 26
    return result

#Letter Convertor Function
def letterToNum(letter):
    num = alphabetDict.get(letter)
    print(f'letterToNum {num}')
    return num
    

#Number Convertor Function
def numToLetter(num):
    letter = retrieveKey(num)
    print(letter)
    return letter

#Dictionary Key Retrieve Function
def retrieveKey(searchValue):
    for key, value in alphabetDict.items():
        if searchValue == value:
            return key
    
    raise RuntimeError("Error 01: Key Does Not Exist Error.") #Error Check

#Main Function
def main():
    m = encryption('A', 'C')
    print(m)

main()