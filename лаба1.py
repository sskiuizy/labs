'''#Задание 1.1
print('Введите число:')
a1 = int(input())
for x in range(1, a1+1):
    print(x)


#Задание 1.2
print("Введите первое число:")    
a2 = int(input())
print("Введите второе число:")
b = int(input())
if a2 > b:
    print(a2)
else:
    print(b)'''



''';#Задание 2.1
def greet(name):
    print(f'Здравствуйте, {name}')
greet(input())'''


'''print("Введите число:")
def square(num):
    return num**2
print(square(int(input())))'''

'''print('Введите два числа')
x = int(input())
y = int(input())
def max_of_two(x,y):
    return x if x > y else y
print(max(x,y))'''


#Задание 2.2
'''def describe_person(name, age=30):
    return f'Имя: {name}, Возраст: {age}'
print(describe_person(input()))'''


#Задание 2.3

'''def is_prime(num):
    if num <= 1:
        return False
    if num >= 2:
        return True
print(is_prime(int(input())))'''

#Задание 3.1
with open('zxc.txt','r') as file:
    cont = file.read()
    print(cont)



    
    





