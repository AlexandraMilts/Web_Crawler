def measure_udacity(p):
    count = 0
    for u in p:
        if u[0] == "U":
            count+=1
    return count

#print(measure_udacity(['Dave','Sebastian','Katy']))
#>>> 0

print(measure_udacity(['Umika','Umberto']))
#>>> 2