# Auto downloads financial statement zips from: https://www.sec.gov/dera/data/financial-statement-data-sets.html
# Unzips all files and fixes file encoding errors (source claims files are supposed to be encoded in utf-8 but they're not)


from definitions import log
import requests
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve
import zipfile
import codecs
from shutil import move


logger = log.get_logger()

def _download_path():
    logger.debug('Getting download path')

    fp = os.getcwd() + '/downloads/'
    return fp


def _get_urls():
    logger.debug('Getting financial statement urls')

    url = 'https://www.sec.gov/dera/data/financial-statement-data-sets.html'
    resp = requests.get(url)

    soup = BeautifulSoup(resp.content, 'html.parser')
    links = soup.find_all('a')
    urls = []
    for link in links:
        href = link.get('href')
        if href is not None and href[-4:] == '.zip':
            urls.append(href)

    return urls


def _filter_files(urls):
    logger.debug('Filtering file history')

    files = open(_download_path() + '/download_history.log', 'r').read().split('\n')

    missing_urls = []
    for url in urls:
        file_name = url.split('/')[-1:][0]
        if file_name not in files:
            missing_urls.append(url)

    return missing_urls


def _download_zips(missing_urls):
    logger.debug('Downloading zips')

    zip_path = _download_path() + 'zips/'

    url_base = 'https://www.sec.gov'

    downloaded_files = []
    for url in missing_urls:
        logger.debug('Downloading {}/{} zips'.format(ix + 1, len(missing_urls)))
        file_name = url.split('/')[-1:][0]
        dest_path = zip_path + file_name
        urlretrieve(url_base + url, dest_path)
        downloaded_files.append(file_name)



    with open(_download_path() + '/download_history.log', 'a') as file_obj:
        for file in downloaded_files:
            file_obj.write('{}\n'.format(file))


def _unzip_files():
    logger.debug('Getting files needed to unzip')

    zip_path = _download_path() + 'zips/'
    unzipped_path = _download_path() + 'unzipped/'
    zips = os.listdir(zip_path)
    unzipped = os.listdir(unzipped_path)

    for zip_file in zips:
        if zip_file not in unzipped:

            # MAKE UNZIP DEST AND UNZIP TO DEST
            unzip_dest = unzipped_path + zip_file
            os.mkdir(unzip_dest)
            zip_obj = zipfile.ZipFile(zip_path + zip_file, 'r')
            zip_obj.extractall(unzip_dest)
            zip_obj.close()


def _fix_encoding(file_path):
    logger.debug('Fixing coding')

    with codecs.open(file_path, 'r', encoding='utf8', errors='ignore') as file_obj:
        lines = file_obj.read()

    with codecs.open(file_path, 'w', encoding='utf8') as file_obj:
        file_obj.write(lines)


def _move_files():
    logger.debug('Moving files')

    unzipped_path = _download_path() + '/unzipped/'
    unzipped_folders = os.listdir(unzipped_path)

    for unzipped_folder in unzipped_folders:
        folder_path = unzipped_path + unzipped_folder + '/'
        folder_files = os.listdir(folder_path)

        for file in folder_files:
            file_path = folder_path + file
            new_file_name = unzipped_folder[:6] + '_' + file
            if file == 'readme.htm':
                os.remove(file_path)
            else:
                table = file[:3].upper()
                dest_path = _download_path() + 'tables/tbl{}/data/{}'.format(table, new_file_name)

                move(file_path, dest_path)

                _fix_encoding(dest_path)



def main():
    logger.debug('Downloading data')

    urls = _get_urls()
    missing_urls = _filter_files(urls)

    if missing_urls:
        logger.info('New files available: {}'.format(len(missing_urls)))
        _download_zips(missing_urls)
        _unzip_files()
        _move_files()

        return len(missing_urls)

    else:
        logger.info('No new available files')

        return 0


