def get_time(time, retop):
    timel = str.split(time, ":")
    if len(timel)!=3:
        return "Wrong time format"
    for i in range(3):
        timel[i-1]=int(timel[i-1])
    if retop=='s':
        print(timel[0]*3600+timel[1]*60+timel[2])
    elif retop=='m':
        print(timel[0] * 60 + timel[1] + timel[2]/60)
    elif retop=='h':
        print(timel[0]  + timel[1] / 60 + timel[2]/3600)
    else:
        return "Wrong return format"

get_time('00:15:59', 's')