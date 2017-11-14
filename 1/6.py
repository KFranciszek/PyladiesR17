import countries

def szukaj(dict1, klucz, wartosc, zawiera):
    i=0
    country = list(dict1)[0]
    print(country["name"]["official"])
    while i < len(dict1):
        country = list(dict1)[i]
        if zawiera==True:
            if country[klucz]==wartosc:
                print(country["name"]["official"])
        else:
            if country[klucz]!=wartosc:
                print(country["name"]["official"])
        i+=1

szukaj(countries.countries,'region', "Africa", False)