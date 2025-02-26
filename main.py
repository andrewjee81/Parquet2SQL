import os
import pandas as pd
import pyarrow.parquet as pq
import time as tm
from banner import Banner

# Path to the 'source' directory
directory = 'source'

def createSQL(sourcefile) :
    # Load Parquet file
    parquet_file = os.path.join(directory, sourcefile)
    table = pq.read_table(parquet_file)
    df = table.to_pandas()

    # Parquet to SQL type mapping
    parquet_to_sql = {
        "int8": "TINYINT",  # Smallest integer type
        "int16": "SMALLINT",  # Better representation for small numbers
        "int32": "INTEGER",  # Standard integer type
        "int64": "BIGINT",  # Large integer values
        "float32": "FLOAT",  # More widely supported than REAL
        "float64": "DOUBLE PRECISION",  # Same as FLOAT8 in PostgreSQL
        "boolean": "BOOLEAN",  # Boolean type
        "string": "TEXT",  # Text type (VARCHAR is another option)
        "binary": "BLOB",  # Binary large object
        "timestamp[ns]": "TIMESTAMP",  # Nanosecond precision timestamp
        "timestamp[ms]": "TIMESTAMP",  # Millisecond precision timestamp
        "date32": "DATE",  # Stores only date, no time
        "time32[ms]": "TIME",  # Stores only time
        "decimal128": "DECIMAL(38,18)",  # High precision decimal (adjust as needed)
        "uuid": "UUID",  # If UUIDs exist in the schema
    }

    # Generate CREATE TABLE statement
    table_name = sourcefile.split('_')[0]
    columns = []

    for col_name, dtype in df.dtypes.items():
        sql_type = parquet_to_sql.get(str(dtype), "TEXT")  # Default to TEXT if unknown
        columns.append(f'"{col_name}" {sql_type}')

    create_table_sql = f"CREATE TABLE {table_name} (\n  {',\n  '.join(columns)}\n);"

    # Save as SQL File #

    # Define the output folder (change this to your desired folder)
    output_folder = 'sql_scripts'
    os.makedirs(output_folder, exist_ok=True)  # Ensure the folder exists

    # Define file path
    sql_filename = table_name + '.sql'
    sql_file_path = os.path.join(output_folder, sql_filename)

    # Write SQL script to file
    try:
        with open(sql_file_path, "w") as f:
            f.write(create_table_sql)

        # Verify the file
        if os.path.exists(sql_file_path) and os.path.getsize(sql_file_path) > 0:
            print(f"{sql_filename} file written successfully!\n")
        else:
            print("File write error!")
    except Exception as e:
        print(f"Error writing file: {e}")


def main() :
    # Create a Banner object and specify the signature color (optional)
    banner = Banner()

    # Display the banner
    banner.display_cli_art()

    # Start the main application
    if os.path.exists(directory) and os.path.isdir(directory):
        for entry in os.scandir(directory):
            if entry.is_file():
                print(f"Processing file: {entry.name}")
                tm.sleep(3)
                createSQL(entry.name)
    else:
        print(f"Error: Directory '{directory}' not found!")

if __name__ == '__main__':
    main()