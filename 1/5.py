import countries


def szukaj(dict1, wartosc):
    i=0
    country = list(dict1)[0]
    print(country["name"]["official"])
    while i < len(dict1):
        country = list(dict1)[i]
        if country["subregion"]==wartosc:
            print(country["name"]["official"])
        i+=1





szukaj(countries.countries, "Northern America")