from classJson import classJson
class ListObject(classJson):
    def __init__(self):
        self._lista = list()
        super(ListObject, self).__init__

    def add(self, objeto):
        self._lista.append(objeto)

    def update(self, index, objeto):
        self._lista[index] = objeto

    def delete(self, index):
        self._lista.pop(index)

    def getList(self):
        return self._lista

    def getElement(self, index):
        return self._lista[index]

    def saveData(self):
        self.saveToJson(self.getDict())