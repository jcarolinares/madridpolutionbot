from pyquery import PyQuery as pq
from lxml import etree
import urllib


#Acceso al html
#d = pq("<html></html>")
#d = pq(etree.fromstring("<html></html>"))
d = pq(url='http://www.mambiente.munimadrid.es/opencms/opencms/calaire/consulta/Gases_y_particulas/informegaseshorarios.html?__locale=es')
#d = pq(url='http://google.com/', opener=lambda url, **kw: urllib.urlopen(url).read())
#d = pq(filename='table.html')

#<span class="tabla_titulo_fecha">2016-01-24 09:00:00.0</span>


#Selection of data date
date_data=d('span[class=tabla_titulo_fecha]')
date_data=date_data.text()
#print (date_data)

#Selection of station name
station_name=d('td[class="primertd"]')
station_name=station_name.append("**")
station_name=station_name.text()
station_name=station_name.split("**")
#print(station_name)

del station_name[0] #Delete the first empty element of  the list

#for x in station_name:
#	print(x)
	

#Selection of all the N02 data
no2rawdata=d('td[headers="NO2"]') 
no2data=no2rawdata.text()
no2data=no2data.replace("-","0")#Replaces no data with a 0
no2data=no2data.split(" ")
no2data = map(int, no2data) #int conversion


'''
#Info output
print("\n\nContaminacion de NO2 en Madrid-Fecha: "+date_data)
for x in no2data: 
	if x<20:
		print(str(x)+"-ALERTA POR POLUCION")	
	else:
		print(x)
'''

#Info output
print("\n\nContaminacion de NO2 en Madrid-Fecha: "+date_data)
for x in range(len(no2data)):
	if no2data[x]>400:
		print("\n")
		print(station_name[x]+": "+str(no2data[x])+" microgramos/metro cubico"+"-POSIBLE ALERTA POR POLUCION")
	elif no2data[x]>250:
		print("\n")
		print(station_name[x]+": "+str(no2data[x])+" microgramos/metro cubico"+"-POSIBLE AVISO POR POLUCION")
	elif no2data[x]>200:
		print("\n")
		print(station_name[x]+": "+str(no2data[x])+" microgramos/metro cubico"+"-POSIBLE PREAVISO POR POLUCION")
	else:
		print("\n")
		print(station_name[x]+": "+str(no2data[x])+" microgramos/metro cubico")




