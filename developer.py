class Developer(object):
    def __init__(self, stringa):
        self.company = stringa.split()[0]
        self.bonus = int(stringa.split()[1])
        self.nSkills = int(stringa.split()[2])
        self.skills = stringa.split()[3:]
        self.used = False

    def toString(self):
        print("Company: " + self.company)
        print("Bonus: " + str(self.bonus))
        print("Skills:")
        for skill in self.skills:
            print("\t " + skill)

    def getCompany(self):
        return self.company

    def getBonus(self):
        return self.bonus

    def getSkills(self):
        return set(self.skills)

    def getUsed(self):
        return self.used

    def setUsed(self,value):
        self.used = value

#if __name__ == '__main__':
#    Developer("opn 7 2 java bpm\n").toString()