from string import printable
from typing import List


data = input("enter:")
type(data)
print(data)
numbers1 = [9, 2, 4, 5]
numbers2 = [123, 3, 231, 2]
numbers3 = [55, 66, 88, 7]
numbers4 = [897, 98, 89]
print(numbers1[2])
numberssorted = sorted(numbers1)
print(numberssorted)
# append liste olarak ekler, extend listeden cıkararak ekler
numbers3.append(numbers4)
numbersAppended = numbers3
print(numbersAppended)

numbers1.extend(numbers2)
newNumbers = numbers1
print(newNumbers)

sentence = "MANİSA Celal Bayar University"
print(sentence.lower().count('a'), ' :adet a bulundu')
print(sentence.count('a'), ': adet a bulundu')

example = "    --------**********  amksdnkasndnas ************ --------    "
ex1 = example.strip()
ex2 = ex1.strip("-")
print(ex1, "\n", ex2)


names = ["berke", "bicak"]
nums = [2, 3, 3, 4]
dictionary = zip(names, nums)
print(type(dictionary))
dictionary2 = dict(dictionary)
print(dictionary2)
print(dictionary2.items())
print(dictionary2.keys())
print(dictionary2.values())

# -----------------------------
nestedList = [[1, 2, 3], [6, 8, 9]]
i = int(input("find number in list"))
var = 0
for s in nestedList:
    for i in s:
        if (i == s):
            var = 1
            print("var")
        else:
            var = 0
            print("yok")


lst1 = [1, 2, 3, 4, 5]
newlst = map(lambda x: x+2, lst1)
aa = list(newlst)
print(aa)
