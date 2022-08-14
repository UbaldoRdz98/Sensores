import http.client
from classSensores import Sensores
from classApi import Api
from classJson import classJson
class Main():
    def __init__(self, data=None):
        self.lstSensores = Sensores()
        self.api = Api()
        self.json = classJson()
        self.codeApi = self.api.login()
        x = self.api.recuperaSensores()
        self.json.saveSensores(x)
        if(data == None):
            self.lstSensores.load()
        else:
            self.lstSensores = data

    def menu(self):
        while True:
            codeApi = 0
            if codeApi == 0:
                codeApi = self.api.login()
            for i, val in enumerate(self.lstSensores.getList()):
                senSel = self.lstSensores.getElement(int(i))
                if senSel.tipo != "Bomba":
                    if codeApi == 200:
                        print(1)
                        x = senSel.read()
                        self.api.createDatosSensor(x)
                        if senSel.tipo == "Humedad":
                            print(1)
                            x = senSel.read()
                            if x.valor <= 1024:
                                datosHist = []
                                print(2)
                                for i2, val2 in enumerate(self.lstSensores.getList()):
                                    senSel2 = self.lstSensores.getElement(int(i2))
                                    print(3)
                                    x2 = senSel2.read()
                                    print(4)
                                    if senSel2.tipo != "Bomba":
                                        dat = self.api.createDatosHistorial(x2)
                                        datosHist.append(dat)
                                print("entra")
                                m = self.api.createHistorial("Automatico", datosHist)
                                print("acaba")

inter = Main()
inter.menu()

# def menu(self):
#         codeApi = 0
#         if codeApi == 0:
#             codeApi = self.api.login()
#         for i, val in enumerate(self.lstSensores.getList()):
#             senSel = self.lstSensores.getElement(int(i))
#             if senSel.tipo != "Bomba":
#                 if codeApi == 200:
#                     input
#                     x = senSel.read()
#                     print(x.tipo)
#                     print(x.valor)
#                     self.api.createDatosSensor(x)
#                     if senSel.tipo == "Humedad":
#                         x = senSel.read()
#                         if x.valor <= 1024:
#                             print("entra")
#                             datosHist = []
#                             for i2, val2 in enumerate(self.lstSensores.getList()):
#                                 senSel2 = self.lstSensores.getElement(int(i2))
#                                 if senSel2.tipo != "Bomba":
#                                     x2 = senSel2.read()
#                                     dat = self.api.createDatosHistorial(x2)
#                                     datosHist.append(dat)
#                             print(datosHist)