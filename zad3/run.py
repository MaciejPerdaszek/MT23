objects = []
file = open('data.txt', 'R')
while True:
    line = file.readline()
    if not line:
        break
    o = line.split(';')
    obj = [o[0], int(o[1]), int[o[2]]]
    objects.append(obj)
file.close()

