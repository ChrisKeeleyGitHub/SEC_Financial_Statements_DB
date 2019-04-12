# Uploads data to MySQL
# Configure your own SQL connector under definitions.sql.connect_sql()
# Current SQL syntax is configured for MySQL!


from definitions import sql_uploader
from financial_statement_manager import database
from definitions import log


logger = log.get_logger()


def main():
    logger.debug('Uploading data')

    tblNUM = database.dbSEC_FINANCIAL_STATEMENTS().tblNUM
    tblPRE = database.dbSEC_FINANCIAL_STATEMENTS().tblPRE
    tblSUB = database.dbSEC_FINANCIAL_STATEMENTS().tblSUB
    tblTAG = database.dbSEC_FINANCIAL_STATEMENTS().tblTAG
    tables = [tblNUM, tblPRE, tblSUB, tblTAG]

    for table in tables:
        sql_uploader.upload(table)

