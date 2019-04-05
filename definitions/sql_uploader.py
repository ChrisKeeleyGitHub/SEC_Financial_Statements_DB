# SQL module to upload table data

from definitions import log, sql
import os

logger = log.get_logger()


def _get_upload_list(cTable):
    logger.debug('Getting upload list')

    upload_history_fp = cTable.table_fp + 'upload_history.log'
    upload_history = open(upload_history_fp, 'r').read().split('\n')

    data_fp = cTable.table_fp + '/data/'
    available_files = os.listdir(data_fp)

    upload_queue = []
    for file in available_files:
        if file not in upload_history:
            upload_queue.append(data_fp + file)

    return upload_queue


def _log_upload(cTable, file):
    logger.debug('Logging file upload')

    upload_history_fp = cTable.table_fp + 'upload_history.log'
    with open(upload_history_fp, 'a') as file_obj:
        file_name = file.split('/')[-1]
        file_obj.write('{}\n'.format(file_name))
        file_obj.close()


def _remake_table(con, cTable):
    logger.debug('Remaking table | {}.{}'.format(cTable.database, cTable.table_name))

    if sql.table_exists(con, cTable):
        sql.drop_table(con, cTable)


def _verify_table(con, cTable):
    logger.debug('Verifying table exists | {}.{}'.format(cTable.database, cTable.table_name))

    table_exists = sql.table_exists(con, cTable)
    if not table_exists:
        sql.create_table(con, cTable)


def _verify_index(con, cTable):
    logger.debug('Verifying index exists | {}.{}'.format(cTable.database, cTable.table_name))

    index_exists = sql.index_exists(con, cTable)
    if not index_exists:
        sql.create_index(con, cTable)


def _upload_files(con, cTable, upload_list):
    logger.debug('Uploading files | {}.{}'.format(cTable.database, cTable.table_name))

    for ix, file_path in enumerate(upload_list):
        try:
            logger.info('Uploading file {}/{}'.format(ix + 1, len(upload_list)))
            sql.upload_file(con, cTable, file_path)


            _log_upload(cTable, file_path)

        except Exception as e:
            logger.exception('Error uploading file: {} \nError: {} \n\n'.format(file_path, e))


def upload(cTable):
    logger.debug('Uploading table | {}.{}'.format(cTable.database, cTable.table_name))

    upload_list = _get_upload_list(cTable)

    if upload_list:
        logger.info('Files needed to upload: '.format(len(upload_list)))
        con = sql.connect_sql()

        sql.verify_database(con, cTable)

        if cTable.remake_table:
            _remake_table(con, cTable)

        _verify_table(con, cTable)
        _verify_index(con, cTable)
        _upload_files(con, cTable, upload_list)

        con.close()


