file = open('py1.2.txt', 'r')
data = file.readlines()
file.close()
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