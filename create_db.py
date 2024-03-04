import sqlite3


def check_tables_exist(conn):
    """Check if tables already exist in the database."""
    cur = conn.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cur.fetchall()
    return len(tables) > 0


def create_database():
    """Create SQLite3 database."""
    # Connect to SQLite3 database (creates a new file if it doesn't exist)
    conn = sqlite3.connect("sales.db")
    cur = conn.cursor()

    # Check if tables already exist
    if not check_tables_exist(conn):
        # Create the tables only if they don't already exist
        cur.execute("""
        CREATE TABLE IF NOT EXISTS Sales (
            sales_id INTEGER PRIMARY KEY,
            customer_id INTEGER
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS Customer (
            customer_id INTEGER PRIMARY KEY,
            age INTEGER
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS Orders (
            order_id INTEGER PRIMARY KEY,
            sales_id INTEGER,
            item_id INTEGER,
            quantity INTEGER
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS Items (
            item_id INTEGER PRIMARY KEY,
            item_name TEXT
        );
        """)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def insert_data():
    """Insert dummy data into the tables."""
    # Connect to SQLite3 database
    conn = sqlite3.connect("sales.db")
    cur = conn.cursor()

    # Check if tables already exist
    if not check_tables_exist(conn):
        cur.executemany(
            "INSERT INTO Sales (sales_id, customer_id) VALUES (?, ?)",
            [
                (1, 1),
                (2, 2),
                (3, 3),
                (4, 4),
                (5, 5),
                (6, 6),
                (7, 7),
                (8, 8),
                (9, 9),
                (10, 10),
            ],
        )

        cur.executemany(
            "INSERT INTO Customer (customer_id, age) VALUES (?, ?)",
            [
                (1, 20),
                (2, 25),
                (3, 30),
                (4, 35),
                (5, 18),
                (6, 22),
                (7, 24),
                (8, 28),
                (9, 33),
                (10, 36),
            ],
        )

        cur.executemany(
            "INSERT INTO Items (item_id, item_name) VALUES (?, ?)",
            [(1, "X"), (2, "Y"), (3, "Z")],
        )

        cur.executemany(
            "INSERT INTO Orders (order_id, sales_id, item_id, quantity) VALUES (?, ?, ?, ?)",
            [
                (1, 1, 1, 2),
                (2, 1, 2, 3),
                (3, 2, 1, 1),
                (4, 3, 1, 4),
                (5, 3, 2, 1),
                (6, 3, 3, 2),
                (7, 4, 3, 3),
                (8, 5, 2, 1),
                (9, 6, 1, 3),
                (10, 6, 2, 2),
                (11, 7, 1, 1),
                (12, 7, 2, 2),
                (13, 8, 1, 1),
                (14, 9, 1, 2),
                (15, 9, 2, 2),
                (16, 10, 1, 2),
                (17, 10, 3, 1),
            ],
        )

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


def main():
    # Create the database (only if it doesn't already exist)
    create_database()

    # Insert data into the tables
    insert_data()


if __name__ == "__main__":
    main()
