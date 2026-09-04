import sqlite3
from datetime import datetime

def create_table(cursor):
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS test_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            test_name TEXT NOT NULL,
            status TEXT NOT NULL,
            run_date TEXT NOT NULL
        )
    ''')

def insert_result(cursor, test_name, status):
    cursor.execute('''
        INSERT INTO test_results (test_name, status, run_date)
        VALUES (?, ?, ?)
    ''', (test_name, status, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

def fetch_all_results(cursor):
    cursor.execute('SELECT * FROM test_results')
    return cursor.fetchall()

def main():
    conn = sqlite3.connect('test_results.db')
    cursor = conn.cursor()

    create_table(cursor)

    insert_result(cursor, 'Login Test', 'Passed')
    insert_result(cursor, 'Add to Cart Test', 'Passed')
    insert_result(cursor, 'Checkout Test', 'Failed')

    conn.commit()

    print("All test results in the database:")
    for row in fetch_all_results(cursor):
        print(row)

    conn.close()

if __name__ == "__main__":
    main()
