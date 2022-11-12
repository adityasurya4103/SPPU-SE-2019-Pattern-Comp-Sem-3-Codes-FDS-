def generateSquare(n):
    # 2-D array with all
    # slots set to 0
    magicSquare = [[0 for x in range(n)]
                   for y in range(n)]

    # initialize position of 1
    i = n / 2
    j = n - 1

    # Fill the magic square
    # by placing values
    num = 1
    while num <= (n * n):
        if i == -1 and j == n:  # 3rd condition
            j = n - 2
            i = 0
        else:

            # next number goes out of
            # right side of square
            if j == n:
                j = 0

            # next number goes
            # out of upper side
            if i < 0:
                i = n - 1

        if magicSquare[int(i)][int(j)]:  # 2nd condition
            j = j - 2
            i = i + 1
            continue
        else:
            magicSquare[int(i)][int(j)] = num
            num = num + 1

        j = j + 1
        i = i - 1  # 1st condition
    print("Magic Squre for n =", n)
    print("Sum of each row or column or diagonal i.e Magic Number is : {0:.0f}".format(n * (n * n + 1) / 2), "\n")
    print_mat(magicSquare, n)


# Printing magic square
def print_mat(t, n):
    for i in range(0, n):
        for j in range(0, n):
            print(t[i][j], end=" ")
        print()


# Determine whether a given matrix is magic matrix or not

def isMagicSquare(mat, n):
    # calculate the sum of the prime diagonal
    s = 0

    for i in range(0, n):
        s = s + mat[i][i]

        # Calculate the sum of the secondary diagonal
    s2 = 0
    for i in range(0, n):
        s2 = s2 + mat[i][n - i - 1]

    if (s != s2):
        return False

    # For sums of Rows
    for i in range(0, n):
        rowSum = 0;
        for j in range(0, n):
            rowSum += mat[i][j]

            # check if every row sum is
        # equal to prime diagonal sum
        if (rowSum != s):
            return False

    # For sums of Columns
    for i in range(0, n):
        colSum = 0
        for j in range(0, n):
            colSum += mat[j][i]

            # check if every column sum is
        # equal to prime diagonal sum
        if (s != colSum):
            return False

    return True


flag = 1

while flag == 1:
    menu = " /************MENU***********/ \n" \
           "1. Generate Magic Square \n" \
           "2. Determine whether matrix is magic square or not \n" \
           "3. Exit"
    print(menu)
    choice = int(input("Enter your choice : "))
    if choice == 1:
        # Works only when n is odd
        n = int(input(" Enter the size of Magic square : "))
        generateSquare(n)

    elif choice == 2:
        # Works only when n is odd
        n = int(input(" Enter the size of Magic square : "))
        # Accept the matrix of size n X n
        # Initialize matrix
        mat = []
        print("Enter the elements rowwise:")

        # For user input
        for i in range(0, n):  # A for loop for row entries
            a = []
            for j in range(0, n):  # A for loop for column entries
                a.append(int(input("Enter element : ")))
            mat.append(a)

        if (isMagicSquare(mat, n)):
            print("Magic Square")
        else:
            print("Not a magic Square")

    else:
        print("Wrong choice")
        flag = 0

'''
/****************OUTPUT**************/
C:\Users\admin\PycharmProjects\DSL_GPA\venv\Scripts\python.exe C:/Users/admin/PycharmProjects/DSL_GPA/GPA_7.py
 /************MENU***********/ 
1. Generate Magic Square 
2. Determine whether matrix is magic square or not 
3. Exit
Enter your choice : 1
 Enter the size of Magic square : 3
Magic Squre for n = 3
Sum of each row or column or diagonal i.e Magic Number is : 15 

2 7 6 
9 5 1 
4 3 8 
 /************MENU***********/ 
1. Generate Magic Square 
2. Determine whether matrix is magic square or not 
3. Exit
Enter your choice : 2
 Enter the size of Magic square : 3
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
Not a magic Square
 /************MENU***********/ 
1. Generate Magic Square 
2. Determine whether matrix is magic square or not 
3. Exit
Enter your choice : 2
 Enter the size of Magic square : 3
Enter the elements rowwise:
Enter element : 2
Enter element : 7
Enter element : 6
Enter element : 9
Enter element : 5
Enter element : 1
Enter element : 4
Enter element : 3
Enter element : 8
Magic Square
 /************MENU***********/ 
1. Generate Magic Square 
2. Determine whether matrix is magic square or not 
3. Exit
Enter your choice : 3
Wrong choice

'''
