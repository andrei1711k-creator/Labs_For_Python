
class BankAccount:
    def __init__(self, client: 'Client', currency: str):
        self.client = client
        self.currency = currency
        self.balance = 0.0

    def top_up(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")
        self.balance -= amount
        return self.balance

    def transfer_to(self, to_account: 'BankAccount', amount: float):
        if self.currency != to_account.currency:
            raise ValueError("Перевод возможен только между счетами в одной валюте")

        if self == to_account:
            raise ValueError("Нельзя переводить деньги на тот же счет")
        self.withdraw(amount)
        to_account.top_up(amount)

    def get_info(self) -> str:
        balance = self.balance if self.balance is not None else 0.0
        return f"Счет ({self.currency}): {balance:.2f}"

class Client:
    def __init__(self, surname: str, name: str, otchestvo: str, passport: str):
        self.surname = surname.capitalize()
        self.name = name.capitalize()
        self.otchestvo = otchestvo.capitalize()
        self.passport = passport.upper()
        self.accounts: dict[str, BankAccount] = {}

        self._val_data()

    def _val_data(self):
        if not self.surname.isalpha():
            raise ValueError("Фамилия должна состоять только из букв")
        if not self.name.isalpha():
            raise ValueError("Имя должно состоять только из букв")
        if not self.otchestvo.isalpha():
            raise ValueError("Отчество должно состоять только из букв")
        if len(self.passport) != 9:
            raise ValueError("Номер паспорта должен состоять из 9 символов")
        if not (self.passport[:2].isalpha() and self.passport[2:].isdigit()):
            raise ValueError("Паспорт должен содержать 2 буквы и 7 цифр")


class Bank:
    def __init__(self):
        self.clients: dict[str, Client] = {}
        self.allowed_currencies = ["EUR", "USD", "BYN", "RUB"]

    def register_client(self, surname: str, name: str, otchestvo: str, passport: str) -> Client:
        if passport in self.clients:
            raise ValueError("Клиент с таким паспортом уже зарегистрирован")

        client = Client(surname, name, otchestvo, passport)
        self.clients[passport] = client
        return client

    def find_client(self, passport: str) -> Client | None:
        return self.clients.get(passport)

    def open_account(self, client_passport: str, currency: str) -> BankAccount:
        client = self.find_client(client_passport)
        if not client:
            raise ValueError("Клиент не найден")

        currency = currency.upper()
        if currency not in self.allowed_currencies:
            raise ValueError(f"Доступные валюты: {', '.join(self.allowed_currencies)}")

        if currency in client.accounts:
            raise ValueError(f"Счет в валюте {currency} уже существует")

        new_account = BankAccount(client, currency)
        client.accounts[currency] = new_account
        return new_account

    def close_account(self, client_passport: str, currency: str):
        client = self.find_client(client_passport)
        if not client:
            raise ValueError("Клиент не найден")

        currency = currency.upper()
        if currency not in client.accounts:
            raise ValueError("Счет не найден")

        account = client.accounts[currency]
        if account.balance > 0:
            raise ValueError("Нельзя закрыть счет с положительным балансом")

        del client.accounts[currency]

    def top_up_account(self, client_passport: str, currency: str, amount: float) -> float:
        client = self.find_client(client_passport)
        if not client:
            raise ValueError("Клиент не найден")

        currency = currency.upper()
        if currency not in client.accounts:
            raise ValueError("Счет не найден")

        return client.accounts[currency].top_up(amount)

    def withdraw_from_account(self, client_passport: str, currency: str, amount: float) -> float:
        client = self.find_client(client_passport)
        if not client:
            raise ValueError("Клиент не найден")

        currency = currency.upper()
        if currency not in client.accounts:
            raise ValueError("Счет не найден")

        return client.accounts[currency].withdraw(amount)

    def transfer(self, from_client_passport: str, to_client_passport: str, currency: str, amount: float):
        from_client = self.find_client(from_client_passport)
        to_client = self.find_client(to_client_passport)
        if not from_client or not to_client:
            raise ValueError("Один из клиентов не найден")
        currency = currency.upper()
        if currency not in from_client.accounts:
            raise ValueError("Исходный счет не найден")
        if currency not in to_client.accounts:
            raise ValueError("Целевой счет не найден")

        from_account = from_client.accounts[currency]
        to_account = to_client.accounts[currency]

        from_account.transfer_to(to_account, amount)

    def statement(self, client_passport: str, filename: str) :

        client = self.find_client(client_passport)
        if not client:
            raise ValueError("Клиент не найден")

        with open(filename, 'w', encoding='utf-8') as f:
            f.write("Выписка по счетам клиента\n")
            f.write(f"Клиент: {client.surname} {client.name} {client.otchestvo}\n")
            f.write(f"Паспорт: {client.passport}\n")
            f.write("=" * 50 + "\n\n")

            total_balance = 0.0

            for currency, account in client.accounts.items():
                f.write(f"{account.get_info()}\n")
                if currency == "EUR":
                    total_balance += account.balance * 3.5
                elif currency == "USD":
                    total_balance += account.balance * 3
                elif currency == "BYN":
                    total_balance += account.balance
                elif currency == "RUB":
                    total_balance += account.balance * 0.035
            f.write("\n" + "-" * 50 + "\n")
            f.write(f"Общий баланс в BYN: {total_balance:.2f}\n")



def interface():
    bank = Bank()



    bank.register_client("Иванов", "Иван", "Иванович", "AB1234567")
    bank.register_client("Петров", "Петр", "Петрович", "CD9876543")
    bank.open_account("AB1234567", "BYN")
    bank.open_account("AB1234567", "USD")
    bank.open_account("CD9876543", "BYN")


    while True:
        print("\n" + "=" * 100)
        print("БАНКОВСКАЯ СИСТЕМА")
        print("=" * 50)

        passport = input("Введите номер паспорта: ").upper()
        client = bank.find_client(passport)

        if not client:
            print("Клиент не найден. Хотите зарегистрироваться? (да/нет)")
            choice = input().lower()
            if choice == 'да':
                try:
                    surname = input("Фамилия: ")
                    name = input("Имя: ")
                    otchestvo = input("Отчество: ")
                    bank.register_client(surname, name, otchestvo, passport)
                    client = bank.find_client(passport)
                    print("Клиент успешно зарегистрирован!")
                except Exception as e:
                    print(f"Ошибка регистрации: {e}")
                    continue
            else:
                continue

        while True:
            print(f"\nДобро пожаловать, {client.surname} {client.name}!")
            print("Доступные операции:")
            print("1. Открыть счет")
            print("2. Закрыть счет")
            print("3. Пополнить счет")
            print("4. Снять со счета")
            print("5. Перевести деньги")
            print("6. Показать мои счета")
            print("7. Выписка по счетам ")
            print("8. Выйти из системы")

            choice = input("Выберите (1-8): ")

            try:
                if choice == '1':
                    available_currencies = []
                    for currency in bank.allowed_currencies:
                        if currency not in client.accounts:
                            available_currencies.append(currency)
                    if not available_currencies:
                        print("У вас уже открыты счета во всех доступных валютах")
                        continue

                    print(f"Доступные для открытия валюты: {', '.join(available_currencies)}")
                    currency = input("Введите валюту: ").upper()

                    if currency not in available_currencies:
                        print(f"Некорректная валюта или счет в этой валюте уже открыт")
                        continue

                    bank.open_account(passport, currency)
                    print(f"Счет в валюте {currency} открыт!")

                elif choice == '2':
                    if not client.accounts:
                        print("У вас нет открытых счетов")
                        continue

                    print("Ваши счета:")
                    for currency in client.accounts.keys():
                        print(f"  {currency}")

                    currency = input("Введите валюту счета для закрытия: ").upper()
                    bank.close_account(passport, currency)
                    print("Счет закрыт!")

                elif choice == '3':
                    if not client.accounts:
                        print("У вас нет открытых счетов")
                        continue

                    print("Ваши счета:")
                    for currency, account in client.accounts.items():
                        print(f"  {account.get_info()}")

                    currency = input("Введите валюту счета: ").upper()
                    amount = float(input("Введите сумму для пополнения: "))
                    new_balance = bank.top_up_account(passport, currency, amount)
                    print(f"Счет пополнен! Новый баланс: {new_balance:.2f}")

                elif choice == '4':
                    if not client.accounts:
                        print("У вас нет открытых счетов")
                        continue

                    print("Ваши счета:")
                    for currency, account in client.accounts.items():
                        print(f"  {account.get_info()}")

                    currency = input("Введите валюту счета: ").upper()
                    amount = float(input("Введите сумму для снятия: "))
                    new_balance = bank.withdraw_from_account(passport, currency, amount)
                    print(f"Снятие выполнено! Новый баланс: {new_balance:.2f}")

                elif choice == '5':
                    if not client.accounts:
                        print("У вас нет открытых счетов")
                        continue

                    print("Ваши счета:")
                    for currency, account in client.accounts.items():
                        print(f"  {account.get_info()}")

                    currency = input("Введите валюту перевода: ").upper()
                    to_passport = input("Введите паспорт получателя: ").upper()
                    amount = float(input("Введите сумму перевода: "))

                    bank.transfer(passport, to_passport, currency, amount)
                    print("Перевод выполнен!")

                elif choice == '6':
                    print("\nВаши счета:")
                    if not client.accounts:
                        print("  У вас нет открытых счетов")
                    else:
                        for currency, account in client.accounts.items():
                            print(f"  {account.get_info()}")

                elif choice == '7':
                    filename = f"выписка_{passport}.txt"
                    bank.statement(passport, filename)
                    print(f"Выписка сохранена в файл: {filename}")

                elif choice == '8':
                    return False

                else:
                    print("!!! только цифры от 1 до 10 !!!")

            except Exception as e:
                print(f"Ошибка: {e}")


if __name__ == "__main__":
    interface()

