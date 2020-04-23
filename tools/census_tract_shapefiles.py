import urllib.request
import zipfile
import os.path


url_dir = 'https://www2.census.gov/geo/tiger/TIGER2019/TRACT'


def get_census_tracts(geoid, download_directory):
    download_url = f'{url_dir}/tl_2019_{geoid}_tract.zip'
    saved_file = f'{download_directory}/tl_2019_{geoid}_tract.zip'

    # download the file from the download url

    # Good resource, check the second solution in first response
    # https://stackoverflow.com/questions/7243750/download-file-from-web-in-python-3
    # using urllib.request.urlretrieve

    # unzip the file to saved_file

    # Good resource here:
    # https://stackoverflow.com/questions/3451111/unzipping-files-in-python
