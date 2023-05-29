class Parser:

    def __init__(self, path: str) -> None:
        self.path = path
        self.text = ""
        self.frequencies = {}
        self.byteNum = 0

        self.compressedPath = path[:-4] + "cmpr.txt"
        self.encodedText = "" 


    def countFrequencies(self, char: str):
        if char in self.frequencies:
            self.frequencies[char] = self.frequencies[char] + 1
        else:
            self.frequencies[char] = 1


    def parseOriginal(self):
        with open(self.path, "r") as file:
            self.text = file.read()
            for char in self.text:
                self.byteNum += 1
                self.countFrequencies(char)

    def parseCompressed(self):
        with open(self.compressedPath, "r", encoding="utf-8") as file:
            self.encodedText = file.read()


    def write(self, text: str):
        with open(self.compressedPath, "w", encoding="utf-8") as file:
            file.write(text)


