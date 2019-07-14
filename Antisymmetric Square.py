# By Dimitris_GR from forums
# Modify Problem Set 31's (Optional) Symmetric Square to return True
# if the given square is antisymmetric and False otherwise.
# An nxn square is called antisymmetric if A[i][j]=-A[j][i]
# for each i=0,1,...,n-1 and for each j=0,1,...,n-1.

def antisymmetric(A):
    for q in range(len(A)):
        if len(A) != len(A[q]):
            return False

    merged_list = []

    lists_swapped = [list(i) for i in zip(*A)]

    for l in A:
        merged_list += l

    merged_list_swapped = []

    for i in lists_swapped:
        merged_list_swapped += i

    for n in merged_list:
        if merged_list[n] != -merged_list_swapped[n]:
            return False
    return True


# Test Cases:

print
antisymmetric([[0, 1, 2],
               [-1, 0, 3],
               [-2, -3, 0]])
# >>> True

print
antisymmetric([[0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]])
# >>> True

print
antisymmetric([[0, 1, 2],
               [-1, 0, -2],
               [2, 2, 3]])
# >>> False

print
antisymmetric([[1, 2, 5],
               [0, 1, -9],
               [0, 0, 1]])
# >>> False


print
antisymmetric([[0, 0],
               [0, 0],
               [0, 0],
               [0, 0]])