
word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")
def remove(lst, value):

    for i in range(len(lst)):
        if lst[i] == value:

            del lst[i]
            return

anagram = False
if len(word1) != len(word2):
    anagram = False
else:

    letters1 = []
    letters2 = []

    for char in word1:
        letters1.append(char)

    for char in word2:
        letters2.append(char)


    for char in letters1:
        if char in letters2:

            letters2.remove(char)
        else:
            anagram = False
            break
    else:

        anagram = True


print("Анаграммы:", anagram)
