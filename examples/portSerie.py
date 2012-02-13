import serial

#Ouvrir le port série de l'arduino
ser = serial.Serial('/dev/ttyUSB0')  

#Nous envoyons une chaîne de charactère à l'arduino
ser.write("hello world")

#L'arduino est supposé nous renvoyer la même chaîne de charactère
print ser.readline()

#Fermeture du port
ser.close()
