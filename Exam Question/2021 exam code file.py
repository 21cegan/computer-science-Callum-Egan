# Question 16(a)
# Examination Number:

# function definition used in part (v)
def is_anagram(w1, w2):
    if sorted(w1.upper()) == sorted(w2.upper()):
        return True
    else:
        return False

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
# test whether the sorted strings are the same as each other
# if the sorted strings are the same then they must be anagrams
if (sorted(word1.upper()) == sorted(word2.upper())):
    print(f"{word1} is an anagram of {word2}")
else:
    print(f"{word1} is not an anagram of {word2}")
    
if is_anagram(word1,word2):
    print(f"{word1} is an anagram of {word2}")
else:
    print(f"{word1} is not an anagram of {word2}")
    
phrase = input("Enter a phrase: ")

phraseNoSpace = phrase.replace(" ","")

if (sorted(phraseNoSpace.upper()) == sorted(word1.upper())):
    print(f"{word1} is an anagram of {phrase}")
else:
    print(f"{word1} is not an anagram of {phrase}")

if (sorted(phraseNoSpace.upper()) == sorted(word2.upper())):
    print(f"{word2} is an anagram of {phrase}")
else:
    print(f"{word2} is not an anagram of {phrase}")