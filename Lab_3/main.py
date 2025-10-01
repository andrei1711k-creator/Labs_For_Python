users = []
user ={}
class User():

    def __init__(self,surname:str,name:str,otchestvo:str,passport:str):

        self.surname =surname.capitalize()
        self.name = name.capitalize()
        self.otchestvo = otchestvo.capitalize()
        self.passport = passport.upper()

        if not self.surname.isalpha():
           raise TypeError ("Фамилия дожна состоять только из букв ")

        if not self.name.isalpha():
            raise TypeError("Фамилия дожна состоять только из букв ")

        if not self.otchestvo.isalpha():
            raise TypeError("Фамилия дожна состоять только из букв ")

        if len(self.passport) < 9:
            raise TypeError("Номер паспорта должен быть состоять минимум из 9 символов  ")
        elif self.passport.isalpha() or self.passport.isdigit():
            raise TypeError("Паспорт должен быть состоять из букв и цифр  ")
        elif not ((self.passport[0].isalpha()) and (self.passport[1].isalpha())):
            raise TypeError("Первые два символа номера паспорта буквы ")
        elif not (self.passport[2:].isdigit()) :
            raise TypeError("начиная с третьего символа номера паспорта все символы - цифры")

        user["Фамилия"] = self.surname
        user["Имя"] = self.name
        user["Очество"] = self.otchestvo
        user["Паспорт"] = self.passport

        users.append(user)


allowed_currency=["EUR","USD","BYN","RUB"]
scheta = []

schet={}
class schet_of_User():


    def __init__(self,currency:str,passport:str,count:int,percent:float):
        self.currency = currency
        self.passport = passport
        self.count = count
        self.percent = percent

        if not self.currency in allowed_currency:
            raise TypeError (f" у нас доступны только {allowed_currency}")
        schet["Валюта"] = self.currency
        schet["Паспорт"]= self.passport
        schet["Сумма"] = self.count
        schet["Процент"] = self.percent
        scheta.append(schet)
    def delete_schet(passpord):
        for schets in scheta:
            if schet["Паспорт"] == passpord:
                schets.remove(schet)
