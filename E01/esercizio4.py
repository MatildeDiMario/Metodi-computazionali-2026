import numpy as np
from datetime import datetime,timedelta

datenow=datetime.now()
gg=int(input("Scrivi la tua data di nascita: giorno"))

mm=int(input("mese"))

aa=int(input("anno"))

mydate_str="{:}-{:}-{:}".format(aa,mm,gg)
mydate=datetime.strptime(mydate_str,"%Y-%m-%d")
mydatehr_str="{:}".format(mydate)
mydatehr=datetime.strptime(mydatehr_str,"%Y-%m-%d %H:%M:%S")

print("date:",mydatehr)
print("day:",mydatehr.day)
print("hour:",mydatehr.hour)

timediff=datenow-mydatehr
diffanni= datenow.year-mydatehr.year
tots=timediff.total_seconds()
diffgiorni=tots/(60*60*24)
intdiffgiorni=int(diffgiorni)

strg="giorni:{:d}".format(intdiffgiorni)
print(strg)
stra="anni:{:}".format(diffanni)
print(stra)
strs="secondi:{:}".format(tots)
print(strs)



