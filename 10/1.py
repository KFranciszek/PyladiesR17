def readfile():
    print(str(file.read()))

option = input("Input: ")
try:
    if option == "1":
        file = open("x.txt")
    elif option == "2":
        file = open("y.txt")
    elif option == "3":
        file = open("z.txt")
    else:
        print("Wrong input!")
except FileNotFoundError:
    print("Nie ma pliku")
readfile()
file.close()