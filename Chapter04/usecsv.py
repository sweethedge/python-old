import csv, os, re

# "가져다 쓰는 데 의미가 있다"

def opencsv(filename):
    f = open(filename, "r", encoding="UTF-8")
    new = csv.reader(f)

    a_list = []

    for line in new:
        a_list.append(line)

    f.close()
    return a_list

def writecsv(filename, the_list):
    f = open(filename, 'w', encoding="UTF-8", newline='')
    csvobject = csv.writer(f, delimiter=',')
    csvobject.writerows(the_list)
    f.close()

def switch(listName):
    for i in listName:
        for j in i:
            try:
                i[i.index(j)] = float(re.sub(',', '', j))
            except:
                pass
    return listName