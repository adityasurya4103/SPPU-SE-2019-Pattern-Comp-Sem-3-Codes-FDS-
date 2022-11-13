import array as arr


# Accept the Roll Numbers of the students

def accept_roll():
    a = arr.array('I', [])
    no_stud = int(input("Enter the number of Students : "))
    for i in range(0, no_stud):
        a.append(int(input("Enter the Roll Number : ")))
    return a


# Print the Roll Numbers of the Students

def print_roll(a):
    for i in range(0, len(a)):
        print("\t", a[i], end=" ")
    print()


# Linear Search

def linear_search(a, x):
    for i in range(len(a)):

        if a[i] == x:
            return i

    return -1


# Sentinel Search

def sentinel_search(a, x):
    count = len(a)
    a.append(x)
    i = 0

    while a[i] != x:
        i = i + 1

    if i != count:
        return i
    else:
        return -1


#  Binary Search recursive
# Returns index of x in arr if present, else -1

def binary_search_R(a, l, r, x):
    # Check base case
    if r >= l:

        mid = l + (r - l) // 2

        # If element is present at the middle itself
        if a[mid] == x:
            return mid

            # If element is smaller than mid, then it
        # can only be present in left subarray
        elif a[mid] > x:
            return binary_search_R(a, l, mid - 1, x)

            # Else the element can only be present
        # in right subarray
        else:
            return binary_search_R(a, mid + 1, r, x)

    else:
        # Element is not present in the array
        return -1


# Python3 code to implement iterative Binary
# Search.

# It returns location of x in given array arr
# if present, else returns -1
def binary_search_NR(a, l, r, x):
    while l <= r:

        mid = l + (r - l) // 2;

        # Check if x is present at mid
        if a[mid] == x:
            return mid

            # If x is greater, ignore left half
        elif a[mid] < x:
            l = mid + 1

        # If x is smaller, ignore right half
        else:
            r = mid - 1

    # If we reach here, then the element
    # was not present
    return -1


# Fibonacci Search

def fibonacci_search(a, x):
    # Initialize the Fibonacci numbers
    fib1, fib2 = 1, 0
    fibn = fib2 + fib1
    a_len = len(a)
    while fibn < a_len:
        fib2 = fib1
        fib1 = fibn
        fibn = fib2 + fib1
    ind = -1
    while fibn > 1:
        n = min(ind + fib2, a_len - 1)
        if a[n] > x:
            fibn = fib2
            fib1 = fib1 - fib2
            fib2 = fibn - fib1
        elif a[n] < x:
            fibn = fib1
            fib1 = fib2
            fib2 = fibn - fib1
            ind = n
        else:
            return n
    if a[ind + 1] == n and fib1 == 1:
        return ind + 1
    return -1


# Insertion sort

def ins_sort(a):
    # Traverse through 1 to len(a)
    for i in range(1, len(a)):

        key = a[i]

        # Move elements of a[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# Driver program
if __name__ == "__main__":

    unsort_A = arr.array('I', [])  # array of unsigned integer
    ins_sort_A = arr.array('I', [])
    flag = 1

    while flag == 1:
        menu = "1. Accept Student Roll Numbers of students who attended training program\n" \
               "2. Display the Roll Numbers of students who attended training program\n" \
               "3. Linear Search \n" \
               "4. Sentinel Search \n" \
               "5. Insertion Sort \n" \
               "6. Binary Search (Recursive) \n" \
               "7. Binary Search (Non-Recursive) \n" \
               "8. Fibonacci Search \n" \
               "9. Exit \n "
        print(menu)

        choice = int(input("Enter your choice : "))

        if choice == 1:
            unsort_A = accept_roll()

        elif choice == 2:
            print_roll(unsort_A)

        elif choice == 3:
            roll = int(input("Enter the Roll Number to be search : "))

            index = linear_search(unsort_A, roll)
            if index != -1:
                print("Roll number", roll, " at the index", index, "has Attended the training program")
            else:
                print("Roll number", roll, "has not Attended the training program")

        elif choice == 4:
            roll = int(input("Enter the Roll Number to be search : "))

            index = sentinel_search(unsort_A, roll)
            if index == -1:
                print("Roll number", roll, "has not Attended the training program")
            else:
                print("Roll number", roll, " at the index", index, "has Attended the training program")

        elif choice == 5:
            print("Elements after sorting using Insertion Sort :")
            ins_sort_A = ins_sort(unsort_A)
            print_roll(ins_sort_A)

        elif choice == 6:
            roll = int(input("Enter the Roll Number to be search : "))

            index = binary_search_R(unsort_A, 0, len(unsort_A) - 1, roll)
            if index == -1:
                print("Roll number", roll, "has not Attended the training program")
            else:
                print("Roll number", roll, " at the index", index, "has Attended the training program")

        elif choice == 7:
            roll = int(input("Enter the Roll Number to be search : "))

            index = binary_search_NR(unsort_A, 0, len(unsort_A) - 1, roll)
            if index == -1:
                print("Roll number", roll, "has not Attended the training program")
            else:
                print("Roll number", roll, " at the index", index, "has Attended the training program")

        elif choice == 8:
            roll = int(input("Enter the Roll Number to be search : "))

            index = fibonacci_search(unsort_A, roll)
            if index == -1:
                print("Roll number", roll, "has not Attended the training program")
            else:
                print("Roll number", roll, " at the index", index, "has Attended the training program")

        else:
            print("Wrong choice")
            flag = 0
'''
/*******************OUTPUT*****************/

1. Accept Student Roll Numbers of students who attended training program
2. Display the Roll Numbers of students who attended training program
3. Linear Search 
4. Sentinel Search 
5. Insertion Sort 
6. Binary Search (Recursive) 
7. Binary Search (Non-Recursive) 
8. Fibonacci Search 
9. Exit 
 
Enter your choice : 1
Enter the number of Students : 5
Enter the Roll Number : 34
Enter the Roll Number : 56
Enter the Roll Number : 52
Enter the Roll Number : 18
Enter the Roll Number : 9
 
Enter your choice : 2
	 34 	 56 	 52 	 18 	 9 

Enter your choice : 3
Enter the Roll Number to be search : 18
Roll number 18  at the index 3 has Attended the training program
 
Enter your choice : 4
Enter the Roll Number to be search : 34
Roll number 34  at the index 0 has Attended the training program

Enter your choice : 5
Elements after sorting using Insertion Sort :
	 9 	 18 	 34 	 34 	 52 	 56 

Enter your choice : 6
Enter the Roll Number to be search : 34
Roll number 34  at the index 2 has Attended the training program

Enter your choice : 7
Enter the Roll Number to be search : 18
Roll number 18  at the index 1 has Attended the training program

Enter your choice : 8
Enter the Roll Number to be search : 56
Roll number 56  at the index 5 has Attended the training program

Enter your choice : 9
'''
