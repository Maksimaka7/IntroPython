Text_1 = 'Вітаю, я створений щоб порівняти ваші числа'
print(Text_1)
number_1 = int(input('Введіть перше число:'))
number_2 = int(input('Введіть друге число:'))
if (number_1)==(number_2):
    print(number_1,'=',number_2)
elif (number_1) > (number_2):
    print(number_1,'>',number_2)
elif (number_1) < (number_2):
    print(number_1,'<',number_2)
