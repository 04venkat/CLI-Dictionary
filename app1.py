import json
from difflib import get_close_matches
data = json.load(open("data.json"))

print("\nCLI - DICTIONARY\nEnter a word and get it's meaning instantly on CLI!")

def searchAnotherWord():
    w1 = input("\nSearch another word?\nGimme a yes or no! ")
    if w1.lower() == "yes":
        word = input("\nWord: ").lower()
        output = getWord(word)
        c = int(1)
        if isinstance(output, list):
            print("\nDefinition(s) Available:")
            for i in output:
                print(f"{c}) {i}")
                c = c+1
        else:
            print(output)
        searchAnotherWord()
    elif w1.lower() == "no":
        print("\nThank you for using CLI - DICTIONARY!\nHope you have an Amazing Day!\n\n")
    else:
        print("\nCouldn't get you :( \nPress 1 to try again or 2 for Adios!")
        tryagain = (input())
        if tryagain == "1":
            searchAnotherWord()
        elif tryagain == "2":
            print("\nThank you for using CLI - DICTIONARY!\nHope you have an Amazing Day!")   
        else:
            print("\nStill couldn't get you :( \nWell, Thank you for using CLI - DICTIONARY!\nHope you have an Amazing Day!")   

def getWord(word):
    if word in data:
        return data.get(word)
    elif word.capitalize() in data:
        return data.get(word.capitalize())
    elif word.upper() in data:
        return data.get(word.upper())
    elif len(get_close_matches(word, data.keys())) > 0:
        print("\nLooking for this? \"%s\"" %get_close_matches(word, data.keys())[0])
        w = input("\nYes or no: ")
        if w.lower() == "yes":
            return data.get(get_close_matches(word, data.keys())[0])
        else:
            return ("\nPlease try again as there's no such word in the English Vocabulary!")
    else:
        return ("\nSorry, there's no such word in the English Vocabulary!")
            
word = input("\nWord: ").lower()
output = getWord(word)
c = int(1)
if isinstance(output, list):
    print("\nDefinition(s) Available:")
    for i in output:
        print(f"{c}) {i}")
        c = c+1
else:
    print(output)

searchAnotherWord()