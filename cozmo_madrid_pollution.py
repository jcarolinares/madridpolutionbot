from bs4 import BeautifulSoup
import urllib
import requests
import os
import sys
import time

#Cozmo SDK
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

#Global lists
station_data=[]
stations_list=[]


def scrapping_madrid_pollution():

    #Downloading page
    r  = requests.get('http://www.mambiente.munimadrid.es/opencms/opencms/calaire/consulta/Gases_y_particulas/informegaseshorarios_antiguo.html?__locale=es')
    data = r.text
    soup = BeautifulSoup(data,"lxml")

    #Scrapping the pollution values
    date=soup.find('span',class_="tabla_titulo_hora")
    #date=str(date)
    #last_issue=last_issue[last_issue.find("MagPi")+5:last_issue.find(">")-5]

    date=date.strings
    #print(date)

    for data in date:
        print(data+"\n")

    #stations_data=soup.find_all('td',class_="primertd")

    stations_raw_data=soup.find_all('tr')

    #Removing headers (twice) from the list
    del stations_raw_data[0]
    del stations_raw_data[0]


    #Station data
    #station_data={'STATION':'','PM10':'','PM2.5':'','SO2':'','CO':'','O3':'','NO2':'','BEN':'','TOL':''}

    for station in stations_raw_data:
        station_name=station.td.string
        auxiliar=station.td.find_next_siblings()

        #Station name
        station_data.append(station_name)
        #print(station_data[0])

        #Stations values
        for value in auxiliar:
            if value.string=="-":
                station_data.append(0)
            else:
                station_data.append(float(value.string))
        
        #print (station_data)
        stations_list.append(station_data[:])
        del station_data[:]    

    #print(stations_list)

    for station in stations_list:
        print(station)

def cozmo_program(robot: cozmo.robot.Robot):

    print("COZMO MADRID POLLUTION")
    print("\nDOWNLOADING POLLUTION DATA\n")
    robot.turn_in_place(degrees(360))#.wait_for_completed()


    #robot.drive_wheels(125, -1)
    scrapping_madrid_pollution()
    #robot.stop_all_motors()

    robot.say_text("The pollution in Madrid in the last hour is: ").wait_for_completed()

    #for station in stations_list:
    #    robot.say_text("At "+station[0]).wait_for_completed()
    #    robot.say_text("The NO2 level is "+str(station[6])).wait_for_completed()


    #Demo mode
    robot.say_text("At "+stations_list[0][0],play_excited_animation=True).wait_for_completed()
    robot.say_text("The NO2 level is "+str(stations_list[0][6]),).wait_for_completed()

    robot.say_text("At "+stations_list[6][0],play_excited_animation=True).wait_for_completed()
    robot.say_text("The NO2 level is "+str(stations_list[6][6])).wait_for_completed()

    robot.say_text("At "+stations_list[9][0],play_excited_animation=True).wait_for_completed()
    robot.say_text("The NO2 level is "+str(stations_list[9][6])).wait_for_completed()


    robot.say_text("Not pollution alerts declared").wait_for_completed()
    
cozmo.run_program(cozmo_program)


