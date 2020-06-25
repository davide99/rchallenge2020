class ProjectManager(object):
    def __init__(self, stringa):
        self.company = stringa.split()[0]
        self.bonus = int(stringa.split()[1])
        self.used = False

    def toString(self):
        print("Company: " + self.company)
        print("Bonus: " + str(self.bonus))

    def getBonus(self):
        return self.bonus

    def getCompany(self):
        return self.company

    def setUsed(self,value):
        self.used = value

    def getUsed(self):
        return self.used

if __name__ == '__main__':
    ProjectManager("opn 2").toString()