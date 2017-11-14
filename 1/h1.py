def ugly(number):
    if number%2==0 & number%3==0 & number%5==0:
        return True
    elif number==1:
        return True
    else:
        return False