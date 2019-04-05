# Uploads data to MySQL
# Configure your own SQL connector under definitions.sql.connect_sql()
# Current SQL syntax is configured for MySQL!


from definitions import sql_uploader
from definitions import databases
from definitions import log


logger = log.get_logger()


def main():
    logger.debug('Uploading data')

    tblNUM = databases.dbSEC_FINANCIAL_STATEMENTS().tblNUM
    tblPRE = databases.dbSEC_FINANCIAL_STATEMENTS().tblPRE
    tblSUB = databases.dbSEC_FINANCIAL_STATEMENTS().tblSUB
    tblTAG = databases.dbSEC_FINANCIAL_STATEMENTS().tblTAG
    tables = [tblNUM, tblPRE, tblSUB, tblTAG]

    for table in tables:
        sql_uploader.upload(table)

