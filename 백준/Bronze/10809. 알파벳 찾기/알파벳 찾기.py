import string
lst = [i for i in string.ascii_lowercase]
word = input()
for x in lst:
    print(word.find(x), end=' ')