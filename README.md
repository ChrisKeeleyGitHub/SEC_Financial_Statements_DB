
# SEC Financial Statements Database Manager
- This project automatically downloads all the SEC compiled financial statements from here: 
    - _https://www.sec.gov/dera/data/financial-statement-data-sets.html_


## definitions/databases.py
- Database structure for uploading to MySQL 

## definitions/log.py
- Logging tool

## definitions/sql.py
- MySQL connection 

## definitions/sql_uploader.py
- Reusable tool for uploading/maintaining MySQL database

## definitions/table_definitions.htm
- Official table definitions from source
 
 
 
## financial_statements_manager/download_data.py
- Auto downloads financial statement zips from: 
    - https://www.sec.gov/dera/data/financial-statement-data-sets.html

- Unzips all files and fixes file encoding errors (source claims files are supposed to be encoded in utf-8 but they're not)
 
## financial_statements_manager/upload_data.py
- Uploads data to a MySQL server *MUST CONFIGURE YOUR OWN MySQL connector in definitions.sql.connect_sql()
- SQL query syntax is only configured for MySQL**

