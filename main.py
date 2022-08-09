from classSensores import Sensores
class Main():
    def __init__(self, data=None):
        self.lstSensores = Sensores()
        if(data == None):
            self.lstSensores.load()
        else:
            self.lstSensores = data

    def menu(self):
        option = ""
        while (option != "s"):
            print("*"*50)
            print("Menu de Sensores")
            print("A Agregar")
            print("M Modificar")
            print("E Eliminar")
            print("C Consultar")
            print("L Leer Sensor")
            print("S Salir")
            option = input("Seleccione una opción:")
            option = option.lower()
            if(option == "c"):
                self.show()
            elif option == "a":
                self.add()
            elif option == "m":
                self.update()
            elif option == "e":
                self.delete()
            elif option == "l":
                self.leerSensor()

    def getDataInput(self):
        s = Sensores()
        s.tipo = input("Ingresa el Tipo de Sensor: ")
        s.nombre = input("Ingresa el Nombre del Sensor: ")
        salir = "s"
        while(salir != "n"):
            pin = int(input("Ingrese el Número del Pin: "))
            s.pines.append(pin)
            salir = input("Quieres agregar más pines? S/N: ")
            salir = salir.lower()
        return s

    def add(self):
        salir = "s"
        while(salir != "n"):
            m = self.getDataInput()
            self.lstSensores.add(m)
            self.lstSensores.saveData()
            salir = input("Quieres agregar otro Sensor S/N: ")
            salir = salir.lower()

    def update(self):
        self.show()
        option=input("Indica cual registro desea modificar: ")
        if (option.isnumeric()):
            m = self.getDataInput()
            self.lstSensores.update(int(option), m)
        else:
            print("Seleccione una opción valida.")
            input()

    def delete(self):
        self.show()
        option = input("Indica cual registro deseas eliminar: ")
        if(option.isnumeric()):
            self.lstSensores.remove(int(option))
        else:
            print("Seleccione una opción valida")
            input

    def show(self):
        print("*"*50)
        print("Datos de los Sensores")
        c = 0
        print(self.lstSensores)
        for a in self.lstSensores.getList():
            print(c, "\t", a.tipo)
            c+=1
        input

    def leerSensor(self):
        print("*"*50)
        c = 0
        for a in self.lstSensores.getList():
            print(c, ".-",a.tipo)
            c = c + 1
        sel = input("Seleccione el Sensor: ")
        senSel = self.lstSensores.getElement(int(sel))
        x = senSel.read()
        print(x.valor)
        input
        input
inter = Main()
inter.menu()
