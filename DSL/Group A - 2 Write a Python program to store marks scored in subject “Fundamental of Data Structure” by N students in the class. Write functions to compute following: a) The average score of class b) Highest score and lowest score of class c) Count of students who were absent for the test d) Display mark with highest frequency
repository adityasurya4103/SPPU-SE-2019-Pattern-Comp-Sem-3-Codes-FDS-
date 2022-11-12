# The average score of class

def average(l):
    sum = 0
    cnt = 0
    for i in range(len(l)):
        if l[i] != -999:
            sum += l[i]
            cnt += 1

    avg = sum / cnt
    print("Total Marks are : ", sum)
    print("Average Marks are : {:.2f}".format(avg))


# Highest score in the class

def Maximum(l):
    Max = l[0]
    for i in range(len(l)):
        if l[i] > Max:
            Max = l[i]
    return (Max)


# Lowest score in the class


def Minimum(l):
    # Assign first element in the array which corresponds to marks of first present student
    # This for loop ensures the above condition

    for i in range(len(l)):
        if l[i] != -999:
            Min = l[i]
            break

    for j in range(i + 1, len(l)):
        if l[j] != -999 and l[j] < Min:
            Min = l[j]
    return (Min)


# Count of students who were absent for the test

def absentCnt(l):
    cnt = 0
    for i in range(len(l)):
        if l[i] == -999:
            cnt += 1
    return (cnt)


# Display mark with highest frequency
# refeence link : https://www.youtube.com/watch?v=QrIXGqvvpk4&t=422s
def maxFrequency(l):
    i = 0
    Max = 0
    print(" Marks ----> frequency count ")
    for ele in l:
        if l.index(ele) == i:
            print(ele, "---->", l.count(ele))
            if l.count(ele) > Max:
                Max = l.count(ele)
                mark = ele
        i += 1
    return (mark, Max)


# Input the number of students and their corresponding marks in FDS

marksInFDS = []
noStudents = int(input("Enter total number of students : "))
for i in range(noStudents):
    marks = int(input("Enter marks of Student " + str(i + 1) + " : "))
    marksInFDS.append(marks)

flag = 1
while flag == 1:
    print("/*************MENU**************/")
    print("1. The average score of class ")
    print("2. Highest score and lowest score of class ")
    print("3. Count of students who were absent for the test ")
    print("4. Display mark with highest frequency ")
    print("5. Exit ")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        average(marksInFDS)

    elif choice == 2:
        print("Highest score in the class is : ", Maximum(marksInFDS))
        print("Lowest score in the class is : ", Minimum(marksInFDS))

    elif choice == 3:
        print("Count of students who were absent for the test is : ", absentCnt(marksInFDS))

    elif choice == 4:
        mark, count = maxFrequency(marksInFDS)
        print("Highest frequency of marks {0} is {1} ".format(mark, count))

    else:
        print("Wrong choice")
        flag = 0

'''
/*********************OUTPUT********************/
Enter marks of Student 1 : 87
Enter marks of Student 2 : 68
Enter marks of Student 3 : -999
Enter marks of Student 4 : 90
Enter marks of Student 5 : 68
/*************MENU**************/
1. The average score of class 
2. Highest score and lowest score of class 
3. Count of students who were absent for the test 
4. Display mark with highest frequency 
5. Exit 
Enter your choice : 1
Total Marks are :  313
Average Marks are : 78.25
/*************MENU**************/
1. The average score of class 
2. Highest score and lowest score of class 
3. Count of students who were absent for the test 
4. Display mark with highest frequency 
5. Exit 
Enter your choice : 2
Highest score in the class is :  90
Lowest score in the class is :  68
/*************MENU**************/
1. The average score of class 
2. Highest score and lowest score of class 
3. Count of students who were absent for the test 
4. Display mark with highest frequency 
5. Exit 
Enter your choice : 3
Count of students who were absent for the test is :  1
/*************MENU**************/
1. The average score of class 
2. Highest score and lowest score of class 
3. Count of students who were absent for the test 
4. Display mark with highest frequency 
5. Exit 
Enter your choice : 4
 Marks ----> frequency count 
87 ----> 1
68 ----> 2
-999 ----> 1
90 ----> 1
Highest frequency of marks 68 is 2 
/*************MENU**************/
1. The average score of class 
2. Highest score and lowest score of class 
3. Count of students who were absent for the test 
4. Display mark with highest frequency 
5. Exit 
Enter your choice : 5
Wrong choice
