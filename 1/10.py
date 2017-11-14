import countries

def najw_gran():
    najw=0
    najw_id=""
    i=0
    while i < len(countries.countries):
        country=countries.countries[i]
        if najw < len(country["borders"]):
            najw=len(country["borders"])
            najw_n=country["borders"]
            najw_id=country["name"]["official"]
        i+=1
    print(najw_id,najw_n)

najw_gran()