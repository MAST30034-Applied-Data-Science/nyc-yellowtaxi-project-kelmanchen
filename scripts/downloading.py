from urllib.request import urlretrieve
import os
import zipfile

TLC_URL_TEMPLATE = "https://d37ci6vzurychx.cloudfront.net/trip-data/"
OUTPUT_REL_DIR = '../data/raw/'
OUTPUT_REL_DIR_CURATED = '../data/curated/'

def make_outputs():
    '''Makes all outputs necessary for downloading.'''

    if not os.path.exists(OUTPUT_REL_DIR):
        os.makedirs(OUTPUT_REL_DIR)

    if not os.path.exists(OUTPUT_REL_DIR + 'NYC TLC Data'):
        os.makedirs(OUTPUT_REL_DIR + 'NYC TLC Data')

    if not os.path.exists(OUTPUT_REL_DIR + "External Data"):
        os.makedirs(OUTPUT_REL_DIR + "External Data")

    if not os.path.exists(output_REL_DIR_CURATED + "Taxi Zones"):
        os.makedirs(output_REL_DIR_CURATED + "Taxi Zones")

def tlc_data_download(name, year, month):
    '''Accepts name, year and month required and download data from TLC website as parquet file into OUTPUT_REL_DIR.'''
    
    month = str(month).zfill(2)

    output_dir = f"{name}_tripdata_{year}-{month}.parquet"
    url =f'{TLC_URL_TEMPLATE}{output_dir}'

    urlretrieve(url, f"{OUTPUT_REL_DIR}NYC TLC Data/{output_dir}")
    print(f"Completed downloading {output_dir}")

def covid_data_download():
    '''Downloads COVID-19 Data from the City of New York website.'''

    covid_url = 'https://data.cityofnewyork.us/api/views/rc75-m7u3/rows.csv?accessType=DOWNLOAD'
    covid_output_dir = 'COVID-19_Daily_Counts_of_Cases__Hospitalizations__and_Deaths.csv'

    urlretrieve(covid_url, f"{OUTPUT_REL_DIR}External Data/{covid_output_dir}")
    print(f"Completed downloading {covid_output_dir}")

def tlc_shapefiles_download():
    '''Downloads shapefiles and zone lookup data from the TLC website, and unzips files.'''

    zone_lookup_url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi+_zone_lookup.csv'
    zone_url = 'https://d37ci6vzurychx.cloudfront.net/misc/taxi_zones.zip'
    zone_lookup_dir = 'taxi_zones_lookup.csv'
    zone_url_dir = 'taxi_zones.zip'

    # data does not require preprocessing, so download straight into curated folder
    urlretrieve(zone_lookup_url, f"{OUTPUT_REL_DIR_CURATED}Taxi Zones/{zone_lookup_dir}")
    urlretrieve(zone_url, f"{OUTPUT_REL_DIR_CURATED}Taxi Zones/{zone_url_dir}")

    print(f"Completed downloading {zone_lookup_dir}")
    print(f"Completed downloading {zone_url_dir}")

    with zipfile.ZipFile(f"{OUTPUT_REL_DIR_CURATED}Taxi Zones/{zone_url_dir}","r") as zip_ref:
        zip_ref.extractall(f"{OUTPUT_REL_DIR_CURATED}Taxi Zones/")

    print(f"Unzipped and extracted {zone_url_dir}")

    
# make outputs
make_outputs()

# download all TLC data required
for name in ('yellow', 'fhvhv'):
    tlc_data_download(name, 2019, 12)
    tlc_data_download(name, 2020, 1)
    tlc_data_download(name, 2020, 2)
    tlc_data_download(name, 2021, 12)
    tlc_data_download(name, 2022, 1)
    tlc_data_download(name, 2022, 2)

# download all COVID-19 data required
covid_data_download()

# download necessary TLC shapefile data
tlc_shapefiles_download()

