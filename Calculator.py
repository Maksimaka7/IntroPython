Text_1 = 'Вітаємо в калькуляторі майбутнього'
print(Text_1)
Number_1 =int(input('Введіть перше число: '))
Number_2 = int(input('Введіть друге число: '))
oper = input('Оберіть одну із операцій +,-,*,/')
if oper == '+':
    print(Number_1+Number_2)
elif oper == '-':
    print(Number_1-Number_2)
elif oper == '*':
    print(Number_1*Number_2)
elif oper == '/':
    print(Number_1/Number_2)
else:
    print('error')