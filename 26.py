#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
def deg(A, B):
    if B == 0:
        return 1
    elif B == 1:
        return A
    else:
        return A * deg(A, B-1)

A = int(input("Введите число A: ")) 
B = int(input("Введите степень B: ")) 

result = deg(A, B)
print(f'{A} в степени {B} равно {result}')