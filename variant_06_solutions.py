""""
Лабораторна робота №5: (Варіант 6)
Прізвище та ім'я: Шокур Марія
Група: 1

"""
import math
from typing import Callable   
def func(x0: float) -> float:
    y=2*(x0**2)-(x0**4)-1-math.log(x0)
    return y

def dfunc(x0: float) -> float:
    dy = 4*x0-4*(x0**3)-1/x0
    return dy

def solve_newton(func: Callable[[float], float], 
dfunc: Callable[[float], float], x0: float):
    eps = 0.00008
    history = []
    step = 1
    x_next = None
    
    while True:
        if dfunc(x0) == 0:
                print("Подальші обчислення зупинені, бо f'(x0)=0.")
                root = None
                return root, history
        x_next = x0 - func(x0)/dfunc(x0)
        history.append((step, x_next))
        step+=1
        if abs(x_next-x0) < eps:
            root = x_next
            return root, history
        x0 = x_next

def save_results(root: float, history, filename = "result_variant_06.txt"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write("Результати обчислень:\n")
        if root is not None:
            file.write(f"Корінь:{root:.6f}\n")
        file.write("Таблиця з результатами обчислень:\n")
        file.write(f"{'Номер ітерації':<15} | {'Значення ітерації':>11}\n") 
        for step, x_next in history:
            file.write(f"{      step:<15} | {x_next:>11.6f}\n")

def main():
    x0=float(input("Введіть х0, яке задовольняє умову f(x0)∙f''(x0) > 0:   "))
    root, history = solve_newton(func, dfunc, x0)
    save_results(root, history)
    print(f"Корінь рівняння дорівнює {root:.6f}, який був знайднений за  таку кількість ітерацій: {len(history)} ")

if __name__ == "__main__":
    main()

