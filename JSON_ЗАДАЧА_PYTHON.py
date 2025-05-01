

"""
Пройти по списку и :
вывести в консоли full name (firstName + lastName)
посчитать и вывести в консоли итоговую зарплату
вывести имена, где в фамилия = Rose
посчитать и вывести количество уникальных фамилий
"""
users = [
    {
        "firstName": "John",
        "lastName": "Rose",
        "gender": "male",
        "salary": 200
    },
    {
        "firstName": "Margo",
        "lastName": "Rose",
        "gender": "male",
        "salary": 150
    },
    {
        "firstName": "Lisa",
        "lastName": "Barcley",
        "gender": "male",
        "salary": 1600
    },
    {
        "firstName": "John",
        "lastName": "Rose",
        "gender": "male",
        "salary": 2600
    },
]


print("Полные имена:")
for user in users:
    full_name = f"{user['firstName']} {user['lastName']}"
    print(full_name)

total_salary = sum(user['salary'] for user in users)
print("\nИтоговая зарплата:", total_salary)

print("\nИмена с фамилией 'Rose':")
roses = [user['firstName'] for user in users if user['lastName'] == 'Rose']
for name in roses:
    print(name)

unique_last_names = {user['lastName'] for user in users}
print("\nКоличество уникальных фамилий:", len(unique_last_names))
