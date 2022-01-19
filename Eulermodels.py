#Создадим класс пространственная точка

class Space_point():
    def __init__(self, x1, x2, v1, v2):
        self.x1 = x1
        self.x2 = x2
        self.v1 = v1
        self.v2 = v2
# Создадим класс пространственная сетка
class Space_mesh():
    def __init__(self, e11, e12, e21, e22, points_mesh):
        self.e11 = e11
        self.e12 = e12
        self.e21 = e21
        self.e22 = e22
        self.points_mesh = points_mesh

