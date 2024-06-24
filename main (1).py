'''
25.11.2023 группа 31ИС-21
Васильева Ангелина Сергеевна
Создать на python класс Мопеу для работы с денежными суммами.
Число должно быть представлено двумя полями: типа long для рублей и типа unsigned char - для копеек.
Дробная часть (копейки) при выводе на экран должна быть отделена от целой части запятой.
Реализовать сложение, вычитание, деление сумм, деление суммы на дробное число, умножение на дробное число и операции сравнения.'''

class Money:
    def __init__(self, rubles, kopeks):
        self.rubles = rubles
        self.kopeks = kopeks

    def __repr__(self):
        return f'{self.rubles},{self.kopeks:02}'

    def __add__(self, other):
        rubles = self.rubles + other.rubles
        kopeks = self.kopeks + other.kopeks
        if kopeks >= 100:
            rubles += 1
            kopeks -= 100
        return Money(rubles, kopeks)

    def __sub__(self, other):
        rubles = self.rubles - other.rubles
        kopeks = self.kopeks - other.kopeks
        if kopeks < 0:
            rubles -= 1
            kopeks += 100
        return  Money(rubles, kopeks)

    def __truediv__(self, other):
        total_kopeks = self.rubles * 100 + self.kopeks
        divisor_kopeks = other.rubles * 100 + other.kopeks
        result_kopeks = total_kopeks / divisor_kopeks * 100
        return  Money(int(result_kopeks // 100), int(result_kopeks % 100))

    def __mul__(self, other):
        total_kopeks = self.rubles * 100 + self.kopeks
        result_kopeks = total_kopeks * other
        return  Money(int(result_kopeks // 100), int(result_kopeks % 100))

