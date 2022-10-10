# regex and pandas libraries
import re
import pandas as pd

txt = "on the horizon"
x = re.findall("on", txt)
print(x)
print(len(x))
######################################
x = re.findall("[arn]", txt)
print(x)

if x:
    print("There is match")
else:
    print("no match")

###################################

txt = "python tutorial"
x = re.search("python", txt)
print("The python word located in position :", x.start())

txt = "Python regular expression"
x = re.match("Python regular expression", txt)
print(x)

######################################

txt = "The python word located in the position"
x = re.split("\s", txt)  # \s bosluga gore ayırır.
print(x)
print(x.count('the'), " found")

#########################################

txt = "The python word located in the position"
x = re.split("\s", txt.lower())
print(x)
print(x.count('the'))


txt = "The Python regular expression is a sequence of characters, that defines a search Python "
x = re.findall("Python$", txt)  # Python la bitiyor mu txt kontrol.
print(x)
if x:
    print("Sentence ends with Python")
else:
    print("no match")


txt = "The Python regular expression is a sequence of characters, that defines a search Python"
x = re.findall("Python|C#", txt)
print(x)
print(x.count("Python"))

txt = "This is Python example"

# * dan onceki harf oladabilir olmayadabilir
x = re.findall("thi*", txt.lower())
x2 = re.findall("thi+", txt.lower())  # + dan onceki harf (i) bir kere olsun
print(x)
print(x2)

################################
txt = "This is Python example"
x = re.findall("[a-k]", txt)
print(x)


txt = "This is Python 100 example"
x = re.findall("\d", txt)
print(x)

txt = "This is Python example"
x = re.findall("he..o", txt)
print(x)


txt = "This is Python ill"
x = re.findall("il{2}", txt)
print(x)
if x:
    print("matches")
else:
    print("no match")


txt = "This is Python example"
x = re.findall("[^arn]", txt)
print(x)
if x:
    print("matches")
else:
    print("no match")

txt = "This is Python example 234"
x = re.findall("[0123]", txt)
print(x)


txt = "This is Python example 28416 -1"
x = re.findall("[0-9]", txt)
print(x)
if x:
    print("matches")
else:
    print("no match")


txt = "This is lesson starts at 11:45  71:45"
# 0-5 aralığı ondalık kısımları kontrol eder 0-9 ise birinci basamakları 23:59
x = re.findall("[0-5][0-9]", txt)
print(x)
if x:
    print("matches")
else:
    print("no match")

txt = "The Python lesson starts at python morning 11:45  71:45"
x = re.findall("[Pp]ython", txt)
print(x)


txt = "The Python lesson all starts ill at python morning 11:45  71:45"
x = re.findall("[ai]ll", txt)
print(x)

txt = "The Python lesson all starts ill at python morning 11:45  71:45"
x = re.sub("\s", "1", txt)
x2 = re.sub("e", "E", txt)
print(x)
print(x2)


p = re.compile("colou?r")  # u harfi ya 1 ya 0 tane olucak
n = p.search("The color green")
print(n.start())  # index at print
n = p.search("abc")
print(n)


# PANDAS
df = pd.read_csv('ds_salaries.csv')


print(df.shape, " \nSHAPE ")
print(df.columns, "\nCOLUMNS ")
print(df.dtypes, " \nTYPES ")
print(df.head(2), " \nHEAD ")  # first 2 data
print(df.tail(), " \nTAIL ")  # last 5 data
print(df.info(), " \nINFO ")
print(df.describe(), "\nDESCRIBE ")
