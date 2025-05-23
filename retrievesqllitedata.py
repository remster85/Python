import sqlite3

def dump_sqlite_db(db_path, output_path="dump.sql"):
    conn = sqlite3.connect(db_path)
    conn.text_factory = str  # Ensures binary data is not auto-decoded
    cursor = conn.cursor()

    with open(output_path, "w", encoding="utf-8") as f:
        # Write BEGIN TRANSACTION
        f.write("BEGIN TRANSACTION;\n")

        # Get all table names
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';")
        tables = cursor.fetchall()

        for (table_name,) in tables:
            # Get CREATE TABLE statement
            cursor.execute(f"SELECT sql FROM sqlite_master WHERE type='table' AND name='{table_name}';")
            create_stmt = cursor.fetchone()[0]
            f.write(f"{create_stmt};\n")

            # Dump INSERT INTO statements
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()

            col_names = [description[0] for description in cursor.description]
            for row in rows:
                values = []
                for value in row:
                    if value is None:
                        values.append("NULL")
                    elif isinstance(value, (int, float)):
                        values.append(str(value))
                    else:
                        escaped = str(value).replace("'", "''")
                        values.append(f"'{escaped}'")
                values_str = ", ".join(values)
                f.write(f"INSERT INTO {table_name} ({', '.join(col_names)}) VALUES ({values_str});\n")

        # Write COMMIT
        f.write("COMMIT;\n")

    print(f"SQL dump written to {output_path}")

# Usage:
# dump_sqlite_db("your_file.db")
