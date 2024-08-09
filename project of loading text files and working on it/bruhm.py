# get user input

txt = ""
while(True):
    fg = input("bruh what your name not what is your name.")
    if "quit" in fg:
        break

    ###c save it to current string
    txt = txt + fg + '\n'
    
    
 

with open('readme.txt', 'w') as f:
   f.write(txt)




