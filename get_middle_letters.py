import math
def get_middleword(s):
    if len(s)%2 == 0:
        print("here")
        newwordeven = s[math.floor(len(s)/2)-1] + s[math.floor(len(s)/2)]
        return newwordeven 
    else:
        newword = s[math.floor(len(s)/2)]
        return newword


print(get_middleword("sstss"))