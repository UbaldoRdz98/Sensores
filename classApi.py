import requests
class Api():
    def __init__(self):
        self.url = "http://54.89.74.151:3333/"
        self.invernadero = 1
        self.estacion = 1
        self.estacionNombre = "Estacion-1"
        self.token = ""

    def login(self):
        path = self.url + "login"
        datos = {"email": "estacion@estacion.com", "password": "Integradora123"}
        r = requests.post(path, data=datos)
        x = r.json()
        self.token = x["type"] + " " + x["token"]
        return r.status_code

    def recuperaSensores(self):
        path = self.url + "sensores/getSensoresByEstacionNombre/" + self.estacionNombre
        headers = {"Authorization": self.token}
        r = requests.get(path, headers=headers)
        x = r.json()
        return x

    def createDatosSensor(self, sensor):
        path = self.url + "sensores/createDatosSensor"
        headers = {"Authorization": self.token}
        datos = {"id_sensor": sensor._id, "estacion": self.estacion, "tipo": sensor.tipo, "nombre": sensor.nombre, "valor": sensor.valor}
        r = requests.post(path, data=datos, headers=headers)
        x = r.json()
        return r.status_code