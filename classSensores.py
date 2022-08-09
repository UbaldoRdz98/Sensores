import RPi.GPIO as GPIO
import time, sys
import serial
from decimal import Decimal
from datetime import datetime
from classLista import ListObject
from classDatos import DatosSensores
from w1thermsensor import W1ThermSensor, Unit
class Sensores(ListObject):
    def __init__(self, tipo="", nombre="", pines =[]):
        self.count = 0
        self.start_counter = 0
        self.tipo = tipo
        self.nombre = nombre
        self.pines = pines
        self.valor = 0.0
        self.fecha = None
        super(Sensores,self).__init__()
        self.filename = "JSONS/listSensores.json"

    def getDict(self):
        if (len(self._lista) > 0):
            lista = list()
            for value in self._lista:
                lista.append(value.getDict())
            return lista
        elif (self.tipo):
            return {"Tipo": self.tipo, "Nombre": self.nombre, "Pines": self.pines}
        else:
            return []

    def load(self):
        data = self.readToJson()
        if(data):
            self.dictToObject(data)

    def dictToObject(self, listData):
        for value in listData:
            self.add(Sensores(value["Tipo"], value["Nombre"], value["Pines"]))

    def countPulse(self, channel):
        if self.start_counter == 1:
            self.count = self.count+1

    def read(self):
        if self.tipo == "Caudal":
            x = self.readCaudal()
            return x
        elif self.tipo == "Temperatura":
            x = self.readTemperatura(self.pines)
            return x
        elif self.tipo == "Humedad":
            x = self.readHumedad(self.pines)
            return x
        elif self.tipo == "Fotoresistencia":
            x = self.readFotoresistencia(self.pines)
            return x
        elif self.tipo == "Movimiento":
            x = self.readMovimiento(self.pines)
            return x
        elif self.tipo == "Oxigeno":
            x = self.readOxigeno(self.pines)
            return x
        elif self.tipo == "Bomba":
            x = self.readBomba(self.pines)
            return x
        else:
            0

    def readCaudal(self):
        objSen = Sensores(self.tipo, self.nombre, self.pines[0])
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pines[0], GPIO.IN, pull_up_down = GPIO.PUD_UP)
        GPIO.add_event_detect(self.pines[0], GPIO.FALLING, callback=self.countPulse)
        try:
            self.start_counter = 1
            time.sleep(1)
            self.start_counter = 0
            flow = (self.count / 7.5)
            self.count = 0
            time.sleep(5)
            ct = datetime.now()
            ts = ct.timestamp()
            objSen.fecha = ts
            objSen.valor = flow
            return objSen
        except KeyboardInterrupt:
            print('\ncaught keyboard interrupt!, bye')
            GPIO.cleanup()
            sys.exit()
        finally:
            GPIO.cleanup()

    def readTemperatura(self, Pin):
        objSen = Sensores(self.tipo, self.nombre, self.pines[0])
        sens = W1ThermSensor()
        temp = sens.get_temperature()
        time.sleep(1)
        ct = datetime.now()
        ts = ct.timestamp()
        objSen.fecha = ts
        objSen.valor = temp
        return objSen

    def readHumedad(self, Pin):
        objSen = Sensores(self.tipo, self.nombre, self.pines[0])
        ser = serial.Serial('/dev/ttyUSB0',9600)
        ser.flushInput()
        lineBytes = ser.readline()
        line = lineBytes.decode('utf-8').strip()
        objSen.valor = float(line)
        return objSen

    def readFotoresistencia(self, Pin):
        objSen = Sensores(self.tipo, self.nombre, self.pines[0])
        objSen.valor = 425.23
        return objSen

    def readMovimiento(self, Pin):
        objSen = Sensores(self.tipo, self.nombre, self.pines[0])
        objSen.valor = 1
        return objSen

    def readOxigeno(self, Pin):
        objSen = Sensores(self.tipo, self.nombre, self.pines[0])
        objSen.valor = 49.52
        return objSen

    def readBomba(self, Pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(Pin, GPIO.OUT)
        try:
            GPIO.output(Pin, GPIO.LOW)
            time.sleep(10)
            GPIO.output(Pin, GPIO.HIGH)
            time.sleep(10)
        finally:
            GPIO.cleanup()
        return 1
