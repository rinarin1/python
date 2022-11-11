word = input()

z = len(word)
a = 0
b = z - 1
def p1(a, b, word):
    if word[a] == word[b]:
        if b - a != 1:
            p1(a + 1, b - 1, word) 
        return 1
    return 0
def p2(a, b, word):
    if word[a] == word[b]:
        if b - a != 0:
            p2(a + 1, b - 1, word)
        return 1
    return 0
if z % 2 == 0:
    if p1(a, b, word)==1:
        print("True")
    else:
        print("False")
else:
    if p2(a, b, word)==1:
        print("True")
    else:
        print("False")