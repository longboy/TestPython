import json


class OpearationJson:
    def __init__(self):
        self.data = self.read_data()

    def read_data(self):
        with open("../Logs/modifyheaders.json") as fp:
            data = json.load(fp)
            return data

    def get_data(self, key):
        return self.data[key]


if __name__ == '__main__':
    opjson = OpearationJson()
    print(opjson.get_data("shanghai"))
