from bs4 import BeautifulSoup
import urllib
import requests
import os
import sys

#Cozmo SDK
import cozmo

#Downloading page
r  = requests.get('http://www.mambiente.munimadrid.es/opencms/opencms/calaire/consulta/Gases_y_particulas/informegaseshorarios_antiguo.html?__locale=es')
data = r.text
soup = BeautifulSoup(data,"lxml")

#Scrapping the NO2 values
date=soup.find('span',class_="tabla_titulo_hora")
#date=str(date)
#last_issue=last_issue[last_issue.find("MagPi")+5:last_issue.find(">")-5]

date=date.strings
#print(date)

for data in date:
    print(data+"\n")

stations_data=soup.find_all('td',class_="primertd")

for station in stations_data:
    print(str(station.string));
    station.headers
def cozmo_program(robot: cozmo.robot.Robot):

    print("COZMO:")

#    for stations in stations_data:
#        robot.say_text(stations.string).wait_for_completed()
    #robot.play_anim(name="id_poked_giggle").wait_for_completed()
    #cube1.set_lights(cozmo.lights.green_light)
    #cube2.set_lights(cozmo.lights.blue_light)
    #cube3.set_lights(cozmo.lights.red_light)
    #robot.say_text("We wish you a happy new year!",in_parallel=True)#.wait_for_completed()
    #robot.play_anim_trigger(cozmo.anim.Triggers.CodeLabWin, in_parallel=False).wait_for_completed()
    #robot.say_text("We wish you a happy new year!",in_parallel=False,play_excited_animation=True).wait_for_completed()



    #Animation lists
    #coz = robot.wait_for_robot()
    #print("All animations = %s" % coz.anim_names)

    
    #CodeLabPartyTime

    # Keep the lights on for 10 seconds until the program exits
    #time.sleep(10)


    
cozmo.run_program(cozmo_program)



'''
#Quotes
#for actual_quote in web_body:
for actual_quote in list_of_quotes:
    auxiliar_object=quote()
    auxiliar_object.new(key,actual_quote.get_text())
    quotes_objects.append(auxiliar_object)
    #auxiliar_object.show_quote()

'''

#http://www.mambiente.munimadrid.es/opencms/opencms/calaire/consulta/Gases_y_particulas/informegaseshorarios.html?__locale=es



'''
print("\nLast issue number: {}".format(last_issue))

for issue in range(int(last_issue)):
    try:
        issue=issue+1
        if not os.path.exists("./magpi-issues/Magpi{:02d}.pdf".format(issue)):
            print("Downloading https://www.raspberrypi.org/magpi-issues/MagPi{:02d}.pdf".format(issue))
            urllib.urlretrieve ("https://www.raspberrypi.org/magpi-issues/MagPi{:2d}.pdf".format(issue), "./magpi-issues/Magpi{:02d}.pdf".format(issue))
    except():
        print(" \nERROR: There was an error downloading Magpi{:02d}\n".format(issue))
    else:
        print(" MagPi{:02d} Downloaded!\n".format(issue))
'''
