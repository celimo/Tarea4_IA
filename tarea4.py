import control as co
import numpy as np
import matplotlib.pyplot as plt

def fun_Tran(A):
    # A es el cromosoma con su estructura definida, arreglo de 15 espacios
    G1 = co.tf([A[0][0]], [A[1][0], A[1][0]*A[2][0], 0])
    G2 = co.tf([A[0][1], 0], [A[1][1], A[1][1]*A[2][1]+A[3][0]])
    G3 = co.tf([A[0][2], A[0][2]*A[2][2], 0], [A[1][2]])

    H1 = co.tf([A[4][0]*A[5][0], A[5][0]], [1])
    H2 = co.tf([A[4][1]*A[5][1], A[5][1], 0], [1])
    H3 = co.tf([A[5][2], 0], [1])

    num = G1*G2*G3 + G1*H1*G3
    den = 1 + G1*G2*G3 + G2*H2 + G2*H3 + H1*H3 + G1*H1*G3

    funct = num/den

    return funct

'''
Definición del cromosoma

Cromosoma = [[A1, A2, A3], [B1, B2, B3], [C1, C2, C3], [D2], [F1, F2], [K1, K2, K3]]

Definición del gen: Cada elemento del cromosoma es un vector con dimensiones variables


Alelos: Como primera aproximación se consideran valores entre -10 y 10
'''

Cm = []

Cm.append([1,2,3])
Cm.append([8,5,6])
Cm.append([7,8,9])
Cm.append([20])
Cm.append([11,12])
Cm.append([13,14,15])

sys = fun_Tran(Cm)

print(sys)

'''
t = np.linspace(0, 1000, 100000)
t1, y1 = co.step_response(sys, t)

plt.plot(t1, y1)
plt.grid()
plt.show()

mag, pha, frec = co.bode_plot(sys)

plt.show()

plt.plot(frec, mag)
plt.yscale('log')
plt.xscale('log')
plt.grid(True, which="both")
plt.show()

pha = np.array(pha)

pha = pha*180/(np.pi)

plt.plot(frec, pha)
plt.xscale('log')
plt.grid(True, which="both")
plt.show()
'''
