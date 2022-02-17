def alphabet_position(text):
    word = text.lower()
    alphabets = ['','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    charlist = []
    for i in word:
        charlist.append(i)
    ch = []
    for j in range(len(charlist)):
        for k in range(len(alphabets)):
            if charlist[j] == alphabets[k]:
                ch.append(k)
    
    return ' '.join(map(str,ch))


print(alphabet_position("The sunset sets at twelve o' clock."))