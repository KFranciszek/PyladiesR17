file = open('py1.2.txt', 'r')
data = file.readlines()
file.close()
dataplus={}
datashort={}
slownik={}
for i in range(len(data)):
    data[i] = data[i].split(' cm tall\n')
    a = str(data[i]).split('. ')
    data[i] = a[1]
    a=data[i].split("\', \'\']")
    data[i]=a[0]
for i in range(len(data)):
    data[i]=data[i].split(' has ')
    imie = data[i][0]
    data[i][1]=data[i][1].split(' and is ')
    h=data[i][1][1]
    ec=data[i][1][0]
    a = h.split(' cm tall')
    h = a[0]
    slownik[imie]={'height':h,"eyes":ec}
fileplus=open('hero_200_plus', 'w')
fileshort = open('hero_short', 'w')
for i in slownik:
    if int(slownik[i]['height'])>=200:
        dataplus[i] =slownik[i]
    else:
        datashort[i]=slownik[i]

fileplus.write(str(dataplus))
fileshort.write(str(datashort))
fileplus.close()
fileshort.close()