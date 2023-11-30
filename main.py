import sqlite3

conn = sqlite3.connect('hw8.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
''')

cursor.execute("INSERT INTO countries (title) VALUES ('Кыргызстан')")
cursor.execute("INSERT INTO countries (title) VALUES ('Германия')")
cursor.execute("INSERT INTO countries (title) VALUES ('Китай')")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    )
''')

cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Бишкек', 123.45, 1)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Ош', 456.78, 2)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Берлин', 123.45, 3)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Мюнхен', 789.01, 4)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Франкфурт', 123.45, 5)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Пекин', 456.78, 6)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Шанхай', 789.01, 7)")


cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id)
    )
''')

cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Алан', 'Аскаров', 1)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Арууке', 'Белекова', 2)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Нурсултан', 'Белеков', 3)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Мерим', 'Омурканова', 1)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Алая', 'Атаканова', 2)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Максим', 'Трофимушкин', 3)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Владимир', 'Ленский', 1)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Алиса', 'Пушистская', 2)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Алымбек', 'Акнов', 3)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Арсений', 'Ри', 1)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Виктор', 'Хевук', 2)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Валерия', 'Ким', 3)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Амаль', 'Хавазова', 1)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Эмин', 'Хавазов', 2)")
cursor.execute("INSERT INTO students (first_name, last_name, city_id) VALUES ('Абай', 'Акунов', 3)")
conn.commit()

def display_cities(cursor):
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    for city in cities:
        print(f"{city[0]}. {city[1]}")
    return cities

def display_students_in_city(cursor, city_id):
    cursor.execute('''
        SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
        FROM students
        INNER JOIN cities ON students.city_id = cities.id
        INNER JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
    ''', (city_id,))
    students = cursor.fetchall()
    for student in students:
        print(f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь: {student[4]}")

while True:
    print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    cities = display_cities(cursor)
    chosen_city_id = int(input())
    if chosen_city_id == 0:
        break
    else:
        display_students_in_city(cursor, chosen_city_id)

conn.close()
