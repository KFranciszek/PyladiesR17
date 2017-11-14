def cenzura_cyfr(text):
    censored=[]
    for i in text:
        try:
            int(i)
        except ValueError:
            censored+=i
        else:
            censored+='#'
    cens=''.join(censored)
    print(cens)


cenzura_cyfr("1a3d5g7")