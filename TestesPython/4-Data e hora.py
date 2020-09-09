from datetime import datetime
now = datetime.now()
ano = now.year
mes = now.month
dia = now.day
print (now)
print (ano)
print (mes)
print (dia)
print ("%02d/%02d/%04d" % (now.day, now.month, now.year))
print ("%02d:%02d:%02d" % (now.hour, now.minute, now.second))
