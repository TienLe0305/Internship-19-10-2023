string = input()

print("Text has", len(string.split()), "words.")

if string.split()[:] == string.split()[::-1]:
    print("Word Palindrome")
else:
    print("NOT Word Palindrome")
