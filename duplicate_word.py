"""
This program is about to change a string in two some character
"""

def duplicate_word(word):
    newword = word.lower()
    words = []
    converted=[]
    myword = ""
    for char in newword:
        words.append(char)
    for i in words:
        if words.count(i)>1:
            i = ")"
            converted.append(i)
        else: 
            i = "("
            converted.append(i)
    myword = ''.join(converted)
    return myword




print(duplicate_word("ttttt"))