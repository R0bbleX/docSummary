import operator

def wordCountFile(file, sentence):
    wordCounter = 0
    for word in sentence.split():
        wordCounter += 1
    print("Document contents: " + "'" + sentence + "'")
    print("Number of words in document: " + str(wordCounter))   

def vowelCountFile(file, sentence):
    aCount = 0
    eCount = 0
    iCount = 0
    oCount = 0
    uCount = 0
    vowelCount = 0
    for word in sentence:
        for letter in word:
            if letter == "a":
                aCount += 1
                vowelCount += 1
            elif letter == "e":
                eCount += 1
                vowelCount += 1
            elif letter == "i":
                iCount += 1
                vowelCount += 1
            elif letter == "o":
                oCount += 1
                vowelCount += 1
            elif letter == "u":
                uCount += 1
                vowelCount += 1
    vowelList = [(aCount), (eCount), (iCount), (oCount), (uCount)]
    maxVowel = max(vowelList)

    if maxVowel == aCount:
        favouriteVowel = 'A'
    elif maxVowel == eCount:
        favouriteVowel = 'E'
    elif maxVowel == iCount:
        favouriteVowel = 'I'
    elif maxVowel == oCount:
        favouriteVowel = 'O'
    elif maxVowel == uCount:
        favouriteVowel = 'U'

    print("Total vowels used: " + str(vowelCount))
    print("favourite vowel: " + str(favouriteVowel))
    
file = open(r'''C:\Users\robca\Desktop\Rob2.0\Programming\Python\pythonProjects\Beginner\stringWordCount\testFile.txt''', 'r')
sentence = file.read()
wordCountFile(file, sentence)
vowelCountFile(file, sentence)
