import numpy as np
from math import sqrt


def N1(ksi, eta):
    return 0.25 * (1 - ksi) * (1 - eta)


def N2(ksi, eta):
    return 0.25 * (1 + ksi) * (1 - eta)


def N3(ksi, eta):
    return 0.25 * (1 + ksi) * (1 + eta)


def N4(ksi, eta):
    return 0.25 * (1 - ksi) * (1 + eta)


def TMatrix(t, ND, tksi, teta, x):
    for i in range(0, x):
        for j in range(0, 4):
            t[i][0] += tksi[i][j] * ND[j].x
            t[i][1] += tksi[i][j] * ND[j].y
            t[i][2] += teta[i][j] * ND[j].x
            t[i][3] += teta[i][j] * ND[j].y


def BC(nrBoku, PC_count, det, con):
    bc = np.zeros(shape=(PC_count, 4), dtype=float)

    if PC_count == 3:
        w = np.zeros(shape=3)
        w[0] = 5.0 / 9.0
        w[1] = 8.0 / 9.0
        w[2] = 5.0 / 9.0
    elif PC_count == 4:
        w = np.zeros(shape=4)
        w[0] = 0.347855
        w[1] = 0.652145
        w[2] = 0.652145
        w[3] = 0.347855
    else:
        w = np.zeros(shape=2)
        w[0] = 1.0
        w[1] = 1.0
    if nrBoku == 0:#contst_bc[nrBoku][PC_count] = bc[i][j]
        if PC_count == 3:
            bc[0][0] = N1(-sqrt(3.0 / 5.0), -1.0)
            bc[0][1] = N2(-sqrt(3.0 / 5.0), -1.0)
            bc[1][0] = N1(0.0, -1.0)
            bc[1][1] = N2(0.0, -1.0)
            bc[2][0] = N1(sqrt(3.0 / 5.0), -1.0)
            bc[2][1] = N2(sqrt(3.0 / 5.0), -1.0)
        elif PC_count == 4:
            bc[0][0] = N1(-0.861136, -1.0)
            bc[0][1] = N2(-0.861136, -1.0)
            bc[1][0] = N1(-0.339981, -1.0)
            bc[1][1] = N2(-0.339981, -1.0)
            bc[2][0] = N1(0.339981, -1.0)
            bc[2][1] = N2(0.339981, -1.0)
            bc[3][0] = N1(0.861136, -1.0)
            bc[3][1] = N2(0.861136, -1.0)
        else:
            bc[0][0] = N1(-sqrt(1.0 / 3.0), -1.0)
            bc[0][1] = N2(-sqrt(1.0 / 3.0), -1.0)
            bc[1][0] = N1(sqrt(1.0 / 3.0), -1.0)
            bc[1][1] = N2(sqrt(1.0 / 3.0), -1.0)
    elif nrBoku == 1:
        if PC_count == 3:
            bc[0][1] = N2(1.0, -sqrt(3.0 / 5.0))
            bc[0][2] = N3(1.0, -sqrt(3.0 / 5.0))
            bc[1][1] = N2(1.0, 0.0)
            bc[1][2] = N3(1.0, 0.0)
            bc[2][1] = N2(1.0, sqrt(3.0 / 5.0))
            bc[2][2] = N3(1.0, sqrt(3.0 / 5.0))
        elif PC_count == 4:
            bc[0][1] = N2(1.0, -0.861136)
            bc[0][2] = N3(1.0, -0.861136)
            bc[1][1] = N2(1.0, -0.339981)
            bc[1][2] = N3(1.0, -0.339981)
            bc[2][1] = N2(1.0, 0.339981)
            bc[2][2] = N3(1.0, 0.339981)
            bc[3][1] = N2(1.0, 0.861136)
            bc[3][2] = N3(1.0, 0.861136)
        else:
            bc[0][1] = N2(1.0, -sqrt(1.0 / 3.0))
            bc[0][2] = N3(1.0, -sqrt(1.0 / 3.0))
            bc[1][1] = N2(1.0, sqrt(1.0 / 3.0))
            bc[1][2] = N3(1.0, sqrt(1.0 / 3.0))
    elif nrBoku == 2:
        if PC_count == 3:
            bc[0][2] = N3(sqrt(3.0 / 5.0), 1.0)
            bc[0][3] = N4(sqrt(3.0 / 5.0), 1.0)
            bc[1][2] = N3(0.0, 1.0)
            bc[1][3] = N4(0.0, 1.0)
            bc[2][2] = N3(-sqrt(3.0 / 5.0), 1.0)
            bc[2][3] = N4(-sqrt(3.0 / 5.0), 1.0)
        elif PC_count == 4:
            bc[0][2] = N3(0.861136, 1.0)
            bc[0][3] = N4(0.861136, 1.0)
            bc[1][2] = N3(0.339981, 1.0)
            bc[1][3] = N4(0.339981, 1.0)
            bc[2][2] = N3(-0.339981, 1.0)
            bc[2][3] = N4(-0.339981, 1.0)
            bc[3][2] = N3(-0.861136, 1.0)
            bc[3][3] = N4(-0.861136, 1.0)
        else:
            bc[0][2] = N3(sqrt(1.0 / 3.0), 1.0)
            bc[0][3] = N4(sqrt(1.0 / 3.0), 1.0)
            bc[1][2] = N3(-sqrt(1.0 / 3.0), 1.0)
            bc[1][3] = N4(-sqrt(1.0 / 3.0), 1.0)
    elif nrBoku == 3:
        if PC_count == 3:
            bc[0][0] = N1(-1.0, sqrt(3.0 / 5.0))
            bc[0][3] = N4(-1.0, sqrt(3.0 / 5.0))
            bc[1][0] = N1(-1.0, 0.0)
            bc[1][3] = N4(-1.0, 0.0)
            bc[2][0] = N1(-1.0, -sqrt(3.0 / 5.0))
            bc[2][3] = N4(-1.0, -sqrt(3.0 / 5.0))
        elif PC_count == 4:
            bc[0][0] = N1(-1.0, 0.861136)
            bc[0][3] = N4(-1.0, 0.861136)
            bc[1][0] = N1(-1.0, 0.339981)
            bc[1][3] = N4(-1.0, 0.339981)
            bc[2][0] = N1(-1.0, -0.339981)
            bc[2][3] = N4(-1.0, -0.339981)
            bc[3][0] = N1(-1.0, -0.861136)
            bc[3][3] = N4(-1.0, -0.861136)
        else:
            bc[0][0] = N1(-1.0, sqrt(1.0 / 3.0))
            bc[0][3] = N4(-1.0, sqrt(1.0 / 3.0))
            bc[1][0] = N1(-1.0, -sqrt(1.0 / 3.0))
            bc[1][3] = N4(-1.0, -sqrt(1.0 / 3.0))
    else:
        print("error - bcglobal")
    pc_temp = np.zeros(shape=(PC_count, 4, 4), dtype=float)
    pc_temp2 = np.zeros(shape=(4, 4), dtype=float)
    for k in range(PC_count):
        for i in range(4):
            for j in range(4):
                pc_temp[k][i][j] = w[k] * con * bc[k][i] * bc[k][j] * det
    for i in range(4):
        for j in range(4):
            for k in range(PC_count):
                pc_temp2[i][j] += pc_temp[k][i][j]
    return pc_temp2


def ID(ID, xx):
    if xx == 4:
        ID[0][0] = -sqrt(3.0 / 7.0 + 2.0 / 7.0 * sqrt(6.0 / 5.0))
        ID[0][1] = -1.0
        ID[1][0] = -sqrt(3.0 / 7.0 - 2.0 / 7.0 * sqrt(6.0 / 5.0))
        ID[1][1] = -1.0
        ID[2][0] = sqrt(3.0 / 7.0 - 2.0 / 7.0 * sqrt(6.0 / 5.0))
        ID[2][1] = -1.0
        ID[3][0] = sqrt(3.0 / 7.0 + 2.0 / 7.0 * sqrt(6.0 / 5.0))
        ID[3][1] = -1.0
        ID[4][0] = 1.0
        ID[4][1] = -sqrt(3.0 / 7.0 + 2.0 / 7.0 * sqrt(6.0 / 5.0))
        ID[5][0] = 1.0
        ID[5][1] = -sqrt(3.0 / 7.0 - 2.0 / 7.0 * sqrt(6.0 / 5.0))
        ID[6][0] = 1.0
        ID[6][1] = sqrt(3.0 / 7.0 - 2.0 / 7.0 * sqrt(6.0 / 5.0))
        ID[7][0] = 1.0
        ID[7][1] = sqrt(3.0 / 7.0 + 2.0 / 7.0 * sqrt(6.0 / 5.0))
        ID[8][0] = sqrt(3.0 / 7.0 + 2.0 / 7.0 * sqrt(6.0 / 5.0))
        ID[8][1] = 1.0
        ID[9][0] = sqrt(3.0 / 7.0 - 2.0 / 7.0 * sqrt(6.0 / 5.0))
        ID[9][1] = 1.0
        ID[10][0] = -sqrt(3.0 / 7.0 - 2.0 / 7.0 * sqrt(6.0 / 5.0))
        ID[10][1] = 1.0
        ID[11][0] = -sqrt(3.0 / 7.0 + 2.0 / 7.0 * sqrt(6.0 / 5.0))
        ID[11][1] = 1.0
        ID[12][0] = -1.0
        ID[12][1] = sqrt(3.0 / 7.0 + 2.0 / 7.0 * sqrt(6.0 / 5.0))
        ID[13][0] = -1.0
        ID[13][1] = sqrt(3.0 / 7.0 - 2.0 / 7.0 * sqrt(6.0 / 5.0))
        ID[14][0] = -1.0
        ID[14][1] = -sqrt(3.0 / 7.0 - 2.0 / 7.0 * sqrt(6.0 / 5.0))
        ID[15][0] = -1.0
        ID[15][1] = -sqrt(3.0 / 7.0 + 2.0 / 7.0 * sqrt(6.0 / 5.0))
    elif xx == 3:
        ID[0][0] = -sqrt(3.0 / 5.0)
        ID[0][1] = -1.0
        ID[1][0] = 0.0
        ID[1][1] = -1.0
        ID[2][0] = sqrt(3.0 / 5.0)
        ID[2][1] = -1.0
        ID[3][0] = 1.0
        ID[3][1] = -sqrt(3.0 / 5.0)
        ID[4][0] = 1.0
        ID[4][1] = 0.0
        ID[5][0] = 1.0
        ID[5][1] = sqrt(3.0 / 5.0)
        ID[6][0] = -sqrt(3.0 / 5.0)
        ID[6][1] = 1.0
        ID[7][0] = 0.0
        ID[7][1] = 1.0
        ID[8][0] = sqrt(3.0 / 5.0)
        ID[8][1] = 1.0
        ID[9][0] = -1.0
        ID[9][1] = -sqrt(3.0 / 5.0)
        ID[10][0] = -1.0
        ID[10][1] = 0.0
        ID[11][0] = -1.0
        ID[11][1] = sqrt(3.0 / 5.0)
    else:
        ID[0][0] = -sqrt(1.0 / 3.0)
        ID[0][1] = -1.0
        ID[1][0] = sqrt(1.0 / 3.0)
        ID[1][1] = -1.0
        ID[2][1] = -sqrt(1.0 / 3.0)
        ID[2][0] = 1.0
        ID[3][1] = sqrt(1.0 / 3.0)
        ID[3][0] = 1.0
        ID[4][0] = -sqrt(1.0 / 3.0)
        ID[4][1] = 1.0
        ID[5][0] = sqrt(1.0 / 3.0)
        ID[5][1] = 1.0
        ID[6][1] = -sqrt(1.0 / 3.0)
        ID[6][0] = 1.0
        ID[7][1] = sqrt(1.0 / 3.0)
        ID[7][0] = 1.0


def Pl(P, Tot, PC_count, nr, det, alfa):
    if PC_count == 3:
        w = np.zeros(shape=3)
        w[0] = 5.0 / 9.0
        w[1] = 8.0 / 9.0
        w[2] = 5.0 / 9.0
    elif PC_count == 4:
        w = np.zeros(shape=4)
        w[0] = 0.347855
        w[1] = 0.652145
        w[2] = 0.652145
        w[3] = 0.347855
    else:
        w = np.zeros(shape=2)
        w[0] = 1.0
        w[1] = 1.0
    bc = np.zeros(shape=(PC_count, 4), dtype=float)
    if nr == 0:
        if PC_count == 3:
            bc[0][0] = N1(-sqrt(3.0 / 5.0), -1.0)
            bc[0][1] = N2(-sqrt(3.0 / 5.0), -1.0)
            bc[1][0] = N1(0.0, -1.0)
            bc[1][1] = N2(0.0, -1.0)
            bc[2][0] = N1(sqrt(3.0 / 5.0), -1.0)
            bc[2][1] = N2(sqrt(3.0 / 5.0), -1.0)
        elif PC_count == 4:
            bc[0][0] = N1(-0.861136, -1.0)
            bc[0][1] = N2(-0.861136, -1.0)
            bc[1][0] = N1(-0.339981, -1.0)
            bc[1][1] = N2(-0.339981, -1.0)
            bc[2][0] = N1(0.339981, -1.0)
            bc[2][1] = N2(0.339981, -1.0)
            bc[3][0] = N1(0.861136, -1.0)
            bc[3][1] = N2(0.861136, -1.0)
        else:
            bc[0][0] = N1(-sqrt(1.0 / 3.0), -1.0)
            bc[0][1] = N2(-sqrt(1.0 / 3.0), -1.0)
            bc[1][0] = N1(sqrt(1.0 / 3.0), -1.0)
            bc[1][1] = N2(sqrt(1.0 / 3.0), -1.0)
    elif nr == 1:
        if PC_count == 3:
            bc[0][1] = N2(1.0, -sqrt(3.0 / 5.0))
            bc[0][2] = N3(1.0, -sqrt(3.0 / 5.0))
            bc[1][1] = N2(1.0, 0.0)
            bc[1][2] = N3(1.0, 0.0)
            bc[2][1] = N2(1.0, sqrt(3.0 / 5.0))
            bc[2][2] = N3(1.0, sqrt(3.0 / 5.0))
        elif PC_count == 4:
            bc[0][1] = N2(1.0, -0.861136)
            bc[0][2] = N3(1.0, -0.861136)
            bc[1][1] = N2(1.0, -0.339981)
            bc[1][2] = N3(1.0, -0.339981)
            bc[2][1] = N2(1.0, 0.339981)
            bc[2][2] = N3(1.0, 0.339981)
            bc[3][1] = N2(1.0, 0.861136)
            bc[3][2] = N3(1.0, 0.861136)
        else:
            bc[0][1] = N2(1.0, -sqrt(1.0 / 3.0))
            bc[0][2] = N3(1.0, -sqrt(1.0 / 3.0))
            bc[1][1] = N2(1.0, sqrt(1.0 / 3.0))
            bc[1][2] = N3(1.0, sqrt(1.0 / 3.0))
    elif nr == 2:
        if PC_count == 3:
            bc[0][2] = N3(-sqrt(3.0 / 5.0), 1.0)
            bc[0][3] = N4(-sqrt(3.0 / 5.0), 1.0)
            bc[1][2] = N3(0.0, 1.0)
            bc[1][3] = N4(0.0, 1.0)
            bc[2][2] = N3(sqrt(3.0 / 5.0), 1.0)
            bc[2][3] = N4(sqrt(3.0 / 5.0), 1.0)
        elif PC_count == 4:
            bc[0][0] = N1(-1.0, 0.861136)
            bc[0][3] = N4(-1.0, 0.861136)
            bc[1][0] = N1(-1.0, 0.339981)
            bc[1][3] = N4(-1.0, 0.339981)
            bc[2][0] = N1(-1.0, -0.339981)
            bc[2][3] = N4(-1.0, -0.339981)
            bc[3][0] = N1(-1.0, -0.861136)
            bc[3][3] = N4(-1.0, -0.861136)
        else:
            bc[0][2] = N3(sqrt(1.0 / 3.0), 1.0)
            bc[0][3] = N4(sqrt(1.0 / 3.0), 1.0)
            bc[1][2] = N3(-sqrt(1.0 / 3.0), 1.0)
            bc[1][3] = N4(-sqrt(1.0 / 3.0), 1.0)
    elif nr == 3:
        if PC_count == 3:
            bc[0][0] = N1(-1.0, sqrt(3.0 / 5.0))
            bc[0][3] = N4(-1.0, sqrt(3.0 / 5.0))
            bc[1][0] = N1(-1.0, 0.0)
            bc[1][3] = N4(-1.0, 0.0)
            bc[2][0] = N1(-1.0, -sqrt(3.0 / 5.0))
            bc[2][3] = N4(-1.0, -sqrt(3.0 / 5.0))
        elif PC_count == 4:
            bc[0][0] = N1(-1.0, 0.861136)
            bc[0][3] = N4(-1.0, 0.861136)
            bc[1][0] = N1(-1.0, 0.339981)
            bc[1][3] = N4(-1.0, 0.339981)
            bc[2][0] = N1(-1.0, -0.339981)
            bc[2][3] = N4(-1.0, -0.339981)
            bc[3][0] = N1(-1.0, -0.861136)
            bc[3][3] = N4(-1.0, -0.861136)
        else:
            bc[0][0] = N1(-1.0, sqrt(1.0 / 3.0))
            bc[0][3] = N4(-1.0, sqrt(1.0 / 3.0))
            bc[1][0] = N1(-1.0, -sqrt(1.0 / 3.0))
            bc[1][3] = N4(-1.0, -sqrt(1.0 / 3.0))
    else:
        print("error-p_local")
    for i in range(4):
        for j in range(PC_count):
            P[i] += alfa * Tot * w[j] * bc[j][i] * det


def Gauss(P, H, T, NodesNumber):
    THP = np.zeros(shape=(NodesNumber, (NodesNumber + 1)), dtype=float)#dekomponowanie petli
    for i in range(NodesNumber):
        T[i] = 0.0
        for j in range(NodesNumber + 1):
            if j == NodesNumber:
                THP[i][j] = P[i]
            else:
                THP[i][j] = H[i][j]
    #np.nozeros?
    #numpy special matrix functions?
    for i in range(NodesNumber):
        for j in range(i + 1, NodesNumber):
            if abs(THP[i][i]) < abs(THP[j][i]):
                for k in range(NodesNumber + 1):
                    THP[i][k] = THP[i][k] + THP[j][k]
                    THP[j][k] = THP[i][k] - THP[j][k]
                    THP[i][k] = THP[i][k] - THP[j][k]
    for i in range(NodesNumber - 1):
        for j in range(i + 1, NodesNumber):
            f = THP[j][i] / THP[i][i]
            for k in range(NodesNumber + 1):
                THP[j][k] -= f * THP[i][k]
    for i in range(NodesNumber - 1, -1, -1):
        T[i] = THP[i][NodesNumber]
        for j in range(i + 1, NodesNumber):
            if i != j:
                T[i] -= THP[i][j] * T[j]
        T[i] = T[i] / THP[i][i]
