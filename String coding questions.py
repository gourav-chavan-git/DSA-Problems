#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      91932
#
# Created:     11-12-2024
# Copyright:   (c) 91932 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Write a program to check palindrome string

# Using slice operator:
##def palindrome(str):
##    reversed_str = str[::-1]
##    if str == reversed_str:
##        return True
##    else:
##        return False
##str = input('Enter string: ')
##if palindrome(str):
##    print('String is palindrome!')
##else:
##    print('String is not a palindrome!')


# Wap to reverse a given string

#Write a program to REVERSE content of the given string by using slicing operatoref
##def reverse(str):
##    reverse_str = str[::-1]
##    return reverse_str
##str = input('Enter your string: ')
##s = reverse(str)
##print(f'The reverse of {str} is {s}')

#Write a program to REVERSE content of the given string by using reversed() function

##def reverse(str):
##    r = ''.join(reversed(str))
##    return r
##str = input('Enter your string: ')
##s = reverse(str)
##print(f'The reverse of {str} is {s}')


# Write a program to REVERSE content of the given string by using while loop
##def reverse(str): # 2 1 0
##    r_str = ''
##    i = len(str) - 1
##    while i>=0:
##        r_str += str[i]
##        i -= 1
##    return r_str
##str = input('Enter your string: ')
##s = reverse(str)
##print(f'The reverse of {str} is {s}'



# Write a program to REVERSE order of words present in the given string
##def reverse(str): # python is language
##    list = str.split()
##    r_list = list[::-1]
##    return ' '.join(r_list)
##str = input('Enter str: ')
##r_o_str = reverse(str)
##print(f'The reversed order string is:\n{r_o_str}')


# Wap to REVERSE internal content of each word
# INPUT: 'gourav is a good boy'
# OUTPUT: 'varuog si a doog yob'

##def reverse(str):
##    w_list = str.split()
##    r_c_list = []
##    for word in w_list:
##        r_c_list.append(word[::-1])
##    r_str = ' '.join(r_c_list)
##    return r_str
##str = input('Enter your string: ')
##s = reverse(str)
##print(f'The reversed ordered content string is:\n{s}')


# Wap to REVERSE internal content of every 2nd word present in given string
# INPUT: 'python is a fun'
# OUTPUT: 'python si a nuf'
##def reverse(str):
##    w_list = str.split()
##    s_r_w_list = []
##    for i in range(len(w_list)):
##        if i%2!=0:
##            s_r_w_list.append(w_list[i][::-1])
##        else:
##            s_r_w_list.append(w_list[i])
##    return ' '.join(s_r_w_list)
##str = input('Enter your string: ')
##s = reverse(str)
##print(f'The string whos second word reversed is\n{s}')


# Write a program to print characters present at even and odd index values.

##def even_odd(str):
##    e_i_char_list = []
##    o_i_char_list = []
##    i=0
##    while i<len(str):
##        e_i_char_list.append(str[i])
##        i+=2
##    i = 1
##    while i <len(str):
##        o_i_char_list.append(str[i])
##        i +=2
##    return e_i_char_list,o_i_char_list
##str = input('Enter your string: ')
##e_list,o_list = even_odd(str)
##print('The characters present at even index number are:')
##for char in e_list:
##    print(char)
##print('The characters present at odd index number are:')
##for char in o_list:
##    print(char)

# Another method to do this.... (using slicing operator)
##def even_odd(str):
##    e_i_char_list = str[0::2]
##    o_i_char_list = str[1::2]
##    return e_i_char_list,o_i_char_list
##str = input('Enter your string: ')
##e_list,o_list = even_odd(str)
##print('The characters present at even index number are:')
##for char in e_list:
##    print(char,end=' ')
##print('\nThe characters present at odd index number are:')
##for char in o_list:
##    print(char,end=' ')


# Write a program to print the characters present at even index and odd index
# seperately for the given string

##def even_odd(str):
##    e_i_chars = str[0::2]
##    o_i_chars = str[1::2]
##    return e_i_chars, o_i_chars
##str = input('Enter your string: ')
##e_i_chars,o_i_chars = even_odd(str)
##print(f'Characters present at Even Index: {e_i_chars}')
##print(f'Characters present at Odd Index: {o_i_chars}')


# Wap to sort chracters of thee string, first symbols followed by digits in sorted order.

##def alphanumeric(str):
##    alpha = []
##    digi = []
##    for char in str:
##        if char.isalpha():
##            alpha.append(char)
##        else:
##            digi.append(char)
##    s_list = sorted(alpha) + sorted(digi)
##    r_str = ''.join(s_list)
##    return r_str
##str = input('Enter your string: ')
##s_str = alphanumeric(str)
##print(f'The sorted string is: {s_str}')


# Can you Write a program for the following requirement?
# input: 'a4b3c2'
# output: 'aaaabbbcc'
##def func(str):
##    r_str = ''
##    alpha = []
##    digi = []
##    for char in str:
##        if char.isalpha():
##            alpha.append(char)
##        else:
##            digi.append(char)
##    for alpha,digi in zip(alpha,digi):
##        r_str = r_str + alpha*int(digi)
##    return r_str
##str='a4b3c2'
##result = func(str)
##print(f'The input: {str}')
##print(f'The output: {result}')

# Another way to do this... but input should be only in this form not like '1a2b3c', it will fail
##str = 'a4b3c2'
##output = ''
##for char in str:
##    if  char.isalpha():
##        x = char
##    else:
##        output = output + x*int(char)
##print(f'Input: {str}')
##print(f'Output: {output}')


# Can you write a program for the following requirement?
# Input: 'c2a4b3
# Output: 'aaaabbbcc'
##def func(str):
##    r_str = ''
##    alpha = []
##    digi = []
##    for char in str:
##        if char.isalpha():
##            alpha.append(char)
##        else:
##            digi.append(char)
##    for alpha,digi in sorted(zip(alpha,digi)):
##        r_str = r_str + alpha*int(digi) #digi is still string type so type casted to int type
##    return r_str
##str=''c2a4b3'
##result = func(str)
##print(f'The input: {str}')
##print(f'The output: {result}')


# Anothe way to do this...

##str = 'c2a4b3'
##output = ''
##for char in str:
##    if  char.isalpha():
##        x = char
##    else:
##        output = output + x*int(char)
##r_str = ''.join(sorted(output))
##print(f'Input: {str}')
##print(f'Output: {r_str}')



#Write a program for the following requirement??
## input: aaaabbbccd
## output: 4a3b2c1d

##s = 'aaaabbbccd' #10
##required_s = ''
##previous = s[0]
##c = 1
##i = 1
##while i < len(s):
##    if s[i] == previous:
##        c += 1
##    else:
##        required_s += str(c) + previous
##        previous = s[i]
##        c = 1
##    if i == len(s) - 1:
##        required_s += str(c) + previous
##    i += 1
##print(required_s)


# Write a program for the following requirement?
# Input: a4k3b2
# Output: aeknbd
##s = 'a4k3b2'
##r_s = ''
##for i in range(0,len(s),2): # 0,2,4
##    r_s += s[i] + chr(ord(s[i]) + int(s[i+1]))
##print(r_s)



# Write a program to remove duplicate characters from the given input string?
## INPUT: 'AZZBCDABBCDABBBCCCCDDEEEF'
## OUTPUT: 'AZBCDA'

##s = 'AZZBCDABBCDABBBCCCCDDEEEF'
##r_s = ''
##for char in s:
##    if char not in r_s:
##        r_s += char
##print(r_s)



# Write a program to find the number of occurences of each character present in the given  strin?

##s = 'ABBACBA'
##letters = sorted(s)  # ['A', 'A', 'A', 'B', 'B', 'B', 'C']
##mapping = {}
##for letter in letters:
##    mapping[letter] = mapping.get(letter,0) + 1
##for letter,count in mapping.items():
##    print(f'{letter} has occured {count} times!')



#Write a program for the following requirement??
## input: ABAABBCA
## output: A4B3C1

##s = 'ABAABBCA' #10
##letters = sorted(s)
##required_s = ''
##previous = letters[0]
##c = 1
##i = 1
##while i < len(letters):
##    if letters[i] == previous:
##        c += 1
##    else:
##        required_s +=  previous + str(c)
##        previous = letters[i]
##        c = 1
##    if i == len(letters) - 1:
##        required_s += previous + str(c)
##    i += 1
##print(required_s)

# Another way to do this...
## output: A4B3C2
##s = 'BBCABAACA'
##r_s = ''
##d = {}
##for char in sorted(s):
##    d[char] = d.get(char,0) + 1
##for char, count in d.items():
##    r_s += char + str(count)
##print(r_s)  # 4A3B2C


# Write a program to find the number of occurences of each vowel present in the given string?
## INPUT: mississippi
## OUTPUT: i has occurred 4 times!

##s = input('Enter String to search for vowels: ')
##vowels = ['a','e','i','o','u','A','E','I','O','U']
##d = {}
##for char in s:
##    if char in vowels:
##        d[char] = d.get(char,0) + 1
##for char,count in d.items():
##    print(f'{char} has occurred {count} times!')


# Program to check whether the given two strings are anagrams or not?
##string1 = input('Enter string1: ')
##string2 = input('Enter string2: ')
##if sorted(string1) == sorted(string2):
##    print('Anagrams!')
##else:
##    print('Not!')



# Write a program to check whether the given string is palindrome or not?
# Original string and its reverse should be equal. e.g.-> level,eye,malayalam,mom etc.
##string = input('Enter string1: ')
##if string == string[::-1]:
##    print('Palindrome!')
##else:
##    print('Not!')


# Write program for the following requirement
##s1 = 'abcdefg'
##s2 = 'xyz'
##s3= '12345'
##result = ''
##i = j = k = 0
##while i <len(s1) or j < len(s2) or k < len(s3):
##    if i < len(s1):
##        result += s1[i]
##        i += 1
##    if j < len(s2):
##        result += s2[j]
##        j += 1
##    if k < len(s3):
##        result += s3[k]
##        k += 1
##print(result)


# Write a program to reverse given string.
# Using slicing operator
##string = input('Enter your string: ')
##reverse = string[::-1]
##print(f'The reverse of given string {string} is: {reverse}')

#Another method to do this...
##string = input('Enter your string: ') # python
##reverse = ''
##for i in range(len(string)):
##    reverse = string[i] + reverse #nohtyp
##print(f'The reverse of given string {string} is: {reverse}')

# Another way to do this...
##string = input('Enter your string: ')
##reversed_letters = reversed(string)
##reversed_string = ''.join(reversed_letters)
##print(f'The reverse of given string {string} is: {reversed_string}')

# Another way to do this...
##string = input('Enter your string: ')
##reverse = ''
##i = 0
##while i < len(string):
##    reverse = string[i] + reverse
##    i += 1
##print(f'The reverse of given string {string} is: {reverse}')


# Write a program to reverse order of words
##string = input('Enter string: ')
##reversed_words = string.split()[::-1]
##result = ' '.join(reversed_words)
##print(f' The reverse ordered string is: {result}')


# Write a program to reverse the interval content of each word.
##string = input('Enter String: ') # learning python is easy
##r_words = []
##for word in string.split(): # [learning, python, is, easy]
##    r_words.append(word[::-1])
##r_string = ' '.join(r_words)
##print(f'The string after reversing the internal content of each word: {r_string}')



# Write a program to REVERSE internal content of every second word present in the given string
## INPUT: one two three four five six
## OUTPUT: one owt three ruof five xis
##string = input('Enter String: ') # learning python is easy
##r_words = []
##list_of_words = string.split()
##i = 0
##while i < len(list_of_words):
##    if i%2!=0:
##        r_words.append(list_of_words[i][::-1])
##    else:
##        r_words.append(list_of_words[i])
##    i += 1
##r_string = ' '.join(r_words)
##print(f'The string after reversing the internal content of each word: {r_string}')

# Print characters present at even & odd index seperately for given string.
##string = input('Enter String: ')
##even_idx_chars = []
##odd_idx_chars = []
##i = 0
##while i <len(string):
##    if i%2==0:
##        even_idx_chars.append(string[i])
##    else:
##        odd_idx_chars.append(string[i])
##    i += 1
##print(f'Chars present at even index positions are: {even_idx_chars}')
##print(f'Chars present at odd index positions are: {odd_idx_chars}')

# Another way to do this...
##string = input('Enter String: ')
##even_idx_chars = [char for char in string[0::2]]
##odd_idx_chars = [char for char in string[1::2]]
##print(f'Even Index: {even_idx_chars}')
##print(f'Odd Index: {odd_idx_chars}')


# Assume input string contains only aplhabet symbols and digits. Write
# a program to sort characters of the string, first alphabet symbols
# followed by digits?

##String = 'B4A1D3'
##digits = []
##alphabets = []
##for char in String:
##    if char.isalpha():
##        alphabets.append(char)
##    else:
##        digits.append(char)
##result = ''.join(sorted(alphabets) + sorted(digits))
##print(result)


# Write a program for the requirement,
# input 'a4b3c2' and expected output 'aaaabbbcc'

##input = 'a4b3c2'
##output = ''
##for alpha,count in dict(zip(input[::2],input[1::2])).items():
##    output += alpha*int(count)
##print(f'Required Output is: {output}')


# Anothe way to do this...
##input = 'a4b3c2'
##output = ''
##for char in input:
##    if char.isalpha():
##        x = char
##    else:
##        output += x*int(char)
##print(f'Required Output is: {output}')


# Write a code the following requirement,
## input = 'a4b3c2'
## output = 'aaaabbbcc'
##input = 'a4b3c2'
##output = ''
##for char in input:
##    if char.isalpha():
##        x = char
##    else:
##        output += x*int(char)
##print(f'Required Output is: {output}')



# Write a code the following requirement,
## input = 'a4c2b3'
## output = 'aaaabbbcc'
##input = 'a4c6b3'
##output = ''
##for alpha,count in sorted(dict(zip(input[::2],input[1::2])).items()):
##    output += alpha*int(count)
##print(f'Required Output is: {output}')


# Write a program for the following requirement,
## INPUT: aaaabbbccz
## OUTPUT: 4a3b2c1z

##input = 'aaaabbbccz'
##r_string = ''
##previous = input[0]
##i = 1
##c = 1
##while i < len(input):
##    if input[i] == previous:
##        c += 1
##    else:
##        r_string = r_string + str(c) + previous
##        previous = input[i]
##        c = 1
##    if i == len(input) - 1:
##        r_string += str(c) + previous
##    i += 1
##print(r_string)


# Write a program to remove duplicate characters from the given input string.

##input = 'AKSLIO#OINKCCVV5APOODFUEEOA5DDBSCCAD@FUUA&SJJASVB#ASVJS'
##original = []
##for char in input:
##    if char not in original:
##        original.append(char)
##result = ''.join(original)
##print(result)

# Another way to do this...
##result = ''.join(set(input))
##print(result)


# Find no. of occurrences of each character present in given string with count()
##string = 'ullallareullallare'
##tem = []
##for char in string:
##    if char not in tem:
##        count = string.count(char)
##        tem.append(char)
##        print(f'{char} has occurred {count} times!')

# Another way to do this... (Using .get() method)
##d = {}
##for char in string:
##    d[char] = d.get(char,0) + 1
##for char,count in d.items():
##    print(f'{char} has occurred {count} times!')


# Program for the requirement,
# INPUT: ABAABBCA
# OUTPUT: 4A3B1C

##input = 'ABAABBCA'
##output = ''
##d = {}
##for char in input:
##    d[char] = d.get(char,0) + 1
##for char,count in d.items():
##    output += str(count)+char
##print('Output is:',output)

# Another way to do this... This time we want in sorted order & character should come first

##input = 'BACCAABDBCA'
##output = ''
##d = {}
##for char in input:
##    d[char] = d.get(char,0) + 1
##for char,count in sorted(d.items()):
##    output += char + str(count)
##print('Output is:',output)


# Write a program to find the number of occurrences of each vowel present in the given string.

##string = 'bumchikibumchikibumbumbolle'
##vowels = ['a','e','i','o','u','A','E','I','O','U']
##for char in set(string):
##    if char in vowels:
##        print(char,'has occurred',string.count(char),'times!')

# Another way to do this...
##string = 'bumchikibumchikibumbumbolle'
##d = {}
##vowels = ['a','e','i','o','u','A','E','I','O','U']
##for char in string:
##    if char in vowels:
##        d[char] = d.get(char,0) + 1
##for char,count in sorted(d.items()):
##    print(char,'has occurred',count,'times!')


# Write a program to check given two strings are anagrams or not.
##string1 = input('Enter String1: ')
##string2 = input('Enter String2: ')
##if sorted(string1) == sorted(string2):
##    print('Anagrams!')
##else:
##    print('Not!')



# Write a program to check whether the given string is palindrome or not.
##string = input('Enter String: ')
##if string == string[::-1]:
##    print('Palindrome!')
##else:
##    print('Not!')


# Write the program for the following requirement.
# INPUT: s1 = 'abcdefg'
#        s2 = 'xyz'
#        s3 = '12345'
# OUTPUT: ax1,by2,cz3,d4,e5,d,g

##s1 = 'abcdefg'
##s2 = 'xyz'
##s3 = '12345'
##output = ''
##i = 0
##while i < len(s1) or i < len(s2) or i < len(s3):
##    if i < len(s1):
##        output += s1[i]
##    if i < len(s2):
##        output += s2[i]
##    if i < len(s3):
##        output += s3[i]
##    print(output,end=',')
##    output = ''
##    i += 1


# Write a program to reverse given string
##string = 'rahul'
##reverse_str = string[::-1]
##print(reverse_str)

# Another way to do this..
# reverse doesn't apply on string type.
##string = 'rahul'
##reverse_str = ''.join(reversed(string))
##print(reverse_str)

# Anothe way to do this...
##string = 'rahul' #5
##output = ''
##i = len(string) - 1
##while i >= 0:
##    output += string[i]
##    i -= 1
##print('Reverse string is:',output)



# Write a program to REVERSE the order of words present in the given string.
##string = 'python is fun'
### output = 'fun is python
##output = ' '.join(string.split()[::-1])
##print(output)


# Write a program to REVERSE the order of words present in the given string.
##string = 'python is fun'
##output = ' '.join([word[::-1] for word in string.split()])
##print(output)


#












































