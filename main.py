import copy
import pprint
from developer import Developer
from pm import ProjectManager #project manager (ci siam capiti)

def main():
    #Leggo file riga riga
    f = open("a_solar.txt","r")
    #Leggo la prima riga con n righe e colonne
    f1 = f.readline()
    C, R = f1.split()
    C = int(C)
    R = int(R)
    ufficio=[]

    #Creo variabili per posti rimanenti da assegnare a developers e managers
    rimDev, rimMan = 0,0
    
    #Riempio matrice ufficio
    for _ in range(0, R):
        line = f.readline()
        riga = []
        for char in line:
            if char != '\n':
                riga.append(char)
                if char == 'M':
                    rimMan = rimMan + 1
                elif char == '_':
                    rimDev = rimDev + 1
        ufficio.append(riga)

    #pprint.pprint(ufficio)

    #leggo n developer e riempio struttura dati
    nD = int(f.readline())
    developers = []

    for _ in range(0, nD):
        dev = f.readline()
        developers.append(Developer(dev.strip()))

    # for d in developers:
    #     d.toString()
    

    # #leggo n project manager e riempio struttura dati
    nPM = int(f.readline())
    managers = []

    for _ in range(0, nPM):
        managers.append(ProjectManager(f.readline()))
    
    #for pm in managers:
        #pm.toString()

    c_sol = copy.deepcopy(ufficio)
    b_sol = copy.deepcopy(ufficio)

    bCosto = 0
    costo = [bCosto]
    sol = [b_sol]

    disp(0, 0, ufficio, sol, c_sol, rimMan, rimDev, costo,developers, managers)

    print(sol[0])
    for riga in sol[0]:
        for col in riga:
            if isinstance(col, ProjectManager) or isinstance(col, Developer):
                col.toString()

    # print(calcCosto(sol[0]))
    print(costo[0])

    #Disposizioni di nD + nPM elementi a boh a boh

    f = open("out.txt","w")
    trovato = False

    for dev in developers:
        trovato = False
        for i in range(0, len(sol[0])-1):
            for j in range(0, len(sol[0][0])-1):
                if isinstance(sol[i][j], Developer):
                    if sol[i][j] == dev:
                        trovato = True
                        f.write(str(i) + " " + str(j))
        if trovato == False:
            f.write("X")

    f.close()


def workP(dev1, dev2):
    # print("Skills in comune: " + str(len(developers[8].getSkills() & developers[9].getSkills())))
    # print("Skills non in comune: " + str(len(developers[8].getSkills() ^ developers[9].getSkills())))

    return len(dev1.getSkills() & dev2.getSkills()) * len(dev1.getSkills() ^ dev2.getSkills())

#Sia per dev sia per manager
def bonusP(a, b):
    c1 = a.getCompany()
    c2 = b.getCompany()

    if c1 == c2:
        return a.getBonus() * b.getBonus()
    else: 
        return 0


def totalP(a,b):
    wP, bP = 0,0

    if isinstance(a, Developer) or isinstance(a, ProjectManager):
        if(isinstance(a, Developer) and isinstance(b, Developer)):
            wP = workP(a,b)
        bP = bonusP(a,b)

    return wP + bP
    
def calcCosto(c_sol):
    tot = 0

    for i in range(0, len(c_sol)):
        for j in range(0, len(c_sol[0])):
            if c_sol[i][j] != '#' and c_sol[i][j] != 'M' and c_sol[i][j] != '_':
                if i>=1: 
                    tot = tot + totalP(c_sol[i-1][j], c_sol[i][j])
                    if isinstance(c_sol[i-1][j], ProjectManager):
                        c_sol[i-1][j] = 'M'
                    else: 
                        c_sol[i-1][j] = '_'
                if j>=1: 
                    tot = tot + totalP(c_sol[i][j-1], c_sol[i][j])
                    if isinstance(c_sol[i][j-1], ProjectManager):
                        c_sol[i][j-1] = 'M'
                    else: 
                        c_sol[i][j-1] = '_'
                if i<len(c_sol)-1:  
                    tot = tot + totalP(c_sol[i+1][j], c_sol[i][j])
                    if isinstance(c_sol[i+1][j], ProjectManager):
                        c_sol[i+1][j] = 'M'
                    else: 
                        c_sol[i+1][j] = '_'
                if j<len(c_sol[0])-1: 
                    tot = tot + totalP(c_sol[i][j+1], c_sol[i][j])
                    if isinstance(c_sol[i][j+1], ProjectManager):
                        c_sol[i][j+1] = 'M'
                    else: 
                        c_sol[i][j+1] = '_'

    return tot

def disp(posR, posC, ufficio, b_sol, c_sol, rimMan, rimDev, b_costo, developers, managers):
    
    #terminazione
    if rimMan == 0 and rimDev == 0:
        c_costo = calcCosto(copy.deepcopy(c_sol)) #controllo costo della soluzione corrente
        if c_costo > b_costo[0]:
            b_costo[0] = c_costo
            b_sol[0] = list(map(list, c_sol))
            #pprint.pp(_sol)
        return

    if posC >= len(c_sol[0]):
        posR = posR + 1
        posC = 0

    if posR>=len(c_sol):
        return

    #chimata ricorsiva
    if c_sol[posR][posC] == '_' or isinstance(c_sol[posR][posC], Developer):
        for dev in developers:
            if dev.getUsed() == False:
                c_sol[posR][posC] = dev
                # pprint.pp(c_sol)
                #input()
                dev.setUsed(True)
                disp(posR, posC+1, ufficio, b_sol , c_sol, rimMan, rimDev-1, b_costo, developers, managers)
                dev.setUsed(False)
    elif c_sol[posR][posC] == 'M' or isinstance(c_sol[posR][posC], ProjectManager):
        for man in managers:
            if man.getUsed() == False:
                c_sol[posR][posC] = man
                #pprint.pp(c_sol)
                #input()
                man.setUsed(True)
                disp(posR, posC+1, ufficio, b_sol , c_sol, rimMan-1, rimDev, b_costo, developers, managers)
                man.setUsed(False)
    else:
        disp(posR, posC+1, ufficio, b_sol , c_sol, rimMan, rimDev, b_costo, developers, managers)

if __name__=="__main__":
    main()