""""
Лабораторна робота №5: (Варіант 6)
Прізвище та ім'я: Шокур Марія
Група: 1

"""
import math
from typing import Callable   
x0=float(input("Введіть х0, яке задовольняє умову f(x0)∙f''(x0) > 0"))
history=[]
def func(x0: float) -> float:
    y=2*(x0**2)-(x0**4)-1-math.log(x0)
    return y

def dfunc(x0: float) -> float:
    dy = 4*x0-4*(x0**3)-1/x0
    return dy

def ddfunc(x0: float):
    ddy=4-12*(x0**2)+1/(x0**2)
    return ddy

def solve_newton(func:Callable[[float], float], dfunc:Callable[[float], float], ddfunc:Callable[[float], float], x0: float):
    eps = 0.00008
    step=1
    while func(x0)*ddfunc(x0) > 0:
        if dfunc(x0) == 0:
            print(f"Похідна дорівнює нулю і дотична горизонтальна, отже розв'язків немає")
            break
        x_next = x0 - func(x0)/dfunc(x0)
        history.append(( step, x_next))
        step+=1
        if abs(x_next - x0)< eps:
            root = x_next
            
        x0 = x_next
    return history

def saving_result( history, filename = "results_variant_06.txt" ):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Результати обчислень:\n")
        file.write("Таблиця з результатами:\n")
        file.write(f"{"Номер ітерації":>15} | {"Значення ітерації":<15}\n" )
        for step, x_next in history:
            file.write(f"{step:>15} | {x_next:<15.6f}\n" )
