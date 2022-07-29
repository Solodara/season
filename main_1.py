# Програма, що за номером місяця виводить пору року
def season(x):
    if 3 <= x <= 5:
        return('spring')
    elif 6 <= x <= 8:
        return('summer')
    elif 9 <= x <= 11:
        return('autumn')
    else:
        return('winter')

months = int(input('введіть номер місяцю(числом): '))
if 1 <= months <= 12:
    print(season(months))
else:
    print('неправильно введено порядковий номер місяцю')