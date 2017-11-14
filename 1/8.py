import countries

def stolica_na_w(dict1):
    i=0
    while i < len(dict1):
        country=list(dict1)[i]
        capital=country["capital"]
        if len(capital)>1:
            if capital[0]=='W':
                print(country["name"]["official"],capital)
        i+=1

stolica_na_w(countries.countries)