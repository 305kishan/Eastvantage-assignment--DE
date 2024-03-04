# Data Engineering Assignment

This repository contains a Python script, SQL file, and database for a data engineering assignment. The assignment involves creating a SQLite3 database, populating it with data, and performing ETL (Extract, Transform, Load) operations. The final result is a CSV file.

## Folder Structure

- `create_db.py`: Python script to create the `.db` file, tables, and fill the data. This script should be run first.
- `sales.db`: The SQLite3 database file.
- `etl.py`: Python script to perform ETL (Extract, Transform, Load) operations on the database.
- `output.csv`: The CSV file generated by the `etl.py` script.

## Instructions

1. Run `create_db.py` to create the database and populate it with data.
2. Run `etl.py` to perform ETL operations and generate `output.csv`.

## Requirements

- Python 3.x
- sqlite3
- pandas

## Usage

1. Clone the repository:
```bash
git clone https://github.com/305kishan/Eastvantage-assignment--DE.git
```

2. Navigate to the repository folder:
```bash
cd Eastvantage-assignment--DE
```

3. Run the create_db.py script:
```bash
python create_db.py
```

4. Run the etl.py script:
```bash
python etl.py
```

5. The output CSV file `output.csv` will be generated.

