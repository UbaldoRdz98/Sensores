import json
class classJson:
    def __init__(self, filename = "file.json"):
        self.filename = filename
        pass

    def saveToJson(self, data):
        with open(self.filename, "w") as myFile:
            json.dump(data, myFile, indent = 4)

    def readToJson(self):
        try:
            with open(self.filename, "r") as myFile:
                data = json.load(myFile)
            if(data):
                return data
        except:
            pass
        return None