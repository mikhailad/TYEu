from Eulermodels import Space_mesh
from Eulermodels import Space_point
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import numpy as np
import math as m


# Получим поле скоростей
def getfield(e11, e12, e21, e22, points_mesh, t):

    Mesh = Space_mesh(e11, e12, e21, e22, points_mesh)
    Points_space = []
    X1 = []
    X2 = []
    x1 = e11
    x2 = e21
    for i in range(0, points_mesh):
        X1.append(x1)
        x1 = x1 + abs((e11 - e12) / points_mesh)
        X2.append(x2)
        x2 = x2 + abs((e21 - e22) / points_mesh)

    def f1(x, t):
        f = -x * m.log(t + 1)
        return f

    def f2(x, t):
        f = x * t
        return f

    for i in range(0, len(X1)):
        for j in range(0, len(X1)):
            P = Space_point(X1[i], X2[j], f1(X1[i], t), f2(X2[j], t))
            Points_space.append(P)
    return Points_space, Mesh


# Движение сковозь пространство
def Move_through_space():
    # функции для скорости
    def f1(x, t):
        f = -x * m.log(t + 1)
        return f

    def f2(x, t):
        try:
            f = x * t
        except Exception:
            f = 0 * x * t
        return f

    # параметры сетки
    e11 = -10
    e12 = 0
    e21 = 0
    e22 = 10
    points_mesh = 10
    steps = 100
    lines = 10
    tfl = 1.5
    # количество временных точе
    ntp = 3
    plt.figure()
    # постороим линии тока
    for h in range(1, 2 * ntp + 1, 2):
        t = (tfl) / ntp * h
        SP, Mesh = getfield(e11, e12, e21, e22, points_mesh, t)
        dict1 = {}
        dict2 = {}

        for j in range(0, lines):
            X1l = []
            X2l = []
            x1 = e11
            x2 = e21 + abs(e22 - e21) / lines * j
            for i in range(0, steps):
                X1l.append(x1)
                X2l.append(x2)
                x2 += f2(x2, t) / f1(x1, t) * abs(e12 - e11) / steps
                x1 += abs(e12 - e11) / steps
            dict1.update({'dict1+' + str(j): X1l})
            dict2.update({'dict1+' + str(j): X2l})
        for j in range(0, lines):
            X1l = []
            X2l = []
            x1 = e11 + abs(e12 - e11) / lines * j
            if e21 != 0:
                x2 = e21
            else:
                x2 = e21 + 0.1

            for i in range(0, steps):
                X1l.append(x1)
                X2l.append(x2)
                try:
                    x2 += f2(x2, t) / f1(x1, t) * abs(e12 - e11) / steps
                    x1 += abs(e12 - e11) / steps
                except Exception:
                    pass
            dict1.update({'dict2+' + str(j): X1l})
            dict2.update({'dict2+' + str(j): X2l})
        n1 = []
        n2 = []
        x1 = e11
        x2 = e21
        for i in range(0, points_mesh):
            n1.append(x1)
            x1 = x1 + abs((e11 - e12) / points_mesh)
            n2.append(x2)
            x2 = x2 + abs((e21 - e22) / points_mesh)
        print(n1, n2)

        plt.subplot(2, ntp, h, aspect='equal')
        plt.title('t = ' + str(t))
        plt.ylim(ymin=0, ymax=10, auto=False)
        plt.xlim(xmin=-10, xmax=0, auto=False)
        # посторим поле скоростей
        for i in SP:
            plt.quiver(i.x1, i.x2, i.v1, i.v2, color='black')
            x, y = np.meshgrid(n1, n2)
        plt.plot(x, y)

        segs1 = np.stack((x, y), axis=2)
        segs2 = segs1.transpose(1, 0, 2)
        plt.gca().add_collection(LineCollection(segs1))
        plt.gca().add_collection(LineCollection(segs2))

        plt.subplot(2, ntp, h + 1, aspect='equal')
        plt.title('t = ' + str(t))
        for n in dict1.keys():
            plt.ylim(ymin=0, ymax=10, auto=False)
            plt.xlim(xmin=-10, xmax=0, auto=False)
            plt.plot(dict1[n], dict2[n])
