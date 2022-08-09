import http.client
from classSensores import Sensores
from classApi import Api
class Main():
    def __init__(self, data=None):
        self.lstSensores = Sensores()
        self.api = Api()
        if(data == None):
            self.lstSensores.load()
        else:
            self.lstSensores = data

    def menu(self):
        codeApi = 0
        while True:
            if codeApi == 0:
                codeApi = self.api.login()
            for i, val in enumerate(self.lstSensores.getList()):
                senSel = self.lstSensores.getElement(int(i))
                if senSel.tipo != "Bomba":
                    if codeApi == 200:
                        x = senSel.read()
                        self.api.createDatosSensor(x)
                        print(x.tipo)
                        print(x.valor)
                        print(x)

inter = Main()
inter.menu()