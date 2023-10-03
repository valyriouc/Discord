
from dataProvider import DataProvider 

class TestDataProvider(DataProvider):
    temp = 31.2
    humidity = 230.4
    pressure = 1019.5
    
    def request_data(self, data: dict):
        res = ""
        first = True
        for command in data:
            if not first:
                res += ","
            if command["identifier"] == "temp":
                res += f" {self.temp}"
            if command["identifier"] == "humid":
                res += f" {self.humidity}"
            if command["identifier"] == "press":
                res += f" {self.pressure}"
            if command["identifier"] == "LED":
                res = "LEDs will be turned on"
                break
            if command["identifier"] == "Change text":
                res = f"Reset LED matrix to {(command['content'])}"
            first = False
        return res
