from math import sqrt
import Global_data

#funkcja ksztaltu
def N1(ksi, eta):
    return 0.25 * (1 - ksi) * (1 - eta)

def N2(ksi, eta):
    return 0.25 * (1 + ksi) * (1 - eta)

def N3(ksi, eta):
    return 0.25 * (1 + ksi) * (1 + eta)

def N4(ksi, eta):
    return 0.25 * (1 - ksi) * (1 + eta)

#pochodne
def dNdeta(ksi, x):
    if x == 0:
        return -0.25 * (1 - ksi)
    elif x == 1:
        return -0.25 * (1 + ksi)
    elif x == 2:
        return 0.25 * (1 + ksi)
    elif x == 3:
        return 0.25 * (1 - ksi)

def dNdksi(eta, x):
    if x == 0:
        return -0.25 * (1 - eta)
    elif x == 1:
        return 0.25 * (1 - eta)
    elif x == 2:
        return 0.25 * (1 + eta)
    elif x == 3:
        return -0.25 * (1 + eta)


#def phicial_cons(tksi,teta,C_pc,weights):
#ksi,eta(...)
#__init__(x):
#   dict(x):
#       dict4
#       get(x)
#     #     fill4()...
##def Fill16

#ksi eta weights
#16
def Fill16(tksi,teta,C_pc,weights):
    for i in range(16):
        if i == 0:
            ksi = -0.861136
            eta = -0.861136
            weights[i] = 0.347855 * 0.347855
        elif i == 1:
            ksi = -0.339981
            eta = -0.861136
            weights[i] = 0.652145 * 0.347855
        elif i == 2:
            ksi = 0.339981
            eta = -0.861136
            weights[i] = 0.652145 * 0.347855
        elif i == 3:
            ksi = 0.861136
            eta = -0.861136
            weights[i] = 0.347855 * 0.347855
        elif i == 4:
            ksi = -0.861136
            eta = -0.339981
            weights[i] = 0.652145 * 0.347855
        elif i == 5:
            ksi = -0.339981
            eta = -0.339981
            weights[i] = 0.652145 * 0.652145
        elif i == 6:
            ksi = 0.339981
            eta = -0.339981
            weights[i] = 0.652145 * 0.652145
        elif i == 7:
            ksi = 0.861136
            eta = -0.339981
            weights[i] = 0.652145 * 0.347855
        elif i == 8:
            ksi = -0.861136
            eta = 0.339981
            weights[i] = 0.652145 * 0.347855
        elif i == 9:
            ksi = -0.339981
            eta = 0.339981
            weights[i] = 0.652145 * 0.652145
        elif i == 10:
            ksi = 0.339981
            eta = 0.339981
            weights[i] = 0.652145 * 0.652145
        elif i == 11:
            ksi = 0.861136
            eta = 0.339981
            weights[i] = 0.652145 * 0.347855
        elif i == 12:
            ksi = -0.861136
            eta = 0.861136
            weights[i] = 0.347855 * 0.347855
        elif i == 13:
            ksi = -0.339981
            eta = 0.861136
            weights[i] = 0.652145 * 0.347855
        elif i == 14:
            ksi = 0.339981
            eta = 0.861136
            weights[i] = 0.652145 * 0.347855
        elif i == 15:
            ksi = 0.861136
            eta = 0.861136
            weights[i] = 0.347855 * 0.347855

        for j in range(4):
            teta[i][j] = dNdeta(ksi, j)
            tksi[i][j] = dNdksi(eta, j)

        C_pc[i][0] = N1(ksi, eta)
        C_pc[i][1] = N2(ksi, eta)
        C_pc[i][2] = N3(ksi, eta)
        C_pc[i][3] = N4(ksi, eta)

#9
def fill9(tksi,teta,C_pc,weights):
    k = sqrt(3.0 / 5.0)
    e = sqrt(3.0 / 5.0)
    for i in range(9):
        if i == 0:
            ksi = -1.0 * k
            eta = -1.0 * e
            weights[i] = (5.0 / 9.0) * (5.0 / 9.0)
        elif i == 1:
            ksi = 0.0 * k
            eta = -1.0 * e
            weights[i] = (8.0 / 9.0) * (5.0 / 9.0)
        elif i == 2:
            ksi = 1.0 * k
            eta = -1.0 * e
            weights[i] = (5.0 / 9.0) * (5.0 / 9.0)
        elif i == 3:
            ksi = -1.0 * k
            eta = 0.0
            weights[i] = (5.0 / 9.0) * (8.0 / 9.0)
        elif i == 4:
            ksi = 0.0 * k
            eta = 0.0 * e
            weights[i] = (8.0 / 9.0) * (8.0 / 9.0)
        elif i == 5:
            ksi = 1.0 * k
            eta = 0.0
            weights[i] = (5.0 / 9.0) * (8.0 / 9.0)
        elif i == 6:
            ksi = -1.0 * k
            eta = 1.0 * e
            weights[i] = (5.0 / 9.0) * (5.0 / 9.0)
        elif i == 7:
            ksi = 0.0 * k
            eta = 1.0 * e
            weights[i] = (8.0 / 9.0) * (5.0 / 9.0)
        elif i == 8:
            ksi = 1.0 * k
            eta = 1.0 * e
            weights[i] = (5.0 / 9.0) * (5.0 / 9.0)
        for j in range(4):
            teta[i][j] = dNdeta(ksi, j)
            tksi[i][j] = dNdksi(eta, j)
        C_pc[i][0] = N1(ksi, eta)
        C_pc[i][1] = N2(ksi, eta)
        C_pc[i][2] = N3(ksi, eta)
        C_pc[i][3] = N4(ksi, eta)

#4
def fill4(tksi,teta,C_pc,weights):
    k = -sqrt(1.0 / 3.0)
    e = sqrt(1.0 / 3.0)
    for i in range(4):
        weights[i] = 1.0
        if i == 0:
            ksi = 1.0 * k
            eta = -1.0 * e
        elif i == 1:
            ksi = -1.0 * k
            eta = -1.0 * e
        elif i == 2:
            ksi = 1.0 * k
            eta = 1.0 * e
        elif i == 3:
            ksi = -1.0 * k
            eta = 1.0 * e
        for j in range(4):
            teta[i][j] = dNdeta(ksi, j)
            tksi[i][j] = dNdksi(eta, j)
        C_pc[i][0] = N1(ksi, eta)
        C_pc[i][1] = N2(ksi, eta)
        C_pc[i][2] = N3(ksi, eta)
        C_pc[i][3] = N4(ksi, eta)
