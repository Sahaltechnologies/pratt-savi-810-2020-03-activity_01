import urllib.request
import zipfile
import os.path


url_dir = 'https://www2.census.gov/geo/tiger/TIGER2019/TRACT'


def get_census_tracts(geoid, download_directory):
    download_url = f'{url_dir}/tl_2019_{geoid}_tract.zip'
    saved_file = f'{download_directory}/tl_2019_{geoid}_tract.zip'

    if not os.path.exists(saved_file):
        print(f'Getting Tracts for {geoid}')
        print(download_url)
        urllib.request.urlretrieve(download_url, saved_file)

    with zipfile.ZipFile(saved_file, 'r') as zip_ref:
        zip_ref.extractall(download_directory)
