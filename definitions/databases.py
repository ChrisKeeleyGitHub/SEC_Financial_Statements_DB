# Database structure for uploading to MySQL
import os


database_fp = os.getcwd() + '/downloads/tables/'

class dbSEC_FINANCIAL_STATEMENTS:
    def __init__(self):
        self.tblNUM = self.NUM()
        self.tblPRE = self.PRE()
        self.tblSUB = self.SUB()
        self.tblTAG = self.TAG()


    class NUM:
        def __init__(self):
            self.table_name = 'tblNUM'
            self.database = 'dbSEC_FINANCIAL_STATEMENTS'
            self.column_term = '\t'
            self.line_term = '\n'
            self.columns = """
                ACCESSION_NUMBER TEXT,
                TAG TEXT,
                VERSION TEXT,
                COREG TEXT,
                DDATE TEXT,
                QTRS TEXT,
                UOM TEXT,
                VALUE DOUBLE,
                FOOTNOTE TEXT
            """
            self.index_column = 'ACCESSION_NUMBER'
            self.index_len = 20
            self.ignore_lines = 1
            self.character_set = 'utf8'
            self.remake_table = False
            self.table_fp = database_fp + self.table_name + '/'


    class PRE:
        def __init__(self):
            self.table_name = 'tblPRE'
            self.database = 'dbSEC_FINANCIAL_STATEMENTS'
            self.column_term = '\t'
            self.line_term = '\n'
            self.columns = """
                ACCESSION_NUMBER TEXT,
                REPORT TEXT,
                LINE TEXT,
                STMT TEXT,
                INPTH TEXT,
                RFILE TEXT,
                TAG TEXT,
                VERSION TEXT,
                PLABEL TEXT,
                NEGATING TEXT
            """
            self.index_column = 'ACCESSION_NUMBER'
            self.index_len = 20
            self.ignore_lines = 1
            self.character_set = 'utf8'
            self.remake_table = False
            self.table_fp = database_fp + self.table_name + '/'


    class SUB:
        def __init__(self):
            self.table_name = 'tblSUB'
            self.database = 'dbSEC_FINANCIAL_STATEMENTS'
            self.column_term = '\t'
            self.line_term = '\n'
            self.columns = """
                ACCESSION_NUMBER TEXT,
                CIK TEXT,
                NAME TEXT,
                SIC TEXT,
                COUNTRYBA TEXT,
                STPRBA TEXT,
                CITYBA TEXT,
                ZIPBA TEXT,
                BAS1 TEXT,
                BAS2 TEXT,
                BAPH TEXT,
                COUNTRYMA TEXT,
                STPRMA TEXT,
                CITYMA TEXT,
                ZIPMA TEXT,
                MAS1 TEXT,
                MAS2 TEXT,
                COUNTRYINC TEXT,
                STPRINC TEXT,
                EIN TEXT,
                FORMER TEXT,
                CHANGED TEXT,
                AFS TEXT,
                WKSI TEXT,
                FYE TEXT,
                FORM TEXT,
                PERIOD TEXT,
                FY TEXT,
                FP TEXT,
                FILED TEXT,
                ACCEPTED TEXT,
                PREVRPT TEXT,
                DETAIL TEXT,
                INSTANCE TEXT,
                NCIKS TEXT,
                ACIKS TEXT
            """
            self.index_column = 'ACCESSION_NUMBER'
            self.index_len = 20
            self.ignore_lines = 1
            self.character_set = 'utf8'
            self.remake_table = False
            self.table_fp = database_fp + self.table_name + '/'


    class TAG:
        def __init__(self):
            self.table_name = 'tblTAG'
            self.database = 'dbSEC_FINANCIAL_STATEMENTS'
            self.column_term = '\t'
            self.line_term = '\n'
            self.columns = """
                TAG TEXT,
                VERSION TEXT,
                CUSTOM TEXT,
                ABSTRACT TEXT,
                DATATYPE TEXT,
                IORD TEXT,
                CRDR TEXT,
                TLABEL TEXT,
                DOC TEXT
            """
            self.index_column = 'TAG'
            self.index_len = 20
            self.ignore_lines = 1
            self.character_set = 'utf8'
            self.remake_table = False
            self.table_fp = database_fp + self.table_name + '/'





