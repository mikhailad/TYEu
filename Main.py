#импорт модулей
import matplotlib.pyplot as plt
import lagmanagers as Lg#вызовем написанные модули
import Eulsermanagers as EU#
#Создадим материальное тело
create = Lg.create_body()
#двигаем материальное тело
move = Lg.move_material_body(create)
#Движение в пространстве
space = EU.Move_through_space()
plt.show()

