
def find_it(seq):
    temp = max(set(seq), key=seq.count)%2!=0 
    print(temp)

#print(find_it([2,2,1]))

find_it([1,2,2,1,2])