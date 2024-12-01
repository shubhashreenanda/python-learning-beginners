class Patient:
    def setId(self,id):
        self.id = id

    def getId(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSsn(self, ssn):
        self.ssn = ssn

    def getSsn(self):
        return self.ssn

    def display(self):
        print(self.id)
        print(self.name)
        print(self.ssn)

p = Patient()
p.setId(1234567890)
p.setName("Sheeman Nanda")
p.setSsn(7260801092)


print(p.getId())
print(p.getName())
print(p.getSsn())

p.display()