import datetime
tagadejais_laiks= datetime.datetime.now()
i=int(tagadejais_laiks)

if i<8:
    print("labrīt")
elif i<18:
    print("labdien")
else:
    print("labvakar")

