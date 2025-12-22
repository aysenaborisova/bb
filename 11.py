#1
"""
n = int(input())
def factorial(n):
    if n >= 1:
        return n * factorial(n-1)
    return 1
print(factorial(n))
    
"""
#2
"""
string = input()
def remowe_vowels(string):
    vowels = "aeyuio"
    if string == "":
        return ""
    s = string[0]
    if s in vowels:
        return remowe_vowels(string[1:])
    else:
        return s + remowe_vowels(string[1:])
print(remowe_vowels(string))
   
"""
#3
def pascal(n)
