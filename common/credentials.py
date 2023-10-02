import common.bots as bots

class Credentials:
    def __init__(self, filename: str) -> None:
        self.filename = filename
    
    def __parse(self) -> dict:
        reading = []
        with open(self.filename, "r") as fobj:
            for line in fobj.readlines():
                reading.append(line.strip())
        res = self.__parse_internal(reading)
        return res 
    
    def __parse_internal(self, reading: list[str]) -> dict:
        res = {}
        it = 0
        while it < len(reading):
            if (reading[it] == ""):
                it += 1
                continue
            name = None
            if reading[it].startswith("#"):
                name = reading[it][1:].strip()
                name = self.__map_names(name)
            it += 1
            block, offset = self.__reading_block(reading[it:])
            res[name] = block
            it += offset
        return res
    
    def __reading_block(self, reading: list[str]) -> dict:
        block = {}
        offset = 0
        if reading[0] != "---":
            raise ValueError("Expected block start (---)")
        offset += 1
        for it in range(1, len(reading)):
            if reading[it] == "---":
                offset += 1
                break
            if (reading[it] == ""):
                offset += 1
                continue
            splited = reading[it].split(":", 1)
            block[splited[0]] = splited[1].strip()
            offset += 1
        return (block, offset)

    # TODO: Separate the parsing and the getting of the credentials 
    def __map_names(self, name: str) -> bots.Bot:
        if name == "Botter":
            return bots.Bot.botter
        if name == "Homie":
            return bots.Bot.homie
        
    @staticmethod
    def get(filepath: str, botId: bots.Bot):
        creds = Credentials(filepath)
        res = creds.__parse()
        if (not botId in res.keys()):
            print("Specified credentials does not exists!")
        return res[botId]
    
if __name__ == "__main__":
    creds = Credentials.get("../auths.txt", bots.Bot.botter)
    print(creds)

