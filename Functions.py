class Contact:
    def __init__(self, name, surname, phone, favor=False, *args, **kwargs):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.favor = favor
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        print(f'Имя: {self.name}')
        print(f'Фамилия: {self.surname}')
        print(f'Телефон: {self.phone}')
        print(f'В избранных: {"да" if self.favor else "нет"}')
        print('Дополнительная информация:')
        if self.args:
            print('\t', *self.args)
        for key in self.kwargs:
            print(f'\t{key} : {self.kwargs[key]}')
        return ''

jhon = Contact('Jhon', 'Smith', '+71234567809', telegram ='@jhony', email='jhony@smith.com')
# print(jhon)

class PhoneBook:
    def __init__(self, book_name):
        self.contacts = {}
        self.book_name = book_name

    def add(self, name, surname, phone, favor=False, *args, **kwargs):
        self.contacts[name] = Contact(name, surname, phone, favor, *args, **kwargs)

    def output(self):
        print('Контакты:')
        for c in self.contacts:
            print(self.contacts[c])

    def delete(self, phone):
        for c in self.contacts:
            if phone == self.contacts[c].phone:
                del self.contacts[c]
                print('Контакт удален')
                return
        print('Контакт не найден')

    def favorite(self):
        for c in self.contacts:
            if self.contacts[c].favor:
                print('Избранные контакты:')
                print(self.contacts[c])

    def search(self, n, s):
        for c in self.contacts:
            if f'{n} {s}'== f'{self.contacts[c].name} {self.contacts[c].surname}':
                print(self.contacts[c])

book1 = PhoneBook('Рабочие контакты')

book1.add('Вася', 'Петров', '123456', email='petrov@ya.ru')
book1.add('Катя', 'Васина', '222222', telegram='katavasina')
book1.add('Тирион', 'Ланистер', '1111111', True, 'Карлик', skype='Tirya')

book1.delete('1234')
book1.favorite()
book1.output()
book1.search('Катя', 'Васина')