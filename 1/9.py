import countries

def najw_pow():
    najw=0
    najw_id=""
    i=0
    while i < len(countries.countries):
        country=countries.countries[i]
        if najw < country["area"]:
            najw=country["area"]
            najw_id=country["name"]["official"]
        i+=1
    print(najw_id,najw)

najw_pow()