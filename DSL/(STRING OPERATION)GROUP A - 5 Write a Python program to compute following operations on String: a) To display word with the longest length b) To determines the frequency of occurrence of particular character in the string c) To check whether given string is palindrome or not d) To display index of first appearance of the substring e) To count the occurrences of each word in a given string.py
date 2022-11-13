# Count the number of characters in the longest word in the sentence

def LongestWordLength(str):
    n = len(str)
    res = 0;
    curr_len = 0;
    longest = ""

    for i in range(0, n):

        # If current character is not end of current word.
        if (str[i] != ' '):
            longest += str[i]
            curr_len += 1

        # If end of word is found
        else:
            res = max(res, curr_len)
            curr_len = 0
            longest = ""

    # We do max one more time to consider last word as there won't be any space
    # after last word.
    return max(res, curr_len), longest

# Determines the frequency of occurrence of particular character in the string
# Iterate the entire string for that particular character and then increase the
# counter when we encounter the particular character.

def countOccurance(str, char):
    count = 0
    for i in str:
        if i == char:
            count = count + 1
    return char, count


# Checks string is palindrome or not

def isPalindrome(str):
    # Run loop from 0 to len/2
    for i in range(0, int(len(str) / 2)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True


# Find all occurrences of substring in a string

def subStr(mainstr, sub):
    res = []
    flag = 0
    k = 0
    for i in range(0, len(mainstr)):
        k = i
        flag = 0
        for j in range(len(sub)):
            if mainstr[k] != sub[j]:
                flag = 1
            if flag:
                break
            k = k + 1
        if flag == 0:
            res.append(i)
    return res


# Find frequency of each word in the string
def freq(str):
    # break the string into list of words
    str = str.split()
    str2 = []

    # loop till string values present in list str
    for i in str:

        # checking for the duplicacy
        if i not in str2:
            # insert value in str2
            str2.append(i)

    print("Frequency of each word in the string is")
    for i in range(0, len(str2)):
        # count the frequency of each word(present in str2) in str and print
        print('Frequency of', str2[i], 'is :', str.count(str2[i]))


flag = 1
while flag == 1:
    print("/*************MENU**************/")
    print("1. To display word with the longest length :")
    print("2. To determines the frequency of occurrence of particular character in the string ")
    print("3. To check whether given string is palindrome or not :")
    print("4. To display index of first appearance of the substring :")
    print("5. To count the occurrences of each word in a given string :")
    print("6. Exit ")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        # s = input("Enter the String to find the longest word : ")
        s = "I am working in the department of computer engineering"
        l, str = LongestWordLength(s)
        print("Longest word is {1} of length {0}".format(l, str))

    elif choice == 2:
        # s = input("Enter the String to find the occurance of a particular character : ")
        # c = input("Enter the character whose occurance is to be find : ")
        c = "r"
        c, cnt = countOccurance(s, c)
        print("Character {0} occured {1} times in string : {2} ".format(c, cnt, s))

    elif choice == 3:
        s = input("Enter the String to check palindrome: ")
        if isPalindrome(s):
            print("Yes string {0} is palindrom ".format(s))
        else:
            print("No string {0} is not palindrom ".format(s))

    elif choice == 4:
        # s = input("Enter the main String : ")
        # s1 = input("Enter the substring : ")
        s = "I am working in the department of computer engineering"
        s1 = "ing"
        print("starting indices of substring {1} in string {0} is {2} ".format(s, s1, subStr(s, s1)))

    elif choice == 5:
        s = "apple mango apple orange orange apple guava mango mango"
        freq(s)

    else:
        print("Wrong choice")
        flag = 0

'''
/********************OUTPUT***********************/
/*************MENU**************/
1. To display word with the longest length :
2. To determines the frequency of occurrence of particular character in the string 
3. To check whether given string is palindrome or not :
4. To display index of first appearance of the substring :
5. To count the occurrences of each word in a given string :
6. Exit 
Enter your choice : 1
Longest word is engineering of length 11
/*************MENU**************/
1. To display word with the longest length :
2. To determines the frequency of occurrence of particular character in the string 
3. To check whether given string is palindrome or not :
4. To display index of first appearance of the substring :
5. To count the occurrences of each word in a given string :
6. Exit 
Enter your choice : 2
Character r occured 4 times in string : I am working in the department of computer engineering 
/*************MENU**************/
1. To display word with the longest length :
2. To determines the frequency of occurrence of particular character in the string 
3. To check whether given string is palindrome or not :
4. To display index of first appearance of the substring :
5. To count the occurrences of each word in a given string :
6. Exit 
Enter your choice : 3
Enter the String to check palindrome: radar
Yes string radar is palindrom 
/*************MENU**************/
1. To display word with the longest length :
2. To determines the frequency of occurrence of particular character in the string 
3. To check whether given string is palindrome or not :
4. To display index of first appearance of the substring :
5. To count the occurrences of each word in a given string :
6. Exit 
Enter your choice : 3
Enter the String to check palindrome: computer
No string computer is not palindrom 
/*************MENU**************/
1. To display word with the longest length :
2. To determines the frequency of occurrence of particular character in the string 
3. To check whether given string is palindrome or not :
4. To display index of first appearance of the substring :
5. To count the occurrences of each word in a given string :
6. Exit 
Enter your choice : 4
starting indices of substring ing in string I am working in the department of computer engineering is [9, 51] 
/*************MENU**************/
1. To display word with the longest length :
2. To determines the frequency of occurrence of particular character in the string 
3. To check whether given string is palindrome or not :
4. To display index of first appearance of the substring :
5. To count the occurrences of each word in a given string :
6. Exit 
Enter your choice : 5
Frequency of each word in the string is
Frequency of apple is : 3
Frequency of mango is : 3
Frequency of orange is : 2
Frequency of guava is : 1
/*************MENU**************/
1. To display word with the longest length :
2. To determines the frequency of occurrence of particular character in the string 
3. To check whether given string is palindrome or not :
4. To display index of first appearance of the substring :
5. To count the occurrences of each word in a given string :
6. Exit 
Enter your choice : 6
Wrong choice

'''
