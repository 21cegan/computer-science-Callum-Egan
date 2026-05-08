#Question 16(b)
#Name and School: Callum Egan

vowels = ["a","e","i","o","u"]
string = "e This program helps a student keep track of their Book Club reading list by asking how many books they've finished reading"

wordCount = len(string.split())
vowelCount = 0

for x in string:
    if x in vowels:
        vowelCount += 1

print("The sentence \"" + string+"\" contains:")
print(wordCount, "words")
print(vowelCount, "vowels" 'df')