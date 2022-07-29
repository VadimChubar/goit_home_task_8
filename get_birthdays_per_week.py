from datetime import datetime, timedelta

users = [
    {'name': 'Alex', 'birthday': datetime(year=1987, month=9, day=23)},
    {'name': 'Bella', 'birthday': datetime(year=1988, month=12, day=24)},
    {'name': 'Al', 'birthday': datetime(year=1990, month=7, day=25)},
    {'name': 'Barbara', 'birthday': datetime(year=2000, month=7, day=26)},
    {'name': 'Marcus', 'birthday': datetime(year=2001, month=7, day=26)},
    {'name': 'Jack', 'birthday': datetime(year=1987, month=7, day=27)},
    {'name': 'Paola', 'birthday': datetime(year=1985, month=7, day=28)},
    {'name': 'Rick', 'birthday': datetime(year=1999, month=8, day=1)},
    {'name': 'Piter', 'birthday': datetime(year=1984, month=7, day=29)},
    {'name': 'Petra', 'birthday': datetime(year=1985, month=8, day=2)},
    {'name': 'Antonio', 'birthday': datetime(year=1988, month=8, day=3)},
    {'name': 'Silvestr', 'birthday': datetime(year=1988, month=7, day=31)},
    {'name': 'Irma', 'birthday': datetime(year=1988, month=7, day=31)},
    {'name': 'Pol', 'birthday': datetime(year=1988, month=8, day=5)},
    {'name': 'Tim', 'birthday': datetime(year=1988, month=7, day=5)},
    {'name': 'Tomas', 'birthday': datetime(year=1988, month=7, day=26)},
    {'name': 'Patric', 'birthday': datetime(year=1988, month=8, day=4)},
    {'name': 'Anna', 'birthday': datetime(year=1988, month=8, day=26)}
]


def get_birthday_per_week(users):
    '''
Функція повертає інформації про іменинників відносно поточної дати.
Результат показує дані на тиждень в перед від поточної дати (7 днів), поточна дата не враховується.
Іменинники у кого день народження на вихідних - відображаються у понеділок
    '''

    Monday = 'Monday: '
    Tuesday = 'Tuesday: '
    Wednesday = 'Wednesday: '
    Thursday = 'Thursday: '
    Friday = 'Friday: '

    for i in users:

        b = datetime.now()
        a = i.get('birthday').replace(year=b.year)

        if a >= b and a < b + timedelta(days=7):
            if a.strftime('%A') in ('Saturday', 'Sunday', 'Monday'):
                Monday = Monday + ', ' + i.get('name')
            if a.strftime('%A') == ('Tuesday'):
                Tuesday = Tuesday + ', ' + i.get('name')
            if a.strftime('%A') == ('Wednesday'):
                Wednesday = Wednesday + ', ' + i.get('name')
            if a.strftime('%A') == ('Thursday'):
                Thursday = Thursday + ', ' + i.get('name')
            if a.strftime('%A') == ('Friday'):
                Friday = Friday + ', ' + i.get('name')

    result = Monday.replace(' , ', ' ') + '\n' + Tuesday.replace(' , ', ' ') + \
        '\n' + Wednesday.replace(' , ', ' ') + '\n' + \
        Thursday.replace(' , ', ' ') + '\n' + Friday.replace(' , ', ' ')
    return result


print(get_birthday_per_week(users))
