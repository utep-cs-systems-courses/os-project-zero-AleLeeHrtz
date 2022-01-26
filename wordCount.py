
import  sys

#since im using a dictionary, this method deals with upercases and lowercases being different
def lowCaseconv(word):

    newWord = word.lower()

    if word[0] == '"' or word[len(word) - 1] == '"' or word[0] == ',' or word[len(word) - 1] == ',' or word[0] == ';' or word[len(word) - 1] == ';' or word[0] == '.' or word[len(word) - 1] == '.' or word[0] == ':' or word[len(word) - 1] == ':' :
        tempWrd = newWord
        newWord = ""

        for leter in tempWrd:
            if leter == '"' or leter == ',' or leter == ';' or leter == ':' or leter == '.':
                continue

            newWord = newWord + leter

    return newWord


wordsdict = {}
text = sys.argv[1]
outp = sys.argv[2]

with open(text ,'r') as file:

    for line in file:

        for word in line.split():

            word = lowCaseconv(word)

            temp  = wordsdict.get(word)

            if temp != None:
                temp += 1
                wordsdict[word] = temp
            else:
                wordsdict[word] = 1

newdict = sorted(wordsdict)

f = open(outp, "w")

for key in newdict:
    tempstr = key + " " + str(wordsdict.get(key))

    f.write(tempstr + "\n")

f.close()