"""
    SerialInterface.py
    --------------------------------------
    Controls a Zowi by sending commands through a serial port
"""

__author__ = "def"
__licence__ = "GPLv3"

import serial

class SerialInterface:

    def __init__(self):
        self.serialPort = None


    def connect(self, port, baudrate):
        """
        Connect with the serial port at a certain baudrate
        """
        # Setup serial port
        self.serialPort = serial.Serial()
        self.serialPort.port = port
        self.serialPort.baudrate = baudrate

        # Open port
        self.serialPort.open()

        if not self.serialPort.isOpen():
            raise IOError("Port could not be opened!")

    def testZowi(self):
        """
        Sends the command to move the servo to waves
        """

        command = "M 5 1000 30\r\n"

        try:
            self.serialPort.write(command)
        except AttributeError, e:
            print 'Not connected: [' + str(e) + ']'

    def stopZowi(self):
        """
        Sends the command to move the servo to waves
        """

        command = "S\r\n"

        try:
            self.serialPort.write(command)
        except AttributeError, e:
            print 'Not connected: [' + str(e) + ']'

    def toneZowi(self,frecuency, time):
        """
        Zowi buzzer /sounds
        """

        command = "T "+ str(frecuency)+" "+str(time)+"\r\n"

        try:
            self.serialPort.write(command)
        except AttributeError, e:
            print 'Not connected: [' + str(e) + ']'
    def moveZowi(self,move, duration):
        """
        Zowi make a specific /move
        """

    	if move=="forwards":
    		command = "M 1 "+ str(duration)+"\r\n"
    	elif move=="backwards":
    		command = "M 2 "+ str(duration)+"\r\n"
    	elif move=="turn_right":
    		command = "M 3 "+ str(duration)+"\r\n"
    	elif move=="turn_left":
    		command = "M 4 "+ str(duration)+"\r\n"
    	elif move=="jumping":
    		command = "M 5 "+ str(duration)+"\r\n"
    	elif move=="moonwalk_right":
    		command = "M 6 "+ str(duration)+"\r\n"
    	elif move=="moonwalk_left":
    		command = "M 7 "+ str(duration)+"\r\n"
    	elif move=="swing":
    		command = "M 8 "+ str(duration)+"\r\n"
    	elif move=="cross_right":
    		command = "M 9 "+ str(duration)+"\r\n"
    	elif move=="cross_left":
    		command = "M 10 "+ str(duration)+"\r\n"
    	elif move=="jump":
    		command = "M 11 "+ str(duration)+"\r\n"
    	elif move=="forwards_fast":
    		command = "M 12 "+ str(duration)+"\r\n"
    	elif move=="backwards_fast":
    		command = "M 13 "+ str(duration)+"\r\n"
    	elif move=="swing_":
    		command = "M 14 "+ str(duration)+"\r\n"
    	elif move=="incline_right":
    		command = "M 15 "+ str(duration)+"\r\n"
    	elif move=="incline_left":
    		command = "M 16 "+ str(duration)+"\r\n"
    	elif move=="shake_right":
    		command = "M 17 "+ str(duration)+"\r\n"
    	elif move=="shake_left":
    		command = "M 18 "+ str(duration)+"\r\n"
    	elif move=="tremble":
    		command = "M 19 "+ str(duration)+"\r\n"
    	elif move=="turn_up":
    		command = "M 20 "+ str(duration)+"\r\n"

        try:
            self.serialPort.write(command)
        except AttributeError, e:
            print 'Not connected: [' + str(e) + ']'

    def gestureZowi(self,gesture):
        """
        Zowi make a /gesture
        """

    	if gesture=="happy":
    		command = "H 1\r\n"
    	elif gesture=="superhappy":
    		command = "H 2\r\n"
    	elif gesture=="sad":
    		command = "H 3\r\n"
    	elif gesture=="sleep":
    		command = "H 4\r\n"
    	elif gesture=="fart":
    		command = "H 5\r\n"
    	elif gesture=="confused":
    		command = "H 6\r\n"
    	elif gesture=="love":
    		command = "H 7\r\n"
    	elif gesture=="angry":
    		command = "H 8\r\n"
    	elif gesture=="nervous":
    		command = "H 9\r\n"
    	elif gesture=="magic":
    		command = "H 10\r\n"
    	elif gesture=="crazy_wave":
    		command = "H 11\r\n"
    	elif gesture=="victory":
    		command = "H 12\r\n"
    	elif gesture=="gameover":
    		command = "H 13\r\n"

        try:
            self.serialPort.write(command)
        except AttributeError, e:
            print 'Not connected: [' + str(e) + ']'

    def soundZowi(self,sound):
        """
        Zowi make a predifined /sound
        """

    	if sound=="connect":
    		command = "K 1\r\n"
    	elif sound=="disconect":
    		command = "K 2\r\n"
    	elif sound=="surprise":
    		command = "K 3\r\n"
    	elif sound=="ohohoh":
    		command = "K 4\r\n"
    	elif sound=="ohohoh2":
    		command = "K 5\r\n"
    	elif sound=="cuddly":
    		command = "K 6\r\n"
    	elif sound=="sleeping":
    		command = "K 7\r\n"
    	elif sound=="happy":
    		command = "K 8\r\n"
    	elif sound=="superhappy":
    		command = "K 9\r\n"
    	elif sound=="happy_short":
    		command = "K 10\r\n"
    	elif sound=="sad":
    		command = "K 11\r\n"
    	elif sound=="confused":
    		command = "K 12\r\n"
    	elif sound=="fart":
    		command = "K 13\r\n"
    	elif sound=="fart2":
    		command = "K 14\r\n"
    	elif sound=="fart3":
    		command = "K 15\r\n"
    	elif sound=="mode1":
    		command = "K 16\r\n"
    	elif sound=="mode2":
    		command = "K 17\r\n"
    	elif sound=="mode3":
    		command = "K 18\r\n"
    	elif sound=="buttonpushed":
    		command = "K 18\r\n"

        try:
            self.serialPort.write(command)
        except AttributeError, e:
            print 'Not connected: [' + str(e) + ']'

# If the script is run directly, this example is executed:
if __name__ == "__main__":
    import time as t

    interface = SerialInterface()
    print 'Este no es el archivo que debes ejecutar'

    t.sleep(5)
