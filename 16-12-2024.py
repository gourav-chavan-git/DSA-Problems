#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      91932
#
# Created:     16-12-2024
# Copyright:   (c) 91932 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Write the code to find the Fibonacci series upto the nth term.

##def fib(n): # 5
##    a,b = 0,1
##    print('The fibonacci series is:',a,b,end=' ')
##    i = 2
##    while i <n:
##        a,b = b,a+b
##        i = i + 1
##        print(b,end=' ')
##n = int(input('Enter nth term: '))
##fib(n)


# Write a code to reverse a number

##def reverse(num): #0 --> 54321
##    temp = num
##    reverse = 0 #54321
##    while num > 0:
##        digit = num%10 # 1,2,3,4,5
##        reverse = reverse*10 + digit
##        num = num // 10
##    print(f'The reverse of {temp} is {reverse}')
##num = int(input('Enter number: '))
##reverse(num)


# Write a code to replace a substring in a string.

#str = 'python is a fun lenaguage!'
#str1 = 'python'
#str2 = 'java'
##def func(str,str1,str2):
##
##    words = str.split()
##    n =words.count(str1)
##    for _ in range(n):
##        idx = words.index(str1)
##        words[idx] = str2
##    str = ' '.join(words)
##    return str
##str = 'python is fun language also python is easy'
##str1 = 'python'
##str2 = 'java'
##print(func(str,str1,str2))

# Another way to do this...
##def func(str,str1,str2):
##    str = str.replace(str1,str2)
##    return str
##str = 'python is fun language also python! is easy'
##str1 = 'python'
##str2 = 'java'
##print(func(str,str1,str2))


# Write a code to replace each element in an array by its rank in the array

##def replace(arr): # arr = [100, 2, 70, 12 , 90]
##    for idx,ele in enumerate(sorted(arr)):
##        arr[arr.index(ele)] = idx + 1
##    return arr
##arr = [100, 2, 70, 12 , 90]
##print(replace(arr))


# Write a code to find non-repeating elements in an array.

##def unique(arr):
##    for ele in arr:
##        count = arr.count(ele)
##        if count > 1:
##            continue
##        else:
##            print(ele,end=' ') # 30, 40, 50
##arr = [10, 30, 40, 20, 10, 20, 50, 10]
##unique(arr)

# Another way to do this...
##def unique(arr):
##    d = {}
##    for ele in arr:
##        d[ele] = d.get(ele,0) + 1
##    for ele,count in d.items():
##        if count == 1:
##            print(ele,end=' ')
##arr = [10, 30, 40, 20, 10, 20, 50, 10]
##unique(arr)


# Write a code to check for the longest palindrome in an array.

##def is_palindrome(num):
##    return True if str(num)==str(num)[::-1] else False
##
##def l_palindrome(arr):
##    longest_palindrome = None
##    max_length = 0
##    for num in arr:
##        if is_palindrome(num):
##            if len(str(num)) > max_length:
##                max_length = len(str(num))
##                longest_palindrome = num
##    return longest_palindrome
##arr = [1, 232, 5545455, 909090, 161]
##result = l_palindrome(arr)
##print(f'The longest palindrome in the array is: {result}')

#  Write a code to find the factorial of a number.

##def fact(num): #5
##    if num == 1:
##        return 1
##    return num*fact(num - 1) #5*4*3*2*1
##num = int(input('Enter number: '))
##factorial = fact(num)
##print(f'The factorial of {num} is {factorial}')

# Another way to do this... (Using for loop)

##def fact(num):
##    factorial = 1
##    for i in range(2,num+1):
##        factorial *= i
##    return factorial
##num = int(input('Enter number: '))
##fact = fact(num)
##print(f'The factorial of {num} is {fact}')


# Write the code for Armstrong number

##def armstrong(num): #153
##    tem = num
##    sum = 0
##    pow = len(str(num)) #3
##    for _ in range(pow): #0,1,2
##        digit = num%10
##        sum += digit**pow
##        num = num//10
##    return True if sum == tem else False
##num = int(input('Enter number: '))
##if armstrong(num):
##    print('Armstrong!')
##else:
##    print('Not Armstrong!')



# Write a program to find the sum of Natural Numbers using Recursion.

##def sum(num): #5 = 5
##    if num == 1:
##        return 1
##    return num + sum(num - 1) # 5+4+3+2+1
##num = int(input('Enter number: '))
##output = sum(num)
##print(f'The sum of first {num} natural numbers is: {output}')



# Write a program to add Two Matrices using Multi-dimensional Array.

##def add_matrices(matrix1,matrix2):
##    rows = len(matrix1)
##    cols = len(matrix1[0])
##    result = [[0 for _ in range(cols)] for _ in range(rows)]
##    for i in range(rows):
##        for j in range(cols):
##            result[i][j] = matrix1[i][j] + matrix2[i][j]
##    return result
##matrix1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
##matrix2 = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
##result = add_matrices(matrix1,matrix2)
##print('The resultant matrix after matrix addition is:', result)


# Write a program to subtract Two Matrices using Multi-dimensional Array.

##def add_matrices(matrix1,matrix2):
##    rows = len(matrix1)
##    cols = len(matrix1[0])
##    result = [[0 for _ in range(cols)] for _ in range(rows)]
##    for i in range(rows):
##        for j in range(cols):
##            result[i][j] = matrix1[i][j] - matrix2[i][j]
##    return result
##matrix1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
##matrix2 = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
##result = add_matrices(matrix1,matrix2)
##print(f'The resultant matrix after matrix subtraction is:', result)


# # Write a program to multiply Two Matrices using Multi-dimensional Array.

##def add_matrices(matrix1,matrix2):
##    rows = len(matrix1)
##    cols = len(matrix1[0])
##    result = [[0 for _ in range(cols)] for _ in range(rows)]
##    for i in range(rows):
##        for j in range(cols):
##            result[i][j] = matrix1[i][j] * matrix2[i][j]
##    return result
##matrix1 = matrix1 = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
##matrix2 = matrix2 = [[9, 8, 7],[6, 5, 4],[3, 2, 1]]
##result = add_matrices(matrix1,matrix2)
##print(f'The resultant matrix after matrix multiplication is:', result)



#  Write code to check a String is palindrome or not?

##def is_palindrome(str): #malayalam
##    return str == str[::-1]
##str = input('Enter string: ')
##if is_palindrome(str):
##    print('Yes!')
##else:
##    print('No!')



# Write a program for Binary to Decimal conversion

##def binary_to_decimal(num): # 1011 -> 11
##    decimal = 0
##    pow = 0
##    for i in num[::-1]: # 1 1 0 1
##        decimal += int(i)*(2**pow)
##        pow+=1
##    return decimal
##num = input('Enter binary number: ')
##result = binary_to_decimal(num)
##print(f'The decimal number equivalent of binary number {num} is: {result}')


# Write a program for Decimal to Binary conversion

##def deci_to_bin(num): # 13
##    rem = ''   #'1101'
##    quo = num
##    while quo>0: #13 6 3 1
##        rem = str(quo%2) + rem
##        quo = quo//2 #6 3 1
##    return rem
##num = int(input('Enter decimal number: '))
##remainder = deci_to_bin(num)
##print(f'The binary equivalent of decimal {num} is: {int(remainder)}')


# Write a program to check whether a character is a vowel or consonant

##def func(char):
##    return True if char.lower() in ['a','e','i','o','u'] else False
##char = input('Enter character: ')
##if func(char):
##    print(f'It\'s Vowel!')
##else:
##    print(f'It\'s Consonant!')


#An automorphic number is a number whose square ends in the same digits as the number itself.
# For example, 25 is an automorphic number because (25**2 = 625)

##def is_automorphic(num): # 25
##    square = num**2 #625
##    return True if num == int(str(square)[-len(str(num)):]) else False
##num = int(input('Enter number: '))
##if is_automorphic(num):
##    print(f'The number {num} is Automorphic!')
##else:
##    print(f'The number {num} is not Automorphic!')



# Write a code to find Find the ASCII value of a character

##def ascci_finder(char):
##    value = ord(char)
##    return value
##char = input('Enter character: ')
##value = ascci_finder(char)
##print(f'The ascii value of given character is: {value}')



# Write a code to Remove all characters from string except alphabets

##def is_alphabet(str):
##    output = ''
##    for char in str:
##        if (ord(char) >=65 and ord(char)<=90) or (ord(char) >=97 and ord(char)<=122):
##            output += char
##    str = output
##    print('The string with only alphabets is:', str)
##str = input('Enter your string: ')
##is_alphabet(str)


# Write a function to check whether given string contains all characters from alphabets
# code to chech whether string is pengram or not.
# str = 'the quick brown fox jumps over the lazy dog'
##def all_alphas(str):
##    letters = set()
##    for char in str:
##        if char.lower() not in letters:
##            if ord(char.lower())>=65 and ord(char)<=90:
##                letters.add(char.lower())
##    return True if len(letters) == 26 else False
##str = input('Enter string: ')
##if all_alphas(str):
##    print('String is pengram!')
##else:
##    print('Not pengram!')



# Write a code to Print the smallest and largest element from the array

##def func(arr): # arr = [1,4,3,6,8,9,5]
##    smallest = arr[0] # 1
##    largest = arr[0] # 1
##    for num in arr: # 1,4,3,6
##        if num < smallest:
##            smallest = num
##        if num > largest:
##            largest = num #4,6,8,9
##    return smallest, largest
##arr = [1,4,3,6,8,9,5]
##smallest,largest = func(arr)
##print(f'The smallest number is: {smallest}')
##print(f'The largest number is: {largest}')



# Write a code to Reverse the element of the array

##def reverse(arr):
##    start = 0
##    end = len(arr) - 1
##    while start < end:
##        arr[start],arr[end] = arr[end],arr[start]
##        start += 1
##        end -= 1
##    return arr
##arr = [10, 20, 30, 40, 50]
##print(reverse(arr))


# Write a code to Replace a Substring in a string

##def func(string,what_t_r,with_w_t_r):
##    temp = string
##    words = string.split()
##    count = words.count(what_t_r)
##    for _ in range(count):
##        idx = words.index(what_t_r)
##        words[idx] = with_w_t_r
##    string = ' '.join(words)
##    return string,temp
##string = input('Enter string: ')
##what_t_r = input('what you want to replace: ')
##with_w_t_r = input('Enter replacement: ')
##string,temp = func(string,what_t_r,with_w_t_r)
##print(f'The string before replacement is: \n{temp}')
##print(f'The string after replacement is: \n{string}')


# Write a code to Remove space from a string

##def space_remover(string):
##    string = ''.join(string.split())
##    return string
##string = input('Enter string: ')
##string = space_remover(string)
##print('The string after removing spaces is:',string)


# Write a code to Count Inversion

# Inversions: A pair (A[i], A[j]) is said to be in inversion if:

##    A[i] > A[j]
##    i < j

##Input: A = [3, 2, 1]
##Output: 3
##Explanation: The three pairs of inversions are – (3, 2) , (3, 1), (2, 1)

##def inversion_counter(arr):
##    count = 0
##    pairs = []
##    for i in range(len(arr)):
##        for j in range(i+1,len(arr)):
##            if arr[i] > arr[j]:
##                pairs.append((arr[i],arr[j]))
##                count += 1
##    return count,pairs
##arr = [3, 2, 1]
##count,pairs = inversion_counter(arr)
##print('Total inversions found are:',count)
##print(f'These inversion pairs are: \n{pairs}')


# Write a Program to Find out the Sum of Digits of a Number.

##def digit_sum_calculator(num): #12345 == 15
##    sum_of_digits = 0
##    for digit in num:
##        sum_of_digits += int(digit)
##    return sum_of_digits
##num = input('Enter your number: ')
##r = digit_sum_calculator(num)
##print(f'The sum of digits of number {num} is: {r}')


# Write a Program to Find out the Power of a Number
##def power_finder(num,power): #2,2
##    result = 1
##    for _ in range(power):#0,1
##        result *= num
##    return result
##num = int(input('Enter number: '))
##power = int(input('Enter power: '))
##result = power_finder(num,power)
##print(f'{num} to the power of {power} is {result}')


# Write a Program to Add two Fractions
##import math
##def fraction_adder(n1,d1,n2,d2):
##    lcm = math.lcm(d1,d2)
##    a = lcm//d1
##    b = lcm//d2
##    fraction = (n1*a + n2*b)/lcm
##    return fraction
##n1,n2 = map(int, input('Enter numerator n1 and n2: ').split())
##d1,d2 = map(int, input('Enter denominator d1 and d2: ').split())
##result = fraction_adder(n1,d1,n2,d2)
##print(f'The added fraction of is: {result}')



# Write a Program to Find the Largest Element in an Array.

##def max_finder(arr): # arr = [1,4,3,6,8,9,5]
##    largest = arr[0]
##    for i in range(1,len(arr)):
##        if arr[i]>largest:
##            largest = arr[i]
##    return largest
##arr = [1,4,3,6,8,9,5]
##largest = max_finder(arr)
##print(f'The array is:\n{arr}')
##print(f'The largest element in the array is: {largest}')


# Write a Program to Find the Roots of a Quadratic Equation

##    Consider an arbitrary quadratic equation: ax2 + bx + c = 0, a ≠ 0
##    Roots are:
##    r1 = (-b + math.sqrt(b**2 - 4*a*c))/2*a
##    r1 = (-b - math.sqrt(b**2 - 4*a*c))/2*a
##    Sum of the Roots: α + β = -b/a = - Coefficient of x/ Coefficient of x2
##    Product of the Roots: αβ = c/a = Constant term/ Coefficient of x2

##import math
##def roots_finder(a,b,c):
##    discriminant = b**2 - 4*a*c
##    op =  math.sqrt(discriminant)
##    r1 = (-b + op) / 2*a
##    r2 = (-b - op) / 2*a
##    return r1,r2
##a,b,c = map(int, input('Enter coefficients a,b & constant c: ').split())
##root1,root2 = roots_finder(a,b,c)
##print(f'The Quadratic equation is: ({a})x**2 + ({(b)})x + ({c}) = 0')
##print(f'The roots are: \nroot1 = {root1:.2f}\nroot2 = {root2:.2f}')



#  Write a Program to Find the Prime Factors of a Number.

##def prime_factors(num):
##    factors = []
##    divisor = 2
##    while num > 1:
##        while num%divisor==0:
##            factors.append(divisor)
##            num = num // divisor
##        divisor +=1
##    return factors
##num = int(input('Enter number: '))
##if num <= 1:
##    print('The number should be greater than 1')
##else:
##    factors = prime_factors(num)
##    print(f'The prime factors of {num} are: {factors}')



# Write a Program to Convert Digits to Words.

##def digits_to_words(num):
##    digit_to_word = {0:'Zero',1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine'}
##    words = [digit_to_word[int(digit)] for digit in num]
##    return ' '.join(words)
##num = input('Enter Number: ')
##print(f'The number {num} in words is: {digits_to_words(num)}')


# Write a Program to Find the Factorial of a Number using Recursion.

##def factorial(num):
##    if num ==1:
##        return 1
##    return num * factorial(num - 1)
##num = int(input('Enter Number: '))
##factorial = factorial(num)
##print(f'The factorial of number {num} is {factorial}')


# Write a Program to Reverse an Array

##def rev(arr): # arr = [10, 20, 30, 40, 50, 60]
##    start = 0
##    end = len(arr) - 1
##    while start < end:
##        arr[start],arr[end] = arr[end],arr[start]
##        start += 1
##        end -= 1
##    return arr
##arr = [10, 20, 30, 40, 50, 60]
##reversed_arr = rev(arr)
##print(f'The array in reverse order is:\n{reversed_arr}')


# Write a code to find Fibonacci Series upto first 10 numbers.

##def fib():
##    a,b = 0,1
##    print('The fibonacci series is:',a,b,end=' ')
##    i = 10
##    while i>2:
##        a,b = b,a+b
##        print(b,end=' ')
##        i -= 1
##fib()

# Write a code to check given number is a perfect number or not.
# A perfect number is a positive integer that is equal to the sum
# of its positive proper divisors, excluding the number itself.
# For example, the number 6 has divisors 1, 2, and 3, and 1 + 2 + 3 = 6,
# making it a perfect number
# The first few perfect numbers are 6, 28, 496, and 8128
##def is_perfect(num): # 6
##    divisor_sum = 0
##    for i in range(1,num):
##        if num%i==0:
##            divisor_sum += i
##    return True if num == divisor_sum else False
##num = int(input('Enter your number: '))
##if is_perfect(num):
##    print(f'The number {num} is a perfect number.')
##else:
##    print(f'Not perfect!')


# Write a code to check for neon number.
# for example: num = 9 -> square == 9*9 = 81 -> 8 + 1 -> 9 == num -> Neon Number

##def is_neon(num):
##    square = num*num # 81
##    sum = 0
##    while square >0:
##        sum += square%10 # 1+8 = 9
##        square //= 10 # 8
##    return True if num == sum else False
##num = int(input('Enter Number: '))
##if is_neon(num):
##    print('Neon!')
##else:
##    print('Not Neon!')


# Write a program to check given number is a spy number or not.
#for example: num = 1124, sum = 1+1+2+4 = 8 and product = 1*1*2*4 = 8,spy-number

##def is_spy(num): # 1124
##    sum = 0
##    product = 1
##    while num>0:
##        digit = num%10 #4
##        sum += digit
##        product *= digit
##        num //= 10 # 112p
##    return True if sum == product else False
##num = int(input('Enter Number: '))
##if is_spy(num):
##    print('Spy Number!')
##else:
##    print('Not!')



# Write a program to check magic number.
# for example: num =1729, sum_of_digits = 1+7+2+9 = 19,
# reverse_of_sum_of_digits = 91, 19*91 == 1729

##def is_magic(num): #1729
##    temp = num
##    sum = 0 # 9+2+7+1=19
##    while num>0: #1729,172,17,1
##        sum += num%10 #9,2,7,1
##        num //= 10 #172,17,1,0
##    return True if sum * int(str(sum)[::-1]) == temp else False
##num = int(input('Enter Number: '))
##if is_magic(num):
##    print(f'{num} is magic number!')
##else:
##    print('Not!')



# Write a code to check special number.
#example: num = 145, 1! + 4! + 5! == 145 --> Special Number

##def fact(num): #5
##    if num == 1:
##        return 1
##    return num * fact(num - 1) # 5*4*3*2*1
##
##def is_special(num):
##    temp = num
##    factorial_sum = 0
##    while num>0:
##        factorial_sum += fact(num%10)
##        num //= 10
##    return True if factorial_sum == temp else False
##num = int(input('Enter Number: '))
##if is_special(num):
##    print(f'Number {num} is a special number!')
##else:
##    print('Not!')


# Write a code to display the sum of first n terms of odd natural numbers.
# example: 5 terms -> 1 + 3 + 5 + 7 + 9 == 25

##def find_sum(n): # 5
##    sum = 0
##    i = n*2 -1 # 9
##    while i>=1:
##        sum += i
##        i -= 2
##    return sum
##n = int(input('Enter nth terms: '))
##sum = find_sum(n)
##print(f'The sum of first {n} odd natural numbers is {sum}')


# Write a code to display the sum of first n terms of even natural numbers.
# example: 5 terms -> 2 + 4 + 6 + 8 + 10 == 30

##def find_sum(n): # 5
##    sum = 0
##    i = n*2  # 10
##    while i>=2:
##        sum += i
##        i -= 2
##    return sum
##n = int(input('Enter nth terms: '))
##sum = find_sum(n)
##print(f'The sum of first {n} even natural numbers is {sum}')


# A number is referred to as a tech number in python if it has an even number of
# digits and can be divided exactly into two parts from the middle.
# example: number = 2025
#divide the number into two equal parts
# first part = 20 & second part = 25
# sum = first part + second part = 20 +25 = 45
#square the obtained 'sum', square_sum = 45*45 = 2025 == number
# Therefore 2025 is a tech number.


##def is_tech(num):  # 2025
##    idx = len(num)//2
##    if len(num)%2!=0:
##        print('Invalid Number! Try to input even numbered digit')
##    else:
##        first_part = int(num[:idx])
##        second_part = int(num[idx:])
##        sum = first_part + second_part
##        square_sum = sum * sum
##        return True if square_sum == int(num) else False
##num = input('Enter Number: ')
##if is_tech(num):
##    print(f'{num} is Tech Number!')
##else:
##    print(f'Not!')



# Python Program to Create a Dictionary with Key as First Character and Value
# as Words Starting with that Character

##string = '''hello this is btechgeeks online programming platform to read the
##  coding articles specially python language'''
##
##result = {}
##for word in string.split():
##    if (word[0] not in result.keys()):
##        result[word[0]] = []
##        result[word[0]].append(word)
##    else:
##        if word not in result[word[0]]:
##            result[word[0]].append(word)
##for letter,matched_words in result.items():
##    print(f'{letter} ::: {matched_words}')



# Python count word frequency dictionary – Python Program to Count the Frequency
# of Words Appearing in a String Using a Dictionary

##string ='''hello this is hello BTechGeeks BTechGeeks BTechGeeks this python
##            programming python language'''
##
##result = {}
##for word in string.split():
##    result[word] = result.get(word,0) + 1
##print(result)


# Python Program to Accept a Hyphen Separated Sequence of Words
# as Input and Print the Words in a Hyphen-Separated Sequence
# after Sorting them Alphabetically.

##string = 'hello-this-is-btechgeeks'
##words = string.split('-')
##words.sort()
##sorted_string = '-'.join(words)
##print('The string before modification: ', string)
##print('The string after modification: ',sorted_string)


# Python Program to Read a List of Words and Return the Length of
# the Longest Word

##string = 'Hello this is BTechGeeks  online platform'
##words = string.split()
##max_length = 0
##longest_word = None
##for word in words:
##    if len(word) > max_length:
##            longest_word = word
##            max_length = len(word)
##print(longest_word,'is the longest word with length',max_length)


# Python Program to Group Words with the Same Set of Characters
##words = ['ehlo', 'this', 'is', 'olhe', 'helo', 'si', 'btechgeeks']
##result = {}
##for word in words:
##    sorted_word = ''.join(sorted(word))
##    if sorted_word not in result:
##        result[sorted_word] = []
##    result[sorted_word].append(word)
##word_list = [list for list in result.values()]
##print(word_list)



# Python Program to Calculate the Number of Words and the Number of Characters
# Present in a String

##string ='Hello this is btechgeeks'
##words = string.split()
##number_of_spaces = len(words) - 1
##word_count = 0
##character_count = number_of_spaces
##for word in words:
##    character_count += len(word)
##    word_count +=  1
##print(f'Total characters present in given string {string} =',character_count)
##print(f'Total words present in given string {string} =',word_count)



# Python Program to Count Number of Lowercase Characters in a String
##string = 'Hello this is BTechGeeks'
##total = 0
##for char in filter(lambda x: x.islower(),list(string)):
##    total += 1
##print('The total lowercase characters are: ',total)


# Anagram program in python – Python Program to Check If Two Strings are
# Anagram
##string1 = "skyis"
##string2= "ssyki"
##if sorted(string1) == sorted(string2):
##    print('anagrams!')
##else:
##    print('Not!')

# Python Program to Check if a String is a Pangram or Not
# If a sentence or string contains all 26 letters of the English alphabet at
# least once, it is considered to be a pangram.

##string ="Helloabcdfegjilknmporqstvuxwzy"
##list = []
##for char in string:
##    if (ord(char) >= 65 and ord(char) <= 90) or (ord(char) >= 97 and ord(char) <=122):
##        if char.lower() not in list:
##            list.append(char.lower())
##if len(list) == 26:
##    print('Pangram!')
##else:
##    print('Not!')



# Python Program to Check Whether the given Number is Strong Number or Not
# A Strong number is a special number in which the total of all digit factorials
# equals the number itself.
# Ex: 145 the sum of factorial of digits = 1 ! + 4 ! + 5 ! = 1 + 24 + 120

##def digits_finder(num): #123
##    digits = []
##    while num >0:
##        digits.append(num%10)
##        num //= 10
##    return digits
##
##def factorial_finder(num):
##    if num == 1:
##        return 1
##    return num * factorial_finder(num - 1)
##
##def is_strong(num):
##    temp = num
##    factorial_sum = 0
##    digits = digits_finder(num)
##    for digit in digits:
##        factorial_sum += factorial_finder(digit)
##    return True if factorial_sum == temp else False
##num = int(input('Enter Number: '))
##if is_strong(num):
##    print('Strong Number!')
##else:
##    print('Not!')


# Write a code to find whether numbers are amicable or not.
# Two distinct positive integers are considered amicable numbers if each number
# is the sum of the proper divisors of the other, excluding that number. In simpler terms, for a pair
# of numbers (A,B):

##The sum of the proper divisors of A equals B.
##The sum of the proper divisors of B equals A.

##def divisor_finder(num):
##    proper_divisors = []
##    for i in range(1,num):
##        if num%i==0:
##            proper_divisors.append(i)
##    return proper_divisors
##
##def is_amicable(num1,num2):
##    if num1 == sum(divisor_finder(num2)) and num2 == sum(divisor_finder(num1)):
##        return True
##    else:
##        return False
##num1 = int(input('Enter Number 1: '))
##num2 = int(input('Enter Number 2: '))
##if is_amicable(num1,num2):
##    print('Numbers Are Amicable!')
##else:
##    print('Not!')



# Write a code to find Fibonacci Series using Recursion
# Write a code to Sort the element of the array
# bubble sort
# lcm















