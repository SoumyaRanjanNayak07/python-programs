class America:
    def __init__(self,countryname):
        print("country name is: ",countryname)
class newyork(America):
    def __init__(self):
        super().__init__("America")
        print("city name is Newyork")
n=newyork()
                