def policz_samogloski(tekst):
    liczbasg=0
    samogloski = list("aeouyiAEOUYI")
    for i in list(tekst):
        for a in samogloski:
            if i==a:
                liczbasg+=1
    print(liczbasg)
