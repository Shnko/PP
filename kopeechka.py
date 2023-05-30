kop = int(input("Введите количество копеек от 0 до 99: "))
if kop < 0 or kop > 99:
    print("это уже не копейки")
    exit()
else:
    if kop % 10 == 0:
        print("Денег нет")
        exit()
    if kop % 10 == 1:
        name = " копейка"
    if kop % 10 == 2 or 3 or 4:
        name = " копейки"
    if kop % 10 > 4:
        name = " копеек"
print(str(kop) + name)