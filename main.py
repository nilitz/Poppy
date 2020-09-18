import numpy as np
import math


def matrice_norm():
    m = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    return m;


def matrice_rx(alpha):
    rx = np.array([[1, 0, 0], [0, math.cos(alpha), -math.sin(alpha)], [0, math.sin(alpha), math.cos(alpha)]])
    return rx;


def matrice_ry(alpha):
    ry = np.array([[math.cos(alpha), 0, math.sin(alpha)], [0, 1, 0], [-math.sin(alpha), 0, math.cos(alpha)]])
    return ry;


def matrice_rz(alpha):
    rz = np.array([[math.cos(alpha), - math.sin(alpha), 0], [math.sin(alpha), math.cos(alpha), 0], [0, 0, 1]])
    return rz;



print('le plan (x,z) est le plan "base" du robot, l axe y est orthogonal au plan (x,z)')

def mouvement(m1, m2, m3, m4, m5):
    m1 = math.radians(m1)
    m2 = math.radians(m2)
    m3 = math.radians(m3)
    m4 = math.radians(m4)
    m5 = math.radians(m5)

    v1 = np.array([0, 1, 0])  # Rotation sur norm
    v2 = np.array([0, 1, 0])  # Rotation sur l'axe Y
    v3 = np.array([0, 1, 0])  # Rotation sur l'axe Z
    v4 = np.array([0, 1, 0])  # Rotation sur l'axe Z
    v5 = np.array([1, 0.25, 0])  # Rotation sur l'axe Y
    v6 = np.array([2, 0, 0])  # Rotation sur l'axe Z

    robot = [{'vector': v1, 'rotation': matrice_norm()}, {'vector': v2, 'rotation': matrice_ry(m1)},
             {'vector': v3, 'rotation': matrice_rz(m2)}, {'vector': v4, 'rotation': matrice_rz(m3)},
             {'vector': v5, 'rotation': matrice_ry(m4)}, {'vector': v6, 'rotation': matrice_rz(m5)}]

    position = np.array([0, 0, 0])


    for i in range(0, len(robot)):
        for j in range(i, len(robot)):
            robot[j]['vector'] = np.dot(robot[j]['vector'], robot[i]['rotation'])

    for k in range(0, len(robot)):
        position = position + robot[k]['vector']

    print(
        'vecteur position (x; y; z) : (' + str(round(position[0], 2)) + '; ' + str(round(position[1], 2)) + '; ' + str(
            round(position[2], 2)) + ')')


mouvement(90, 0, 0, 0, 0)