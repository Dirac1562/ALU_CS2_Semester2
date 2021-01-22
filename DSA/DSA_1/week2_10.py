def get_sequence(n):
    #create an empty list
    ls = []
    if n <= 0:
        #return list if n is 0 or negative
        return ls
    for n1 in range(1, n+1):
        # create a sequence of list from 1 to n using range function:
        #loop over that sequence
        for n2 in range(0, n1):
            #get the number of times we should repeat a number in the list.
            #check by doing print(n2)
            ls.append(n1)
    return ls

print(get_sequence(3)) 
print(get_sequence(5)) 