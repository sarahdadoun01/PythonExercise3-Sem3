"""""""""""""""""""""""""""""""""

        Assignment # 3
         Sarah Dadoun

"""""""""""""""""""""""""""""""""


###     Question 1
#       Arrange String characters such that lowercase letters should come first
'''
myString = input("Input a string : ")
myList = [None] * len(myString)

j = len(myList)-1
k = 0
for i in range(0, len(myString)):
    if myString[i] == myString[i].upper():
        myList[j] = myString[i]
        j -= 1
    else:
        myList[k] = myString[i]
        k+=1

def listToString(s):
    aStr = ""
    for i in s:
        aStr += i
    return aStr


print("\n",listToString(myList),"\n")
'''

###     Question 2
#       Given an input string Count all lower case, upper case, digits, and special symbols
'''
myStr = input("Type something : ")
charTypeOcc = {
    "Lower Case":0,
    "Upper Case":0,
    "Digits":0,
    "Special Symbols":0
}

myStr = myStr.replace(" ", "")
# FIRST OPTION
for i in range(0, len(myStr)):
    if myStr[i].isalpha():
        if myStr[i] == myStr[i].lower():
            charTypeOcc["Lower Case"] += 1
        if myStr[i] == myStr[i].upper():
            charTypeOcc["Upper Case"] += 1
    if myStr[i].isnumeric():
        charTypeOcc["Digits"] += 1
    if not myStr[i].isalpha() and not myStr[i].isnumeric():
        charTypeOcc["Special Symbols"] += 1

# SECOND OPTION
for i in range(0, len(myStr)):
    if myStr[i].isalpha():
        if myStr[i] == myStr[i].lower():
            charTypeOcc["Lower Case"] += 1
        if myStr[i] == myStr[i].upper():
            charTypeOcc["Upper Case"] += 1
    if myStr[i].isnumeric():
        charTypeOcc["Digits"] += 1

charTypeOcc["Special Symbols"] = len(myStr) - (charTypeOcc["Lower Case"] + charTypeOcc["Upper Case"] + charTypeOcc["Digits"])

#print(charTypeOcc)
print("\n")
for key, value in charTypeOcc.items():
    print(f"{key} : {value}\n")
print("\n")
'''
# isalpha() -> returns true if all chars are letters
# isnumeric() -> returns true if all chars are numbers

# remove white spaces using replace()
# if letter -> check if upper or lower case -> add 1 to lower/upper
# if number -> add 1 to digits
# if not letter or not number -> add 1 to special char
# OR
# add lower, uppper and digits, subrtract total from length of string without spaces.


###     Question 3
#       String characters balance Test
'''
sA = "yn"
sB = "ynf"
sC = "Python"

sA = set(sA)
sB = set(sB)
sC = set(sC)

print(f"\n A = {sA}", f"\n B = {sB}", f"\n C = {sC}")

print(f"\nIs A subset of C ? {sA.issubset(sC)}")
print(f"Is B subset of C ? {sB.issubset(sC)}\n")
'''


###     Question 4
#       Given an input string, count occurrences of all characters within a string
'''
myStr = input("Type a word : ")
letters = {}

for i in myStr:
    letters[i] = myStr.count(i)

print(letters)
'''


###     Question 5
#       Given a list iterate it and count the occurrence of each element 
#       and create a dictionary to show the count of each element
'''
aList = [10, 20, 30, 10, 20, 40, 50]
aDict = {10: 2, 
         20: 2, 
         30: 1, 
         40: 1, 
         50: 1}

for i in aList:
    aDict[i] = aList.count(i)
    
print(f"\nDictionary : {aDict}")
print(f"List       : {aList}\n")
'''



###     Question 6
#       Write a Python program to reverse a given string
'''
myStr = input("Type a word : ")
print(myStr[::-1])
'''



###     Question 7
#       Write a Python program to construct the following pattern, using a nested for loop.
#       * 
#       * * 
#       * * * 
#       * * * * 
#       * * * * * 
#       * * * * 
#       * * * 
#       * * 
#       *

star = "* " 
'''
'''
mL = [0,1,2,3,4,5,4,3,2,1,0]

for j in mL:
    print(star * mL[j])

del(mL)

# OR 
"""
for j in range(1,6,1):
    print(star * j)
for j in range(4,-1,-1):
    print(star * j)
"""
# OR

for i in range(1,7):
    for j in range(1,i):
        print(f"{star}", end=" ")
    print("\n")
    
for i in range(1,5):   
    for j in range(5,i,-1):
        #print(f"\n\nSecond Loop\ni = {i}, j = {j}")
        print(f"{star}", end=" ")
    print("\n")




###     Question 8
#       Write a Python program to display astrological sign for given date of birth.

# Capricorn : dec 22 - jan 19
# Aquarius  : jan 20 - feb 18
# Pisces    : feb 19 - march 20
# Aries     : mar 21 - april 19
# Taurus    : april 20 - may 20
# Gemini    : may 21 - jun 20
# Cancer    : jun 21 - july 22
# Leo       : july 23 - aug 22
# Virgo     : aug 23 - sep 22
# Libra     : sep 23 - oct 22
# Scorpio   : oct 23 - nov 21
# Sagittarus: nov 22 - dec 21

print("\nPlease Enter Date Of Birth\n\n")
m = (input("Month (ex: may): ").lower()).replace(" ", "")
d = int(input("Day : "))

def getAstroSign(m, d):
    aS = ""
    if m == "jan":
        if d < 20:
            aS = "Capricorn"
        else:
            aS = "Aquarius"
    elif m == "feb":
        if d < 19:
            aS = "Aquarius"
        else:
            aS = "Pisces"
    elif m == "march":
        if d < 21:
            aS = "Pisces"
        else:
            aS = "Aries"
    elif m == "april":
        if d < 20:
            aS = "Aries"
        else:
            aS = "Taurus"
    elif m == "may":
        if d < 21:
            aS = "Taurus"
        else:
            aS = "Gemini"
    elif m == "june":
        if d < 21:
            aS = "Gemini"
        else:
            aS = "Cancer"
    elif m == "july":
        if d < 23:
            aS = "Cancer"
        else:
            aS = "Leo"
    elif m == "august":
        if d < 23:
            aS = "Leo"
        else:
            aS = "Virgo"
    elif m == "september":
        if d < 23:
            aS = "Virgo"
        else:
            aS = "Libra"
    elif m == "october":
        if d < 23:
            aS = "Libra"
        else:
            aS = "Scorpio"
    elif m == "november":
        if d < 22:
            aS = "Scorpio"
        else:
            aS = "Sagittarius"
    else:
        if d < 22:
            aS = "Sagittarius"
        else:
            aS = "Capricorn"
    return aS

print(f"\nYour astrological sign is : {getAstroSign(m, d)}\n")
'''