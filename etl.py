import sqlite3

import pandas as pd


def connect_to_db(db_name):
    """Connect to the SQLite3 database and return the connection and cursor objects."""
    conn = sqlite3.connect(db_name)
    cur = conn.cursor()
    return conn, cur


def execute_sql_query(cur, sql_query):
    """Execute the given SQL query and return the results."""
    cur.execute(sql_query)
    return cur.fetchall()


def convert_results_to_dataframe(results, columns):
    """Convert the SQL query results to a DataFrame."""
    return pd.DataFrame(results, columns=columns)


def save_dataframe_to_csv(df, file_name, sep=";", index=False):
    """Save the DataFrame to a CSV file."""
    df.to_csv(file_name, sep=sep, index=index)


def close_db_connection(conn, cur):
    """Close the database connection."""
    cur.close()
    conn.close()


def main():
    # Connect to the SQLite3 database
    conn, cur = connect_to_db("sales.db")

    # SQL solution
    sql_query = """
    SELECT Customer.customer_id, Customer.age, Items.item_name, SUM(Orders.quantity)
    FROM Orders
    JOIN Sales ON Orders.sales_id = Sales.sales_id
    JOIN Customer ON Sales.customer_id = Customer.customer_id
    JOIN Items ON Orders.item_id = Items.item_id
    WHERE Customer.age BETWEEN 18 AND 35 AND Orders.quantity IS NOT NULL
    GROUP BY Customer.customer_id, Items.item_name
    """
    results = execute_sql_query(cur, sql_query)

    # Convert results to DataFrame
    df_sql = convert_results_to_dataframe(
        results, columns=["Customer", "Age", "Item", "Quantity"]
    )

    # Store the query to a CSV file
    save_dataframe_to_csv(df_sql, "output.csv")

    # Close the database connection
    close_db_connection(conn, cur)


if __name__ == "__main__":
    main()
