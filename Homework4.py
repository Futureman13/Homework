

from datetime import datetime, timedelta
users = [
    {"name": "John Doe", "birthday": "1985.03.11"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Oleksii", "birthday": "1994.03.13"},
    {"name": 'Jiest', "birthday": "1994.03.16"}
]

# TODO 1 function
def users_list(users: list):
    prepared_users = []
    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'],'%Y.%m.%d').date()
            prepared_users.append({"name": user['name'], 'birthday': birthday})
        except ValueError:
            print(f'Не коректна дата народження для користувача{user["name"]}')
    return prepared_users

prepared_users = users_list(users)

#TODO 2 function
def find_next_weekday(d, weekday: int):
    days_ahead = weekday - d.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return d + timedelta(days=days_ahead)


#todo 3 function
def congratulation_list( prepared_users ):
    days = 7
    today = datetime.today().date()
    upcoming_birthdays = []
    for user in prepared_users:
        birthday_this_year = user["birthday"].replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if 0 <= (birthday_this_year - today).days <= days:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year = find_next_weekday(birthday_this_year, 0)

            congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
            upcoming_birthdays.append({ "name": user["name"],"congratulation_date": congratulation_date_str})
    return upcoming_birthdays
print(congratulation_list(prepared_users))