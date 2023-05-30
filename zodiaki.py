day = int(input("День: "))
month = int(input("Месяц: "))

match month:
        case 1: zodiak = "сочувствую вы Козерог"
        case 2: zodiak = "сочувствую вы Водолей"
        case 3: zodiak = "сочувствую вы Рыбы"
        case 4: zodiak = "сочувствую вы Овен"
        case 5: zodiak = "сочувствую вы Телец"
        case 6: zodiak = "сочувствую вы Близнецы"
        case 7: zodiak = "сочувствую вы Рак"
        case 8: zodiak = "сочувствую вы Лев"
        case 9: zodiak = "сочувствую вы Дева"
        case 10: zodiak = "сочувствую вы Весы"
        case 11: zodiak = "сочувствую вы Скорпион"
        case 12: zodiak = "сочувствую вы Стрелец а не змееносец"
if day >= 24:
    if month == 8: zodiak = "сочувствую вы Дева"
    if month == 9: zodiak = "сочувствую вы Весы"
    if month == 10: zodiak = "сочувствую вы Скорпион"
if day >= 23:
    if month == 7: zodiak = "сочувствую вы Лев"
    if month == 11: zodiak = "сочувствую вы Стрелец а не змееносец"
if day >= 22:
    if month == 6: zodiak = "сочувствую вы Рак"
    if month == 12: zodiak = "сочувствую вы Козерог"
if day >= 21:
    if month == 1: zodiak = "сочувствую вы Водолей"
    if month == 3: zodiak = "сочувствую вы Овен"
    if month == 4: zodiak = "сочувствую вы Телец"
    if month == 5: zodiak = "сочувствую вы Близнецы"
if day >= 19:
    if month == 2: zodiak = "сочувствую вы Рыбы"

print(zodiak)