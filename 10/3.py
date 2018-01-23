new_string = []
def cezar(raw_string):
    for i in range(len(raw_string)):
        order = ord(raw_string[i])
        if order+1 > 122:
            order -= 25
        else:
            order += 1
        new_string.append(chr(order))
    return "".join(new_string)
my_string = input("String: ")
print(cezar(my_string))