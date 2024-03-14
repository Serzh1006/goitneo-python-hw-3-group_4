from collections import UserDict,defaultdict
from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = ''

    def add_birthday(self,birthday):
        try:
            self.birthday = datetime.strptime(birthday, "%d.%m.%Y")
            return 'Birthday added'
        except ValueError:
            return "Format DD.MM.YYYY"
        
    def show_birthday(self):
        try:
            return self.birthday.strftime('%d.%m.%Y')
        except:
            return 'Not found'

    def add_phone(self,new_phone):
        phone = Phone(new_phone)
        self.phones.append(phone.value)

    def remove_phone(self,phone):
        self.phones.remove(phone)

    def edit_phone(self,old,new):
        index = self.phones.index(old)
        self.phones[index] = new
        return "Contact updated"

    def find_phone(self):
        return f"{'; '.join(p for p in self.phones)}"

    def __str__(self):
        return f"Contact name: {self.name.value.capitalize()}, phones: {'; '.join(p for p in self.phones)}{', birthday: ' + self.birthday.strftime('%d.%m.%Y') if self.birthday else ''}\n"

class AddressBook(UserDict):
    def add_record(self,record):
       self.data[record.name.value] = record
       return "Contact added."

    def find(self,name):
        return self.data[name]

    def delete(self,name):
        self.data.pop(name)
    
    def get_birthdays_per_week(self):
        users_list_for_birthday = defaultdict(list)
        today = datetime.today().date()
        for name,date in self.items():
            birthday_this_year = date.birthday.date().replace(year=today.year)
            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year+1)
            delta_days = (birthday_this_year - today).days
            if delta_days < 7:
                if birthday_this_year.weekday() in [5,6]:
                    users_list_for_birthday['Monday'].append(name)
                else:
                    weekday = birthday_this_year.strftime('%A')
                    users_list_for_birthday[weekday].append(name)
        return users_list_for_birthday
    
    def __str__(self):
        result = ''
        for key, value in self.data.items():
            result += f"Contact name: {key.capitalize()}, phones: {'; '.join(p for p in value.phones)}{', birthday: ' + value.birthday.strftime('%d.%m.%Y') if value.birthday else ''}\n"
        return result
