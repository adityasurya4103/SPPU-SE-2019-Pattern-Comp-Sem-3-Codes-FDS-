import array as arr

# Accept the Roll Numbers of the students

def accept_perc():
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


# Non-Recursive Ternary Search function

def ternarySearch_NR(arr, to_find):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid1 = left + (right - left) // 3
        mid2 = left + 2 * (right - left) // 3
        if to_find == arr[left]:
            return left
        elif to_find == arr[right]:
            return right
        elif to_find < arr[left] or to_find > arr[right]:
            return -1
        elif to_find <= arr[mid1]:
            right = mid1
        elif to_find > arr[mid1] and to_find <= arr[mid2]:
            left = mid1 + 1
            right = mid2
        else:
            left = mid2 + 1
    return -1


# Recursive Ternary Search

def ternarySearch_R(arr, left, right, to_find):
    if (right >= left):
        mid1 = left + (right - left) // 3;  # // operator returns the floor not float
        mid2 = right - (right - left) // 3;
        if (arr[mid1] == to_find):
            return mid1;
        if (arr[mid2] == to_find):
            return mid2;

        if (to_find < arr[mid1]):
            return ternarySearch_R(arr, left, mid1 - 1, to_find);
        elif (to_find > arr[mid2]):
            return ternarySearch_R(arr, mid2 + 1, right, to_find);
        else:
            return ternarySearch_R(arr, mid1 + 1, mid2 - 1, to_find);
    return -1;


# Driver program
if __name__ == "__main__":

    unsort_A = arr.array('I', [])  # array of unsigned integer
    ins_sort_A = arr.array('I', [])
    flag = 1

    while flag == 1:
        menu = "1. Accept Student Roll Numbers \n" \
               "2. Display the Roll Numbers \n" \
               "3. Sort Roll Numbers \n" \
               "4. Ternary Search (Non-Recursive) \n" \
               "5. Ternary Search (Recursive) \n" \
               "6. Exit"
        print(menu)
        # print("\n 1. Accept Student Roll Numbers \n 2. Display the Roll Numbers \n 3. Sort Roll Numbers \n 4. Ternary Search (Non-Recursive)  \n 5. Ternary Search (Recursive) \n 6. exit")
        choice = int(input("Enter your choice : "))

        if choice == 1:
            unsort_A = accept_perc()

        elif choice == 2:
            print_roll(unsort_A)

        elif choice == 3:
            print("Elements after sorting using Insertion Sort :")
            ins_sort_A = ins_sort(unsort_A)
            print_roll(ins_sort_A)

        elif choice == 4:
            roll = int(input("Enter the Roll Number to be search : "))

            index = ternarySearch_NR(ins_sort_A, roll)
            if index != -1:
                print("The element", roll, "is at the index", index)
            else:
                print("Element", roll, "not found!")

        elif choice == 5:
            roll = int(input("Enter the Roll Number to be search : "))
            left = 0
            right = len(ins_sort_A) - 1
            index = ternarySearch_R(ins_sort_A, left, right, roll)
            if index != -1:
                print("The element", roll, "is at the index", index)
            else:
                print("Element", roll, "not found!")

        else:
            print("Wrong choice")
            flag = 0

'''
/****************OUTPUT*******************/
1. Accept Student Roll Numbers 
2. Display the Roll Numbers 
3. Sort Roll Numbers 
4. Ternary Search (Non-Recursive) 
5. Ternary Search (Recursive) 
6. Exit

Enter your choice : 1
Enter the number of Students : 4
Enter the Roll Number : 78
Enter the Roll Number : 56
Enter the Roll Number : 49
Enter the Roll Number : 35

Enter your choice : 3
Elements after sorting using Insertion Sort :
	 35 	 49 	 56 	 78 

Enter your choice : 4
Enter the Roll Number to be search : 78
The element 78 is at the index 3

Enter your choice : 5
Enter the Roll Number to be search : 49
The element 49 is at the index 1

Enter your choice : 6
Wrong choice

'''
