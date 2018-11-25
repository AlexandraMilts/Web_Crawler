#Given the names and grades for each student in a Physics class of  students,
#  store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

#Input Format
#The first line contains an integer, N, the number of students.
#The  subsequent lines describe each student over  lines;
#  the first line contains a student's name, and the second line contains their grade.

if __name__ == '__main__':
    #for _ in range(int(input())):
        #name = input()
        #score = float(input())
        n = int(input())
        marksheet = [[input(), float(input())] for _ in range(n)] #list comprehension
        marksheet.sort(key = lambda x: x[1])
        # reverse = None (Sorts in Ascending order)
        # key is set to sort using second element of sublist
        #lambda has been used as a key for sorting
        worst = marksheet[0][1]
        i = 1
        while 1<=i<=len(marksheet): #remove all with te lowest score
            if marksheet[i][1] == worst:
                del marksheet[i]
            else:
                del marksheet[0]
                break
        names =[]
        j = 1
        if len(marksheet)<= 1:
            names.append(marksheet[0][0])
        else:
            while 1<=j<len(marksheet): #make the list of the runner-ups
                if marksheet[j][1] == marksheet[0][1]:
                    names.append(marksheet[j][0])
                    j+=1
                else:
                    names.append(marksheet[0][0])
                    break
        names.sort()
        print("\n".join(names))
