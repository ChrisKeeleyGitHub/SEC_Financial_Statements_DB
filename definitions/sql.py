# SQL Connection manager
# ADD YOUR OWN CONNECTION IN connect_sql()
# SQL syntax is configured for MySQL

import mysql.connector
from definitions import log


logger = log.get_logger()


def connect_sql():
    logger.info('Connecting to SQL')

    # TODO: input your own mysql connector
    con = mysql.connector.connect(
        host="",
        user="",
        passwd="",
        auth_plugin=''
    )
    return con


def verify_database(con, cTable):
    logger.debug('Verifying table exists')

    sql = 'CREATE DATABASE IF NOT EXISTS {};'.format(cTable.database)
    cur = con.cursor()
    cur.execute(sql)
    con.commit()



def table_exists(con, cTable):
    logger.debug('Checking if table exists')

    # CHECK IF TABLE EXISTS
    sql = "SELECT * FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA='{}' AND TABLE_NAME='{}'".format(cTable.database, cTable.table_name)

    cur = con.cursor()
    cur.execute(sql)

    # GET RESULTS
    results = cur.fetchall()

    cur.close()

    if results:
        return True
    else:
        return False


def create_table(con, cTable):
    logger.debug('Creating table')

    if hasattr(cTable, 'character_set'):
        sql_string = """CREATE TABLE {}.{} ({}) CHARACTER SET {}""".format(cTable.database, cTable.table_name, cTable.columns, cTable.character_set)
    else:
        sql_string = """CREATE TABLE {}.{} ({})""".format(cTable.database, cTable.table_name, cTable.columns)

    cur = con.cursor()
    cur.execute(sql_string)
    cur.close()

    con.commit()


def index_exists(con, cTable):
    logger.debug('Checking if index exists')

    # CHECK IF INDEX EXISTS
    sql = """
            SELECT COUNT(1) IndexIsThere FROM INFORMATION_SCHEMA.STATISTICS WHERE table_schema='{}' 
            AND table_name='{}' AND index_name='ix{}';
          """.format(cTable.database, cTable.table_name, cTable.index_column)

    cur = con.cursor()
    cur.execute(sql)
    results = cur.fetchall()

    cur.close()
    # GET RESULTS

    if results[0][0] == 0:
        return False
    else:
        return True


def create_index(con, cTable):
    logger.debug('Creating index')

    sql = 'create index ix{} on {}.{} ({}({}));'.format(cTable.index_column, cTable.database, cTable.table_name, cTable.index_column, cTable.index_len)
    cur = con.cursor()
    cur.execute(sql)
    cur.close()
    con.commit()


def upload_file(con, cTable, file_path):
    logger.debug('Uploading file to: {}.{} | File: {}'.format(cTable.database, cTable.table_name, file_path))

    sql = """
        LOAD data INFILE '{file_path}' IGNORE
        INTO TABLE {database}.{table_name}
        COLUMNS TERMINATED BY '{column_term}'
        ESCAPED BY ''
        LINES TERMINATED BY '{line_term}'
        IGNORE {ignore_lines} LINES;
    """.format(
        file_path=file_path,
        database=cTable.database,
        table_name=cTable.table_name,
        column_term=cTable.column_term,
        line_term=cTable.line_term,
        ignore_lines=cTable.ignore_lines
    )

    cur = con.cursor()
    cur.execute(sql)
    cur.close()
    con.commit()


def drop_table(con, cTable):
    logger.debug('Dropping table')

    sql = 'TRUNCATE TABLE {}.{}'.format(cTable.database, cTable.table_name)
    cur = con.cursor()
    cur.execute(sql)
    cur.close()
    con.commit()






