# WORK IN PROGRESS, ACTUALLY DOESN HAVE ALL THE OPTIONS


import telebot

import ConfigParser
import os

from pyquery import PyQuery as pq
from lxml import etree
import urllib
import re, string
import time


# Read the config file
print '[+] Reading config file...'
config = ConfigParser.ConfigParser()
config.read([os.path.expanduser('./config')])

# Read data
API_TOKEN = config.get('bot', 'name')
API_TOKEN = config.get('bot', 'token')

bot = telebot.TeleBot(API_TOKEN)

@bot.updates.getState
def main():
        #Takes the actual time
        time_notify=time.asctime(time.localtime(time.time()))
        #print(time_notify)
        time_notify=time_notify.split(" ");
        #print(time_notify)
        main_hour=time_notify[3]
        main_hour=main_hour.split(":")
        main_hour=map(int, main_hour)
        print(main_hour)




# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    chat_id = message.chat.id
    #bot.reply_to(message, """\
    bot.send_message(chat_id,"""\
TELEGRAM POLUTION BOT

Este bot te muestra periodicamente el nivel de NO2 en Madrid, escribe /polution para ver los datos de todas las estaciones \
""")

    #bot.send_message(chat_id, 'CHAR IDE ACEPTAD0')

'''
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)
'''


# Handle '/polution'
@bot.message_handler(commands=['polution'])
def send_detailed_polution(message):

    #Acceso al html
    d = pq(url='http://www.mambiente.munimadrid.es/opencms/opencms/calaire/consulta/Gases_y_particulas/informegaseshorarios.html?__locale=es')

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

    #Selection of all the N02 data
    no2rawdata=d('td[headers="NO2"]')
    no2data=no2rawdata.text()
    no2data=no2data.replace("-","0")#Replaces no data with a 0
    no2data=no2data.split(" ")
    no2data = map(int, no2data) #int conversion
    #print(no2data)

    #Info output
    print(date_data+" Buenos dias la media de NO2 en Madrid es: ")
    #bot.send_message(chat_id, "\n\n"+date_data+"\n\nBuenos dias la media de NO2 en Madrid es: ")
    #for x in message.chat.id:
	#bot.send_message(x, "\n\n"+date_data+"\n\nLa media de NO2 en Madrid es: ")

	#t.sleep(3);
	#print(no2data[-1])

    if no2data[-1]>400:
    	print("\n")
    	print(station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico"+"-POSIBLE ALERTA POR POLUCION")
#for x in chat_id:
	#bot.send_message(x, station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico"+"-POSIBLE ALERTA POR POLUCION")
	alert_counter=alert_counter+1
    elif no2data[-1]>250:
	print("\n")
	print(station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico"+"-POSIBLE AVISO POR POLUCION")
		#for x in chat_id:
		#	bot.send_message(x, station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico"+"-POSIBLE AVISO POR POLUCION")
	warning_counter=warning_counter+1
    elif no2data[-1]>200:
	print("\n")
	print(station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico"+"-POSIBLE PREAVISO POR POLUCION")
		#for x in chat_id:
		#	bot.send_message(x, station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico"+"-POSIBLE PREAVISO POR POLUCION")
	prewarning_counter=prewarning_counter+1
    else:
	print("\n")
	print(station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico")
		#for x in chat_id:
	bot.send_message(message.chat.id, station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico")

bot.polling()
