#miniProject1

#Python Libraries
import itertools
import string
import time
import datetime

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

bar = '=============================='

#Encryption Function
def encryption(m, K):
    m = letterToNum(m)
    K = letterToNum(K)
    result = (m + K) % 26
    result = numToLetter(result)
    return result

#Decryption Function
def decryption(m, K):
    m = letterToNum(m)
    K = letterToNum(K)
    result = (m - K) % 26
    result = numToLetter(result)
    return result

#Letter Convertor Function
def letterToNum(letter):
    num = alphabetDict.get(letter)
    return num
    
#Number Convertor Function
def numToLetter(num):
    letter = retrieveKey(num)
    return letter

#Dictionary Key Retrieve Function
def retrieveKey(searchValue):
    for key, value in alphabetDict.items():
        if searchValue == value:
            return key
    #Error Check: Key Does Not Exist
    raise RuntimeError("Error 01: Key Does Not Exist Error.")

#Message Split Function
def splitMessage(message, keyLength):
    #Local Variables
    splitMessage = []
    combinedChar = ''
    currentIndex = 1

    #Split the Message into keyLength Size
    for char in message:
        combinedChar = combinedChar + char
        if currentIndex % keyLength == 0:
            splitMessage.append(combinedChar)
            combinedChar = '' #Reset combinedChar
        currentIndex += 1 #Increment the currentIndex
    
    #Append Remaining Characters
    if len(combinedChar) != 0:
        splitMessage.append(combinedChar)
    
    return splitMessage #Return List

#Limit List Function
def limitList(firstWordLengthList, firstWordLength):
    #Local Variables
    firstWords = []

    for word in firstWordLengthList:
        if len(word) == firstWordLength:
            firstWords.append(word)

    return firstWords #Return List

#Password Crack Function
def messageBreak(message, keyLength, firstWordLength, firstWordLengthList):
    #Local Variables
    decipherKeys = []
    decipherMessages = []
    firstWords = limitList(firstWordLengthList, firstWordLength)
    splitMsg = splitMessage(message, keyLength)

    #Start Timer
    tm = startTimer(message, keyLength, firstWordLength)

    #Generate Key Function
    allKeys = generateKeys(keyLength)

    #Use all keys on the message
    for key in allKeys:
        decryptedMessage = removeKey(splitMsg, key)

        for word in firstWords:
            if word in decryptedMessage and decryptedMessage not in decipherMessages:
                decipherKeys.append(key)
                decipherMessages.append(decryptedMessage)

    elapsed_time = endTimer(tm)
    fileWrite(message, decipherMessages, decipherKeys, elapsed_time)
    return

#Apply Key Function
def applyKey(message, key):
    #Local Variables
    keyLength = len(key)
    encryptChar = []

    stringList = splitMessage(message, keyLength)
    for string in stringList:
        keyIndex = 0
        for char in string:
            encryptChar.append(encryption(char, key[keyIndex]))
            keyIndex += 1

    encryptedMessage = ''.join(encryptChar)
    return encryptedMessage

#Generate Keys Function (Used stackOverflow)
def generateKeys(length):
    letters = string.ascii_uppercase
    return [''.join(key) for key in itertools.product(letters, repeat=length)]

#Remove Key Function
def removeKey(message, key):
    #Local Variables
    decryptChar = []
    
    for string in message:
        keyIndex = 0
        for char in string:
            decryptChar.append(decryption(char, key[keyIndex]))
            keyIndex += 1
    
    decryptedMessage = ''.join(decryptChar)
    return decryptedMessage

#File Writer Function
def fileWrite(msg, dMsg, dKeys, elapsed_time):
    with open('output.txt', 'a') as outputFile:
        outputFile.write(f'{bar}{bar}{bar}\nEncrypted Message: {msg}\n\n')

        for index in range(0, len(dMsg)):
            outputFile.write(f'{dMsg[index]} | {dKeys[index]}\n')

        outputFile.write(f'\nElapsed Time: {elapsed_time:.3f} seconds\n{bar}{bar}{bar}\n\n')
        outputFile.close()
    return

#File Opener Function
def fileOpener(file):
    #Local Variables
    fileContent = []

    #Generate Output File
    with open('output.txt', 'w') as outputFile:
        td = datetime.datetime.now()
        outputFile.write(f'Output File | Started on {td.strftime('%c')}\n')
        outputFile.close()

    #Open File Function
    with open(file) as accessFile:
        for line in accessFile:
            fileContent.append(line.strip())
    return fileContent

#Start Timer Function
def startTimer(message, keyLength, firstWordLength):
    print(f'{bar}\nStarting Timer...')
    print(f'Decrypting Message: {message}\nKey Length: {keyLength}\nFirst Word Length: {firstWordLength}')
    return time.time()

#End Timer Function
def endTimer(startTime):
    elapsed_time = time.time() - startTime
    print(f'Stopping Timer...\nElapsed Time: {elapsed_time:.3f} seconds\n{bar}\n')
    return elapsed_time

#Main Function
def main():
    #Local Variables
    firstWordLengthList = fileOpener("MP1_dict.txt")

    messageBreak("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX", 2, 6, firstWordLengthList)
    messageBreak("PSPDYLOAFSGFREQKKPOERNIYVSDZSUOVGXSRRIPWERDIPCFSDIQZIASEJVCGXAYBGYXFPSREKFMEXEBIYDGFKREOWGXEQSXSKXGYRRRVMEKFFIPIWJSKFDJMBGCC", 3, 7, firstWordLengthList)
    messageBreak("MTZHZEOQKASVBDOWMWMKMNYIIHVWPEXJA", 4, 10, firstWordLengthList)
    messageBreak("SQLIMXEEKSXMDOSBITOTYVECRDXSCRURZYPOHRG", 5, 11, firstWordLengthList)
    messageBreak("LDWMEKPOPSWNOAVBIDHIPCEWAETYRVOAUPSINOVDIEDHCDSELHCCPVHRPOHZUSERSFS", 6, 9, firstWordLengthList)
    messageBreak("VVVLZWWPBWHZDKBTXLDCGOTGTGRWAQWZSDHEMXLBELUMO", 7, 13, firstWordLengthList)

main()