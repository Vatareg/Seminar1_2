def method_Task1():
    numOne = int(input("Введите первое число: "))
    numTwo = int(input("Введите второе число: "))
    if (numOne == numTwo * numTwo):
        print(f"{numOne} Является квадратом {numTwo}")
    elif (numTwo == numOne * numOne):
        print(f"{numTwo} Является квадратом {numOne}")
    else:
        print("Не являются квадратом")

#method_Task1()

def method_Task2():
    array = [1, 2, 3, 4, 5]
    max = 0
    for step in array:
        tond = int(array[step - 1])
        print(tond)
        if (tond > max):
            max = tond
    print(f"Максимальное значение = {max}")

#method_Task2()

def method_Task3():
    num = int(input("введите число для построения диапозона: "))
    for step in range(-num, num + 1, 1):
        print(step)

#method_Task3()

num = float(input("Введите дробное число: "))
num * 10