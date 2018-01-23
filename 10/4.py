przelicznik = {'PLN': 1, 'USD': 1000, 'EURO': 4505, 'JPY': 100}

def convert(some_string):
    query = some_string.split(" ")
    query = list(filter(None, query))
    value = int(query[0])/przelicznik[query[1]]
    return value*przelicznik[str(query[3])]

print(convert("2 USD to JPY"))