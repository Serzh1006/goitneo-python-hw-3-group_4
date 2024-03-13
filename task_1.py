from collections import defaultdict
from datetime import datetime

users_birthday = [{"name":'Audrey Williams',"birthday":datetime(1974,3,17)},
{"name":'Anna Manning',"birthday":datetime(1996,3,5)},
{"name":'Alex Kravchenko',"birthday":datetime(1974,3,15)},
{"name":'Ray Green',"birthday":datetime(1986,3,10)},
{"name":'Joseph Porter',"birthday":datetime(1997,3,1)},
{"name":'Mary Nelson',"birthday":datetime(2000,7,15)},
{"name":'Annie White',"birthday":datetime(2001,3,1)},
{"name":'Susan Barker',"birthday":datetime(1991,3,2)},
{"name":'Chad Johnson',"birthday":datetime(1979,3,6)},
{"name":'Maria Simmons',"birthday":datetime(1993,3,3)},
{"name":'Theodore Davis',"birthday":datetime(1995,3,4)}]

def get_birthdays_per_week(users):
    users_list_for_birthday = defaultdict(list)
    today = datetime.today().date()
    for date in users:
        birthday = date['birthday'].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year+1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7:
            if birthday_this_year.weekday()==5 or birthday_this_year.weekday()==6:
                users_list_for_birthday['Monday'].append(date['name'])
            else:
                weekday = birthday_this_year.strftime('%A')
                users_list_for_birthday[weekday].append(date['name'])
    return users_list_for_birthday


result = get_birthdays_per_week(users_birthday)
for day,name in result.items():
    print(f'{day}: {", ".join(name)}') 


   