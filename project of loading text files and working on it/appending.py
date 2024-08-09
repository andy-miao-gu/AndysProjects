while(True):
    thy = input("what your name not what is your name.")
    thy = thy +'\n'
    if "quit" in thy:
        break
    with open('new_append.txt', 'a') as f:
        f.write(thy)
    
