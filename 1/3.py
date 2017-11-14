def xo_checker(text):
    x=0
    o=0
    for i in list(text):
        if i=='x':
            x+=1
        elif i=='o':
            o+=1
        else:
            print("illegal")
            exit()
    if x==o:
        print("True")
    else:
        print("False")

xo_checker("xoxo")
xo_checker("xoxox")
xo_checker("xopxo")