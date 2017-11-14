import countries

def szukaj(dict1, klucz, wartosc, funkcja):
    if funkcja==1 or funkcja==2:
        i=0
        while i < len(dict1):
            country = list(dict1)[i]
            if funkcja==1:
                if country[klucz]==wartosc:
                    print(country["name"]["official"])
            elif funkcja==2:
                if country[klucz]!=wartosc:
                    print(country["name"]["official"])
            i+=1
    elif funkcja==3:
        i = 0
        while i < len(dict1):
            country = list(dict1)[i]
            if len(country[klucz])>1:
                print(country["name"]["official"])
                print(country[klucz])
            i+=1
szukaj(countries.countries,"currency", "", 3)