from classLista import ListObject
class DatosSensores(ListObject):
    def __init__(self, fecha=None, valor=0.0):
        self.fecha = fecha
        self.valor = valor
        from classSensores import Sensores
        self.Sensor = Sensores()
        super(DatosSensores,self).__init__()
        self.filename = "JSONS/listDatosSensores.json"

    def getDict(self):
        if (len(self._lista) > 0):
            lista = list()
            for value in self._lista:
                lista.append(value.getDict())
            return lista
        elif (self.fecha):
            return {"Fecha": self.fecha, "Valor": self.valor, "Sensores": self.Sensor.getDict()}
        else:
            return []

    def load(self):
        data = self.readToJson()
        if(data):
            self.dictToObject(data)

    def dictToObject(self, listData):
        for value in listData:
            from classSensores import Sensores
            d = DatosSensores(value["Fecha"], value["Valor"])
            s = Sensores()
            s.dictToObject(value["Sensor"])
            d.Sensor = S
            self.add(d)