import matplotlib.pyplot as plt
from lagmodels import MaterialBody
from lagmodels import MaterialPoint
import math as m
import numpy as np

# функция для создания тела
def create_body():
    def get_Materialpoints(points,C1,C2):
        MatPoints = []
        
        
        for prt in range(1, 3):
            for prt2 in range(1, 3):
                for i in range(0, points):
                    for j in range(0, points):
                        A1 = C1 + (-1)**prt * 2 / points * i
                        A2 = C2 + (-1)**(prt2) * 2 / points * j

                        M = MaterialPoint(A1, A2, 0, 0,0,0,[],[])
                        MatPoints.append(M)
                        
                       

            return MatPoints
    MatBody = MaterialBody( -2.5,2.5,3,get_Materialpoints(3,-2,2))

    return MatBody


def integ(steps, y0, x0, xf, f):
    step = (xf - x0) / steps

    Yd = {'y 0': y0}

    x = x0

    X = [x]
    for i in range(1, steps):
        x = x + step
        X.append(x)
        yn = Yd['y ' + str(i - 1)]
        y = yn + step * 1 / 2 * f(x) * yn
        Yd.update({'y ' + str(i): y})
    Y = []
    for i in Yd.keys():
        Y.append(Yd[i])
    return Y, X
def trajctory(steps,t0,tf,X1,X2):
    def f1(x):
        try:
            f =  -m.log(x+1)
            return f
        except Exception:
            f = 0
            return f
    def f2(x):
        f = x
        return f

    x1,T = integ(steps,X1,t0,tf,f1)
    x2,T = integ(steps,X2,t0,tf,f2)
    x1f = x1[len(x1)-1]
    x2f = x1[len(x2)-1]
    v1 = f1(x1f)
    v2 = f2(x2f)
    return  x1,x2,x1f,x2f,v1,v2
# движение материального тела

def move_material_body (MatBody):
    for i in MatBody.Points:
        T1, T2, x1, x2, v1, v2 = trajctory(100,0,2,i.X1,i.X2)
        i.x1 = x1
        i.x2 = x2
        i.v1 = v1
        i.v2 = x2
        i.T1 = T1
        i.T2 = T2

        OX1 = np.zeros(1000)
        OY1 = np.linspace(-10, 10, 1000)
        OY2 = np.zeros(1000)
        OX2 = np.linspace(-10, 10, 1000)
        plt.Figure(figsize=(2, 2))
        plt.ylim(ymin=-10, ymax=10, auto=False)
        plt.xlim(xmin=-10, xmax=10, auto=False)


        for i in MatBody.Points:
            plt.scatter(i.X1, i.X2)
            plt.plot(i.T1, i.T2)
        plt.plot(OX1, OY1, c='b')
        plt.plot(OX2, OY2, c='b')

    return MatBody
