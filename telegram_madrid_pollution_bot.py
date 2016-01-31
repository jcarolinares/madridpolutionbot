#####################################################################################################################
##
## Madrid polution bot - Telegram Bot to know the N02 values of Madrid polution
##
#####################################################################################################################


from pyquery import PyQuery as pq
from lxml import etree
import urllib
import ConfigParser
import os
import re, string
import time as t
from twx.botapi import TelegramBot, ReplyKeyboardMarkup, InputFile, InputFileInfo
#from SerialInterface import SerialInterface
import platform



__author__ = 'def'


global chat_id


### Basic bot things ####################################
def load_last_id():
    if not os.path.isfile('id'):
        save_last_id(0)
        return 0

    with open('id', 'r') as f:
        return int(f.readline())

def save_last_id(last_id):
    with open('id', 'w') as f:
    	f.write(str(last_id))

def save_log(id, update_id, chat_id, text):
    with open('log.txt', 'a') as f:
        f.write(str((id, update_id, chat_id, text))+'\n')

### Init configs #########################################


### JukeBot things #######################################
def send_keyboard(bot, user_id):
    keyboard_layout = [['/polution']]
    reply_markup = ReplyKeyboardMarkup.create(keyboard_layout)
    bot.send_message(user_id, 'Este bot te muestra la contaminacion en Madrid!\n Usa /polution', reply_markup=reply_markup)

def get_user_name(user, show_last_name = 0, show_all_info = 0):

    if show_all_info == False:

        if user.username != None: name = user.username
        else:
            name = user.first_name
            if (user.last_name != None) and show_last_name == True: name += " " + user.last_name
    else:
        if (user.first_name != None): name = user.first_name
        else:
            name = "No name"
        if (user.last_name != None): name += " " + user.last_name
        if (user.username != None): name += " " + user.username

    return name





def main():

    prewarning_counter=0
    warning_counter=0
    alert_counter=0
    day_alert_flag=False

    print '[+] Starting bot...'

    # Read the config file
    print '[+] Reading config file...'
    config = ConfigParser.ConfigParser()
    config.read([os.path.expanduser('./config')])

    # Read data
    bot_name = config.get('bot', 'name')
    bot_token = config.get('bot', 'token')
    #user_id=[]
    #user_id.append(config.get('user', 'allowed'))
    #for x in user_id:
    #	print(x)

    #misiones.append(nuevo_elemento)
    user_id= config.get('user', 'allowed')

    # Last mssg id:
    last_id = int(load_last_id())
    print '[+] Last id: %d' % last_id

    # Configure regex
    regex = re.compile('[%s]' % re.escape(string.punctuation))

    # Create bot
    print '[+] Conectando tu bot...'
    bot = TelegramBot(bot_token)
    bot.update_bot_info().wait()

    print '\tBot conectado! El nombre de tu bot es: %s' % bot.username

    # Send special keyboard:
    send_keyboard(bot, user_id)
    print bot

    global chat_id
    chat_id=[]

    while True:
        try:
            updates = bot.get_updates(offset=last_id).wait()
            #print updates[0].message.sender
            #print "-------------------------------"

	    time_notify=t.asctime(t.localtime(t.time()) )
	    #print(time_notify)
	    time_notify=time_notify.split(" ");
	    #print(time_notify)
	    main_hour=time_notify[3]
	    main_hour=main_hour.split(":")
	    main_hour=map(int, main_hour)
	    #print(main_hour)


            for update in updates:#arroja un error de tiempo

                id = update.message.message_id
                update_id = update.update_id
                user = update.message.sender


		#file_chat_id=open('chat_id.txt','r')
		#chat_id_aux=file_chat_id.read()
		#print(chat_id_aux)
		#chat_id.append(update.message.chat.id)
		#for x in chat_id:
		#	print (x)
                active_chat_id = update.message.chat.id
                #chat_id=8999128
		#chat_id2=97335854
		text = update.message.text


		#if main_hour[0]==00 and main_hour[1]==00 and main_hour[2]==00:#Reset the day_alert_flag
		#if main_hour[2]==50:#Reset the day_alert_flag
			#day_alert_flag=False
			#print("FLAG RESETEADA A FALSE")
		if (main_hour[0]==9 and main_hour[1]==30 and main_hour[2]==00) or (main_hour[0]==18 and main_hour[1]==30 and main_hour[2]==00) :
		#if main_hour[2]==00: #and main_hour[2]==00 :# and main_hour[2]==00:
				#day_alert_flag=True #This day the alert is done

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


				#Info output
				print(date_data+" Buenos dias la media de NO2 en Madrid es: ")
				#bot.send_message(chat_id, "\n\n"+date_data+"\n\nBuenos dias la media de NO2 en Madrid es: ")
				for x in chat_id:
					bot.send_message(x, "\n\n"+date_data+"\n\nLa media de NO2 en Madrid es: ")

				t.sleep(3);
				#print(no2data[-1])

				if no2data[-1]>400:
					print("\n")
					print(station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico"+"-POSIBLE ALERTA POR POLUCION")
					for x in chat_id:
						bot.send_message(x, station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico"+"-POSIBLE ALERTA POR POLUCION")
					alert_counter=alert_counter+1
				elif no2data[-1]>250:
					print("\n")
					print(station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico"+"-POSIBLE AVISO POR POLUCION")
					for x in chat_id:
						bot.send_message(x, station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico"+"-POSIBLE AVISO POR POLUCION")
					warning_counter=warning_counter+1
				elif no2data[-1]>200:
					print("\n")
					print(station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico"+"-POSIBLE PREAVISO POR POLUCION")
					for x in chat_id:
						bot.send_message(x, station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico"+"-POSIBLE PREAVISO POR POLUCION")
					prewarning_counter=prewarning_counter+1
				else:
					print("\n")
					print(station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico")
					for x in chat_id:
						bot.send_message(x, station_name[-2]+": "+str(no2data[-1])+" microgramos/metro cubico")
                if int(update_id) > last_id:
                    last_id = update_id
                    save_last_id(last_id)
                    save_log(id, update_id, chat_id, text) #chat_id pertece al usuario ultimo almacenado

                    #text = regex.sub('', text)
                    if text:
                        words = text.split()

                        for i, word in enumerate(words):
                            # Process commands:
                            if word == '/start':
                                print "New user started the app: " + str(user)
				vara=user[0]
				#print("vara: "+str(vara))
				chat_id.append(vara)

				for x in chat_id:
					print(x)

				send_keyboard(bot, active_chat_id)
				#send_keyboard(bot, chat_id)
				#send_keyboard(bot, chat_id2)
                            elif word == '/polution':
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


				#Info output
				print("Contaminacion de NO2 en Madrid-Fecha: "+date_data)

				bot.send_message(active_chat_id, "\n\nContaminacion de NO2 en Madrid-Fecha: "+date_data)
				t.sleep(3);

				for x in range(len(no2data)):
					if no2data[x]>400:
						print("\n")
						print(station_name[x]+": "+str(no2data[x])+" microgramos/metro cubico"+"-POSIBLE ALERTA POR POLUCION")
						bot.send_message(active_chat_id, station_name[x]+": "+str(no2data[x])+" microgramos/metro cubico"+"-POSIBLE ALERTA POR POLUCION")
						alert_counter=alert_counter+1
					elif no2data[x]>250:
						print("\n")
						print(station_name[x]+": "+str(no2data[x])+" microgramos/metro cubico"+"-POSIBLE AVISO POR POLUCION")
						bot.send_message(active_chat_id, station_name[x]+": "+str(no2data[x])+" microgramos/metro cubico"+"-POSIBLE AVISO POR POLUCION")
						warning_counter=warning_counter+1
					elif no2data[x]>200:
						print("\n")
						print(station_name[x]+": "+str(no2data[x])+" microgramos/metro cubico"+"-POSIBLE PREAVISO POR POLUCION")
						prewarning_counter=prewarning_counter+1
					else:
						print("\n")
						print(station_name[x]+": "+str(no2data[x])+" microgramos/metro cubico")
						bot.send_message(active_chat_id, station_name[x]+": "+str(no2data[x])+" microgramos/metro cubico")
				break


        except (KeyboardInterrupt, SystemExit):
            print '\nkeyboardinterrupt caught (again)'
            print '\n...Program Stopped Manually!'
	    #main()
            raise

if __name__  == '__main__':
    main()
