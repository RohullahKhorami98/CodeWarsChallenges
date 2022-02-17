import math



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

def array_diff(a,b):
    temp = []
    for i in a:
        if i not in b:
            temp.append(i)
    return temp
 
def binaryaddition(a,b):
    c = a+b
    binar = bin(c).replace("0b","")
    return binar

def get_middleword(s):
    if len(s)%2 == 0:
        print("here")
        newwordeven = s[math.floor(len(s)/2)-1] + s[math.floor(len(s)/2)]
        return newwordeven 
    else:
        newword = s[math.floor(len(s)/2)]
        return newword

def RomanToDecimal(s):
    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,            
        "M": 1000
        }
    current = 0
    previous = 0
    total = 0

    for i in range(len(s)):
        current = symbols[s[i]]
        if current > previous:
            total = total + current- 2*previous
        else:
            total += current
        previous = current
    return total

def main():
    arr1 = [1,2,2]
    arr2 =[1]
    print("difference between two arrays: " , array_diff(arr1,arr2))
    print("changing words to characters:" , duplicate_word("NtpW(!tGr(Answrcmce"))
    print("adding two decimal and result is binary: " ,binaryaddition(1,1))
    print(get_middleword("test"))
    print("Roman number to decimals: " , RomanToDecimal('DIIC'))
main()