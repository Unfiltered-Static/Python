#Defining the sets
A = {1, 3, 5, 7, 9}
B = {2, 3, 5, 7, 10}

#Finding elements only in A
only_in_A = A.difference(B) 
print("Elements only in A:", only_in_A)

#Find elements only in B
only_in_B = B.difference(A)  
print("Elements only in B:", only_in_B)

#Find elements in either A or B but not in both
in_either_not_both = A.symmetric_difference(B)  
print("Elements in either A or B but not in both:", in_either_not_both)
