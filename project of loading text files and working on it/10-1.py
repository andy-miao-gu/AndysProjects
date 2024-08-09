##3 write a python code tha
####t can read the text file
with open('learned_thing.txt') as file:
    filler = file.read()
    print(filler)
    
    
    
data = open("learned_thing.txt")
data2 = data.readlines()
for each in data2:
    print("andy:",each.replace("mama","papa"))
    print("Miao","shehehe")

