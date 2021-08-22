#Programa para el curso Crea proyectos con Raspberry Pi 13 edicion
#Basado en https://github.com/CamJam-EduKit/EduKit2/blob/master/CamJam%20EduKit%202%20-%20GPIO%20Zero/CamJam%20EduKit%202%20-%20Sensors%20Worksheet%206%20(GPIO%20Zero)%20-%20Alarm.pdf

#Importacion de librerias de Python
from gpiozero import MotionSensor, LED, Buzzer
from time import sleep

#Creación de un objeto de tipo MotionSensor que almacena el GPIO al que esta conectado el sensor
pir = MotionSensor(17)

#Creación de un objeto de tipo LED que almacena el GPIO al que esta conectado el LED
led = LED(18)

#Creación de un objeto de tipo Buzzer que almacena el GPIO al que esta conectado el buzzer
buzzer = Buzzer(22)

#Esperando que el sensor se asiente
pir.wait_for_no_motion()

print ("Comienza la prueba (CTRL-C para salir)")

#Variables que almacenan los estados actual y pasado
estadoActual = False
estadoPasado = False

try:
    #Bucle hasta que el usuario salga con CTRL-C
    while True:
        #Leer el estado del sensor
        estadoActual = pir.motion_detected
        
        #Si el sensor es activado
        if estadoActual == True and estadoPasado == False:
            print ("Movimiento detectado!")
            
            #Se activan las alarmas visual y sonora
            led.on()
            buzzer.on()
            sleep(2)
            led.off()
            buzzer.off()
            
            #Se actualiza el estado
            estadoPasado = True
        
        #Si el sensor ha vuelto al estado "preparado para detectar"
        elif estadoActual == False and estadoPasado == True:
            print ("No hay movimiento")
            #Se actualiza el estado
            estadoPasado = False
        
        #Espera para establilizar los circuitos
        sleep(0.1)
            
except KeyboardInterrupt:
    print ("Saliendo")

