a = input("Enter a letter: ")

def vowel(letter):
    vowels = "aeiou AEIOU"
    return letter in vowels

if vowel(a):
    print("a is a vowel.")
else:
    print("a is not a vowel.")
    