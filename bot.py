from classesBook import AddressBook,Record
from decorators import input_error,show_error,birthday_error

@input_error
def add_contact(args,book):
        name,phone = args
        if len(phone)<10:
            return 'Phone must be 10 digits'
        else:
            record = Record(name.lower())
            record.add_phone(phone)
            return book.add_record(record)

@input_error
def change_contact(args,book):
        name,old_phone,new_phone = args
        record = book.find(name)
        return record.edit_phone(old=old_phone,new=new_phone)

@show_error
def show_phone(args,book):
        name = args
        name = ("".join(name)).lower()
        record = book.find(name)
        return record.find_phone()

@birthday_error
def add_birthday(args,book):
        name, birthday = args
        record = book.find(name)
        return record.add_birthday(birthday)

@show_error
def show_birthday(args,book):
        name = args
        name = ("".join(name)).lower()
        record = book.find(name)
        return record.show_birthday()

@input_error
def birthdays(book):
    return book.get_birthdays_per_week()

def show_all(book):
    return book.__str__()


def parce_input(user_input):
    cmd,*args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd,*args

def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input('Enter a command: ')
        command,*args = parce_input(user_input)
        if command in ['close','exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args,book))
        elif command == 'change':
            print(change_contact(args,book))
        elif command == 'phone':
            print(show_phone(args,book))
        elif command == 'all':
            print(show_all(book))
        elif command == 'add-birthday':
            print(add_birthday(args,book))
        elif command == 'show-birthday':
            print(show_birthday(args,book))
        elif command == 'birthdays':
            dataBirthdays = birthdays(book)
            for day,name in dataBirthdays.items():
                print(f'{day}: {", ".join(name)}') 
        else: print('Invalid command.')

if __name__ == "__main__":
    main()