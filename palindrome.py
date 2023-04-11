#iterativa
def palindromeiter(word):
    word = word.lower()
    wordrev = word[::-1]
    if word == wordrev:
        return True


#recursiva
def palindromerecu(word):
    word = word.lower()
    if len(word)<=1:
        return True
    if word[0] == word[-1]:
        return palindromerecu(word[1:-1])
