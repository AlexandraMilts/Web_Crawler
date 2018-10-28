def find_element_while(p, e):
    i = 0
    while i < len(p):
        if p[i] == e:
            return i
        i+=1
    return -1

def find_element_for(p, e):
    i = 0
    for t in p:
        if t == e:
            return i
        i+=1
    return -1

print(find_element_while([1,2,3],3))
print(find_element_for(['alpha','beta'],'gamma'))


