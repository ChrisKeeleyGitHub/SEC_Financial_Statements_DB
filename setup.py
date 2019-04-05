from setuptools import setup

setup(
    name='SEC_Financial_Statements_DB',
    version='1.0',
    packages=['definitions', 'financial_statement_manager'],
    url='https://github.com/dsilva525',
    license='open source',
    author='ds',
    author_email='davidsilva525@outlook.com',
    description='Downloads all financial statement data from SEC and uploads to a MySQL database'
)
