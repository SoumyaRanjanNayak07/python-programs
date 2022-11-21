class Convert():
    def getString(self,string):
        self.string=string
    def printString(self):
        self.string=self.string.upper()
        return self.string 

c=Convert()
c.getString("Soumya")
print(c.printString())