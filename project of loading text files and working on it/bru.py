### make a list of fruits

lst = list(("strawberry","kiwi","lemon","lime","bruh fruit","i don't know fruit"))

### use a for loop to print i like mango...
TXT  = ''
for each in lst:
    print("i like",each)
    TXT = TXT + "i like "+each + '\n'
### save it to fruits.txt file


with open('fruits.txt', 'w') as f:
   f.write(TXT)

