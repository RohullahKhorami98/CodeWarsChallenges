def find_max_odd_number(seq):
    temp = []
    oddnumbers = 0
    for i in seq:
        if i%2!=0:
          temp.append(i)
    oddnumbers = max(set(temp), key=temp.count)
    return oddnumbers


print(find_max_odd_number([12,1,2]))