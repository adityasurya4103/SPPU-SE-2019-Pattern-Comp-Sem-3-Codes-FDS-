'''
GROUP A- 8
Write a python program that determines the location of a saddle point of matrix if one exists.
A saddle point is an element of the matrix such that it is the minimum element in its row and maximum in its column. 
Example of matrix[3][3]:
   1 2 3
   4 5 6
   7 8 9
7 is minimum in its row and maximum in its column.
saddle point is present at matrix[2][0]

Algorithm
Traverse all rows one by one and do following for every row 
   1.Find the minimum element of current row and store column index of the minimum element.
   2.Check if the row minimum element is also maximum in its column. We use the stored column index here.
   3.If yes, then saddle point else continue till end of matrix.

'''


# Find saddle point position if present
def saddle(m):
    for i in range(0, len(m)):

        # Find the minimum element of row i.
        # Also find column index of the minimum element 
        min_row = m[i][0]
        col_ind = 0
        for j in range(1, len(m[0])):
            if min_row > m[i][j]:
                min_row = m[i][j]
                col_ind = j

        # Check if the minimum element of row is also 
        # the maximum element of column or not 
        flag = 0
        for k in range(0, len(m)):
            if min_row < m[k][col_ind]:
                flag = 1
                break

        if flag == 0:
            print("Saddle point is : ", min_row)
            print("Saddle point is present at location m[{0}][{1}]".format(i, col_ind))
            return
    print("No Saddle point present")
    return

# Read the matrix
def read_mat():
    row = int(input(" Enter the rows in the matrix : "))
    col = int(input(" Enter the columns in the matrix : "))
    # Accept the matrix of size row X col
    # Initialize matrix
    mat = []
    print("Enter the elements rowwise:")
    # For user input
    for i in range(0, row):  # A for loop for row entries
        a = []
        for j in range(0, col):  # A for loop for column entries
            a.append(int(input("Enter element : ")))
        mat.append(a)
    return mat, row, col

matrix = []
# example of no saddle point
#matrix = [[1, 2, 3], [4, 5, 6], [10, 18, 4]]
# example of saddle point
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix, row, col = read_mat()

# Print Matrix 
print("The matrix is : ")
for i in range(0, row):
    for j in range(0, col):
        print(matrix[i][j], end = " ")
    print()

saddle(matrix)

'''
/*****************OUTPUT***************/

 Enter the rows in the matrix : 3
 Enter the columns in the matrix : 3
Enter the elements rowwise:
Enter element : 1
Enter element : 2
Enter element : 3
Enter element : 4
Enter element : 5
Enter element : 6
Enter element : 7
Enter element : 8
Enter element : 9
The matrix is : 
1 2 3 
4 5 6 
7 8 9 
Saddle point is :  7
Saddle point is present at location m[2][0]

'''
