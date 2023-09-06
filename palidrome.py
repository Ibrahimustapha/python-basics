#Palindrome are words that when read in forward and backward they are the same
#e.g  mum, dad, pop, deed, level, madam 
word = input('Enter your word: ')
word = word.replace(' ','')
if word == word[::-1]:
    print(word, 'is palindrome')
else:
    print(word, 'is not palindrome')
''