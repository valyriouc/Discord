
from dataProvider import DataProvider 

class TestDataProvider(DataProvider):
    temp = 31.2
    humidity = 230.4
    pressure = 1019.5
    
    def request_data(self, data: dict):
        res = ""
        first = True
        for key in data.keys():
            if not first:
                res += ","
            if key == "temp":
                res += f" {self.temp}"
            if key == "humid":
                res += f" {self.humidity}"
            if key == "press":
                res += f" {self.pressure}"
            first = False
        return res
