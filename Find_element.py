#with while loop
def find_element_while(p, e):
    i = 0
    while i < len(p):
        if p[i] == e:
            return i
        i+=1
    return -1

#with for loop
def find_element_for(p, e):
    i = 0
    for t in p:
        if t == e:
            return i
        i+=1
    return -1


#To find the fist position you can also use index
#p.index(e)


#To find out if e is at all in the list simply use in
#print e in p
#or even
#print e not in p
#--> True or False

def find_element(p, e):
    if e not in p:
        return(-1)
    else:
        return p.index(e)


print(find_element([1,2,3],3))
print(find_element_for(['alpha','beta'],'gamma'))


