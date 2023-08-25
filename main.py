from datetime import date, datetime, timedelta

def get_birthdays_per_week(users):
    if users:
        today = date.today()
        end_of_week = today + timedelta(days=7)
        another_dict = {}
        birthday_dict = {'Monday':[],
                         'Tuesday':[],
                         'Wednesday':[],
                         'Thursday':[],
                         'Friday':[],
                         'Saturday':[],
                         'Sunday':[]}
        for user in users:
            user_birthday = user.get('birthday')
            if today <= user_birthday.replace(year=today.year) < end_of_week:
                day_of_week = (user_birthday.replace(year=today.year).strftime('%A'))
                if day_of_week == 'Saturday' or day_of_week == 'Sunday':
                    birthday_dict['Monday'].append(user['name'])
                elif day_of_week != 'Saturday' or day_of_week != 'Sunday':
                    birthday_dict[day_of_week].append(user.get('name'))
            elif today > user_birthday.replace(year=today.year):
                if user_birthday.month == 1:
                    if today <= user_birthday.replace(year=(today.year+1)) < end_of_week:
                        day_of_week = (user_birthday.replace(year=(today.year+1)).strftime('%A'))
                        if day_of_week == 'Saturday' or day_of_week == 'Sunday':
                            birthday_dict['Monday'].append(user['name'])
                        elif day_of_week != 'Saturday' or day_of_week != 'Sunday':
                            birthday_dict[day_of_week].append(user.get('name'))
        for day, names  in birthday_dict.items():
            if names:
                another_dict[day] = names
        return another_dict
    else:
        return dict()

if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
    ]
    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")