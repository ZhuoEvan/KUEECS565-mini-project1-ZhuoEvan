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
    decipherMessages = []
    firstWords = limitList(firstWordLengthList, firstWordLength)
    splitMsg = splitMessage(message, keyLength)

    findKey(splitMsg, keyLength, firstWords)


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

#Find Key Function
def findKey(message, keyLength, firstWords):
    #Local Variables
    decipherList = []
    keyList = []
    nextKey = 0

    #Generate Key Function
    for _ in range(0, keyLength):
        keyList.append(0)

    #Generate Next Key Function
    while keyList[keyLength - 1] != 25:
        for num in range(0, keyLength):
            keyList[num] = nextKey
            holdKeySegments = []

            #Convert Key Number To Key Letter
            for keySegment in keyList:
                holdKeySegments.append(numToLetter(keySegment))
            r = holdKeySegments[::-1]
            
            decipher = removeKey(message, ''.join(holdKeySegments))
            decipherR = removeKey(message, ''.join(r))
            print(decipher, decipherR)

            for word in firstWords:
                if word in decipher:
                    decipherList.append(decipher)
                elif word in decipherR:
                    decipherList.append(decipherR)

        nextKey += 1
    
    print(decipherList)
    return decipherList



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


#File Opener Function
def fileOpener(file):
    #Local Variables
    fileContent = []

    with open(file) as accessFile:
        for line in accessFile:
            fileContent.append(line.strip())
    return fileContent

#Main Function
def main():
    print(applyKey('JAYHAWK', 'EECS'))
    firstWordLengthList = fileOpener("MP1_dict.txt")
    messageBreak("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX", 2, 6, firstWordLengthList)
    messageBreak("PSPDYLOAFSGFREQKKPOERNIYVSDZSUOVGXSRRIPWERDIPCFSDIQZIASEJVCGXAYBGYXFPSREKFMEXEBIYDGFKREOWGXEQSXSKXGYRRRVMEKFFIPIWJSKFDJMBGCC", 3, 7, firstWordLengthList)
    messageBreak("MTZHZEOQKASVBDOWMWMKMNYIIHVWPEXJA", 4, 10, firstWordLengthList)
    messageBreak("SQLIMXEEKSXMDOSBITOTYVECRDXSCRURZYPOHRG", 5, 11, firstWordLengthList)
    messageBreak("LDWMEKPOPSWNOAVBIDHIPCEWAETYRVOAUPSINOVDIEDHCDSELHCCPVHRPOHZUSERSFS", 6, 9, firstWordLengthList)
    messageBreak("VVVLZWWPBWHZDKBTXLDCGOTGTGRWAQWZSDHEMXLBELUMO", 7, 13, firstWordLengthList)

main()