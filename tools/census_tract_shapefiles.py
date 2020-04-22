import urllib.request
import zipfile
import os.path


url_dir = 'https://www2.census.gov/geo/tiger/TIGER2019/TRACT'


def get_census_tracts(geoid, download_directory):
    download_url = f'{url_dir}/tl_2019_{geoid}_tract.zip'
    saved_file = f'{download_directory}/tl_2019_{geoid}_tract.zip'

    # download the file from the download url

    # unzip the file to saved_file 
    