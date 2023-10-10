#At least 1 letter between [a-z]
def checkLetterLowerCase(s):
    flag=[False,"At least 1 letter between [a-z]"]
    for x in s:
        if x.isalpha() and x.islower():
            flag[0]=True
            break
    return flag
#At least 1 letter between [A-Z].
def checkLetterUpperCase(s):
    flag=[False,"At least 1 letter between [A-Z]"]
    for x in s:
        if x.isalpha() and x.isupper():
            flag[0]=True
            break
    return flag
#At least 1 number between [0-9].
def checkNumbers(s):
    flag=[False,"At least 1 number between [0-9]"]
    for x in s:
        if x.isnumeric():
            flag[0]=True
            break
    return flag
#At least 1 character from [$#@].
def checkSpecialCharacter(s):
    a="$#@"
    flag=[False,"At least 1 character from [$#@]"]
    for x in s:
        if x in a:
            flag[0]=True
            break
    return flag
#Minimum length 6 characters and Maximum length 16 characters.
def checkSize(s):
    flag=[False,"Minimum length 6 characters and Maximum length 16 characters"]
    if  6 <= len(s) <= 16:
        flag[0]=True
    return flag

# Check validity of Password
s=input("Enter the password")
if all([checkSize(s)[0],checkSpecialCharacter(s)[0],checkNumbers(s)[0],checkLetterUpperCase(s)[0],checkLetterLowerCase(s)[0]]):
        print("Password is Valid")
else:
    print(''' Invalid Password
    Password should have:''')
    if not checkSize(s)[0]:
        print("* ",checkSize(s)[1])
    if not checkSpecialCharacter(s)[0]:
        print("* ",checkSpecialCharacter(s)[1])
    if not checkNumbers(s)[0]:
        print("* ",checkNumbers(s)[1])
    if not checkLetterUpperCase(s)[0]:
        print("* ",checkLetterUpperCase(s)[1])
    if not checkLetterLowerCase(s)[0]:
        print("* ", checkLetterLowerCase(s)[1])
