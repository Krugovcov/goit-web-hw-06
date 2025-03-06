import psycopg2
from pathlib import Path

# Підключення до бази даних
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="newpassword",
    host="localhost",
    port="5432"
)
cur = conn.cursor()


# Функція для виконання SQL-запиту з файлу та виведення результату
def execute_sql_query_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        query = file.read()
    cur.execute(query)
    return cur.fetchall()  # Отримуємо всі рядки результату


# Виконання кожного запиту з файлів
queries_files = [
    'query_1.sql',
    'query_2.sql',
    'query_3.sql',
    'query_4.sql',
    'query_5.sql',
    'query_6.sql',
    'query_7.sql',
    'query_8.sql',
    'query_9.sql',
    'query_10.sql'
]


queries_files = [Path(__file__).parent / file_name for file_name in queries_files]

for file_path in queries_files:
    print(f"\nВиконую запит з файлу: {file_path}")
    results = execute_sql_query_from_file(file_path)

    # Виведення результату запиту
    if results:  # Якщо є результати
        for row in results:
            print(row)
    else:
        print("Без результатів")


cur.close()
conn.close()
