import Global_data
from math import sqrt
import Constant_values
import numpy as np
import Matrix

######################################################################################
#                                                                                    #
#                           Global Values for Main loop                              #
#                                                                                    #
######################################################################################

Tksi = np.zeros(shape=(Global_data.x, 4), dtype=float)
Teta = np.zeros(shape=(Global_data.x, 4), dtype=float)
C_pc = np.zeros(shape=(Global_data.x, 4), dtype=float)
wagi = np.zeros(shape=(Global_data.x), dtype=float)
H = np.zeros(shape=(Global_data.x, 4, 4), dtype=float)
P = np.zeros(shape=(Global_data.grid["nN"]), dtype=float)
C = np.zeros(shape=(Global_data.grid["nN"], Global_data.grid["nN"]), dtype=float)
AggregationArray = np.zeros(shape=(Global_data.grid["nN"], Global_data.grid["nN"]), dtype=float)
C_sum_pc = np.zeros(shape=(Global_data.x, 4, 4), dtype=float)

if (Global_data.x == 4):
    Constant_values.fill4(Tksi, Teta, C_pc, wagi)

if (Global_data.x == 9):
    Constant_values.fill9(Tksi, Teta, C_pc, wagi)

if (Global_data.x == 16):
    Constant_values.Fill16(Tksi, Teta, C_pc, wagi)


#if __name__='__main__'
#### Main loop
for i in range(Global_data.grid["nE"]):

    # temp for future convertion to function
    temp_ND = [Global_data.grid1.ND[Global_data.grid1.EL[i].ID[0] - 1],
               Global_data.grid1.ND[Global_data.grid1.EL[i].ID[1] - 1],
               Global_data.grid1.ND[Global_data.grid1.EL[i].ID[2] - 1],
               Global_data.grid1.ND[Global_data.grid1.EL[i].ID[3] - 1]]

    # declaration of local loop variables
    P_loc = np.zeros(shape=(4, 4), dtype=float)
    detJ_HBc = np.zeros(shape=4, dtype=float)
    t = np.zeros(shape=(Global_data.x, 4), dtype=float)
    detM = np.zeros(shape=(Global_data.x, 4), dtype=float)
    dndy = np.zeros(shape=(Global_data.x, 4), dtype=float)
    dndx = np.zeros(shape=(Global_data.x, 4), dtype=float)
    det = np.zeros(shape=(Global_data.x), dtype=float)
    H_global = np.zeros(shape=(4, 4), dtype=float)
    C_local = np.zeros(shape=(4, 4), dtype=float)

    detJ_HBc[0] = sqrt((temp_ND[1].x - temp_ND[0].x) * (temp_ND[1].x - temp_ND[0].x) + (temp_ND[1].y - temp_ND[0].y) * (
                temp_ND[1].y - temp_ND[0].y)) / 2
    detJ_HBc[1] = sqrt((temp_ND[2].x - temp_ND[1].x) * (temp_ND[2].x - temp_ND[1].x) + (temp_ND[2].y - temp_ND[1].y) * (
                temp_ND[2].y - temp_ND[1].y)) /2
    detJ_HBc[2] = sqrt((temp_ND[2].x - temp_ND[3].x) * (temp_ND[2].x - temp_ND[3].x) + (temp_ND[2].y - temp_ND[3].y) * (
                temp_ND[2].y - temp_ND[3].y)) /2
    detJ_HBc[3] = sqrt((temp_ND[3].x - temp_ND[0].x) * (temp_ND[3].x - temp_ND[0].x) + (temp_ND[3].y - temp_ND[0].y) * (
                temp_ND[3].y - temp_ND[0].y)) /2

    for j in range(0, 4):
        Global_data.grid1.EL[i].bok[j].pC = Global_data.xx
        Matrix.ID(Global_data.grid1.EL[i].bok[j].ID, Global_data.xx)

    if temp_ND[0].BC == 1 and temp_ND[1].BC == 1: # boundary condition on side no.0
        Global_data.grid1.EL[i].bok[0].pCValue = Matrix.BC(0, Global_data.xx,
                                                           detJ_HBc[0],
                                                           Global_data.global_data['alfa'])
        Matrix.Pl(P_loc[0], Global_data.global_data['tot'], Global_data.xx, 0, detJ_HBc[0],
                  Global_data.global_data['alfa'])

    if temp_ND[1].BC == 1 and temp_ND[2].BC == 1:  # boundary condition on side no.1
        Global_data.grid1.EL[i].bok[1].pCValue = Matrix.BC(1, Global_data.xx,
                                                           detJ_HBc[1],
                                                           Global_data.global_data['alfa'])
        Matrix.Pl(P_loc[1], Global_data.global_data['tot'], Global_data.xx, 1, detJ_HBc[1],
                  Global_data.global_data['alfa'])

    if temp_ND[2].BC == 1 and temp_ND[3].BC == 1: # boundary condition on side no.2
        Global_data.grid1.EL[i].bok[2].pCValue = Matrix.BC(2, Global_data.xx,
                                                           detJ_HBc[2],
                                                           Global_data.global_data['alfa'])
        Matrix.Pl(P_loc[2], Global_data.global_data['tot'], Global_data.xx, 2, detJ_HBc[2],
                  Global_data.global_data['alfa'])

    if temp_ND[3].BC == 1 and temp_ND[0].BC == 1:  # boundary condition on side no.3
        Global_data.grid1.EL[i].bok[3].pCValue = Matrix.BC(3, Global_data.xx,
                                                           detJ_HBc[3],
                                                           Global_data.global_data['alfa'])
        Matrix.Pl(P_loc[3], Global_data.global_data['tot'], Global_data.xx, 3, detJ_HBc[3],
                  Global_data.global_data['alfa'])

    for k in range(4):
        for j in range(4):
            P[Global_data.grid1.EL[i].ID[k] - 1] += P_loc[k][j]


    for j in range(0, 4):
        for k in range(0, 4):
            for q in range(0, 4):
                Global_data.grid1.EL[i].HBC[k][j] += Global_data.grid1.EL[i].bok[q].pCValue[k][j]

    Matrix.TMatrix(t, temp_ND, Tksi, Teta, Global_data.x)

    for z in range(Global_data.x):
        det[z] = (t[z][0] * t[z][3]) - (t[z][1] * t[z][2])

    for z in range(0, Global_data.x):
        if det[z] != 0:
            detM[z][0] = t[z][3] / det[z]
            detM[z][1] = -t[z][2] / det[z]
            detM[z][2] = -t[z][1] / det[z]
            detM[z][3] = t[z][0] / det[z]

    for j in range(Global_data.x):
        for z in range(4):
            dndx[j][z] = detM[j][0] * Tksi[j][z] + detM[j][2] * Teta[j][z]
            dndy[j][z] = detM[j][1] * Tksi[j][z] + detM[j][3] * Teta[j][z]

    for a in range(Global_data.x):
        print("\n\nH matrix for element no:" + str(a + 1) + "]\n")
        for j in range(4):
            for k in range(4):
                H[a][j][k] = float(Global_data.global_data['conductivity']) * (
                            (dndx[a][j] * dndx[a][k]) + (dndy[a][j] * dndy[a][k])) * det[a] * wagi[a]
                C_sum_pc[a][j][k] = float(Global_data.global_data['density']) * float(
                    Global_data.global_data['specifiheat']) * (C_pc[a][j] * C_pc[a][k]) * det[a] * wagi[a]
                print(H[a][j][k], end=" ")
            print()

    print("H matrix")
    for k in range(Global_data.x):
        H_global += H[k]


    print("C matrix")
    for k in range(Global_data.x):
        C_local += C_sum_pc[k]  # * w


    for k in range(0, 4):
        for j in range(0, 4):
            AggregationArray[(int(Global_data.grid1.EL[i].ID[k]) - 1)][(int(Global_data.grid1.EL[i].ID[j]) - 1)] += (
                        H_global[k][j] + Global_data.grid1.EL[i].HBC[k][j])
            C[(int(Global_data.grid1.EL[i].ID[k]) - 1)][(int(Global_data.grid1.EL[i].ID[j]) - 1)] += C_local[k][j]


###################################################################################
#                                                                                 #
#                        Printing out final solution                              #
#                                                                                 #
###################################################################################

print("\n\nAggregation -  H + Hbc:\n")
for i in range(Global_data.grid["nN"]):
    for j in range(Global_data.grid["nN"]):
        print(AggregationArray[i][j], end="  ")
    print()

print("\n\nP vector:")
print(P)

print("Final C matrix")
for i in range(Global_data.grid["nN"]):
    for j in range(Global_data.grid["nN"]):
        print(C[i][j], end="  ")
    print()

################################################################################################
#                                                                                              #
#                     Support arrays for final temperature calculations                        #
#                                                                                              #
################################################################################################

T = np.zeros(shape=(Global_data.grid["nN"]), dtype=float)
T0 = np.full(shape=(Global_data.grid["nN"]), fill_value=Global_data.global_data['initialtemp'], dtype=float)
T1 = np.zeros(shape=(Global_data.grid["nN"]), dtype=float)
Temp_H_and_P = np.zeros(shape=(Global_data.grid["nN"], Global_data.grid["nN"] + 1), dtype=float)
H_C_dT = np.zeros(shape=(Global_data.grid["nN"], Global_data.grid["nN"]), dtype=float)
C_T0_dT_P = np.zeros(shape=(Global_data.grid["nN"]), dtype=float)

for i in range(Global_data.grid["nN"]):
    for j in range(Global_data.grid["nN"]):
        H_C_dT[i][j] = AggregationArray[i][j] + (C[i][j] / int(Global_data.Step_Time))  # H + C/dT


#Calculating the T vector
# Matrix.Gauss(P, AggregationArray, T, Global_data.grid["nN"])
# print("T Vector", T)



print("\n\nTemperature in time:\n")
for s in range(int(int(Global_data.Simulation_time) / int(Global_data.Step_Time))):
    for i in range(Global_data.grid["nN"]):
        C_T0_dT_P[i] = P[i]
        for j in range(Global_data.grid["nN"]):
            C_T0_dT_P[i] += (C[i][j] / int(Global_data.Step_Time) * T0[j])  #wektor P
    Matrix.Gauss(C_T0_dT_P, H_C_dT, T1, Global_data.grid["nN"])



    min_val_of_T1 = T1[0]
    max_val_of_T1 = T1[0]
    T0[0] = T1[0]

    if np.max(T1) > max_val_of_T1:
        max_val_of_T1 = np.max(T1)
    if T1[j] < np.min(T1):
        min_val_of_T1 = np.min(T1)
    T0=T1
    #insted of print use logger
    print("in point(of time) " + str((s + 1) * int(Global_data.Step_Time)) + " \tLowest temperature: " + str(
        min_val_of_T1) + "\t Highest temperature:" + str(max_val_of_T1) + "\n")
