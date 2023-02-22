import numpy as np
import re

# set the xx for the ammount of points of integrals and x accordingly (if xx = 2, then x = 4. If xx = 3, x = 9 etc.)
x = 16  # 4/9/16
xx = 4  # 2/3/4
file = open("Test1_4_4.txt", "r")


class node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.t = 0.0
        self.BC = 0


class BOK():
    def __init__(self, pC):
        self.pC = pC
        self.ID = np.zeros(shape=(pC * 4, 2), dtype=float)
        self.pCValue = np.zeros(shape=(4, 4), dtype=float)


# element
class ELEMENT():
    def __init__(self, a, b, c, d, pC):
        self.ID = [a, b, c, d]
        self.HBC = np.zeros(shape=(4, 4), dtype=float)
        self.bok = [None] * 4
        for i in range(4):
            self.bok[i] = BOK(pC)


# Integral / całka powierzchni
class GRID:
    def __init__(self, nn, en):
        self.nE = en
        self.nN = nn
        self.ND = [] * nn
        self.EL = [] * en
    #
    # def __repr__(self):
    #     return self.EL.bok


Simulation_time = file.readline().split()[1]
Step_Time = file.readline().split()[1]
global_data = {"conductivity": float(re.sub(r"\b[^\d\W]+\b", "", file.readline().split()[1])),
               "alfa": float(re.sub(r"\b[^\d\W]+\b", "", file.readline().split()[1])),
               "tot": float(re.sub(r"\b[^\d\W]+\b", "", file.readline().split()[1])),
               "initialtemp": float(re.sub(r"\b[^\d\W]+\b", "", file.readline().split()[1])),
               "density": float(re.sub(r"\b[^\d\W]+\b", "", file.readline().split()[1])),
               "specifiheat": float(re.sub(r"\b[^\d\W]+\b", "", file.readline().split()[1]))}

grid = {}
grid["nN"] = int(re.sub(r"\b[^\d\W]+\b", "", file.readline().split()[2]))
grid["nE"] = int(re.sub(r"\b[^\d\W]+\b", "", file.readline().split()[2]))

grid1 = GRID(grid["nN"], grid["nE"])

file.readline()
nodes = []
for i in range(grid["nN"]):
    temp = file.readline().split()
    nodes.append(node(float(temp[1].replace(",", "")), float(temp[2].replace(",", ""))))  # .append(node.constructor())

file.readline()  # skip a line

elements = []  # element array
for i in range(grid["nE"]):
    temp = file.readline().split()

    elements.append(ELEMENT(int(temp[1].replace(",", "")), int(temp[2].replace(",", "")), int(temp[3].replace(",", "")),
                            int(temp[4]), xx))  # ,b1,b2,b3,b4

file.readline()

temp = file.readline().replace(",", "").split()
for i in range(len(temp)):
    nodes[int(temp[i]) - 1].BC = 1

grid1.EL = elements
grid1.ND = nodes

file.close()


## TO-DO
## Parsowanie w klasie
##