'''#1.3 Функции и стек вызовов
Напишите реализацию функции closest_mod_5, принимающую в качестве единственного аргумента целое число x и возвращающую самое маленькое целое число y, такое что:

y больше или равно x
y делится нацело на 5
Формат того, что ожидается от вас в качестве ответа:

def closest_mod_5(x):
    if x % 5 == 0:
        return x
    return "I don't know :("
    '''
    
    
    
def closest_mod_5(x):
	  return int((5 - (x % 5)) + x)
    
    
   #Не проходило, так как в принт вывод оборачивал!!!
