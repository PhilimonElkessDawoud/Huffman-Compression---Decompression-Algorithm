class binasci:

    def __init__(self) -> None:
        pass

    def toBinary(string):
        return "".join([format(ord(char), '#010b')[2:] for char in string])

    def toString(binaryString):
        return "".join([chr(int(binaryString[i : i + 8], 2)) for i in range(0, len(binaryString), 8)])
