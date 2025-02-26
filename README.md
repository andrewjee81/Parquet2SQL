# Parquet2SQL - Parquet to SQL Table Script
 
This script reads Parquet files from a `source` directory, extracts the schema, and generates corresponding `CREATE TABLE` SQL statements. The generated SQL files are saved in the `sql_scripts` folder.

## Features
- Reads Parquet files from the `source` directory.
- Extracts column names and data types.
- Maps Parquet data types to SQL data types.
- Generates `CREATE TABLE` statements.
- Saves the SQL script to the `sql_scripts` folder.

## Prerequisites
Ensure you have the following installed:
- Python 3
- Required dependencies:
  ```sh
  pip install pandas pyarrow
  ```

## Folder Structure
```
project_folder/
│── source/             # Parquet files should be placed here
│── sql_scripts/        # SQL files will be generated here
│── banner.py           # Contains CLI art for display
│── main.py           # Main script
│── README.md           # Documentation
```

## How to Use
1. Place your Parquet files inside the `source` directory.
2. Run the script:
   ```sh
   python main.py
   ```
3. The script will process each file, generate SQL scripts, and save them in the `sql_scripts` folder.
4. If the SQL file is successfully written, you will see a confirmation message.

## Example Output
For a Parquet file named `users_2024.parquet`, an SQL file `users.sql` will be created with content similar to:
```sql
CREATE TABLE users (
  "id" INTEGER,
  "name" TEXT,
  "email" TEXT,
  "created_at" TIMESTAMP
);
```

## Error Handling
- If the `source` directory is missing, the script will display an error message.
- If a file fails to be written, an error message will be shown.

## Notes
- Data type mappings are predefined but can be modified in the script.
- The script includes a `banner` module for CLI visuals.

## License
This project is licensed under the MIT License.

