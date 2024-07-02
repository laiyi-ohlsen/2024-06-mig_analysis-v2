import streamlit as st
# pip install streamlit
from google.oauth2 import service_account
# pip install google_oauth2_tool
from google.cloud import bigquery, bigquery_storage
#pip install google-cloud-bigquery
#pip install google-cloud-bigquery-storage

from os.path import dirname, basename, isfile, join
import queries


from queries import dl_filtered_cdf, dl_filtered_raw,  dl_unfiltered_cdf, dl_unfiltered_raw,  ul_filtered_cdf, ul_filtered_raw,  ul_unfiltered_cdf, ul_unfiltered_raw, both_unfiltered_cdf, both_unfiltered_raw

# Setup Info
project_id = 'measurement-lab'
location = 'US'
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)

# BigQuery Client
client = bigquery.Client(project=project_id, location=location,credentials=credentials)

# BigQuery Storage
bq_storage_client = bigquery_storage.BigQueryReadClient(credentials=credentials)


def get_data(query):
        name = query.__name__
        name = name[8:]
        print(name)
        if 'cdf' in name:
            df = client.query(query.query).to_dataframe()
            df.to_csv('data/{}.csv'.format(name), index=False)
        if 'raw' in name: 
            df = client.query(query.query).result().to_dataframe(bqstorage_client=bq_storage_client)
            df.to_csv('data/{}.csv'.format(name), index=False)

get_data(both_unfiltered_cdf) 
# get_data(both_unfiltered_raw)
            
# get_data(dl_filtered_raw)  
# get_data(dl_filtered_cdf) 

# get_data(dl_unfiltered_cdf) 
# get_data(dl_unfiltered_raw) 

# get_data(ul_filtered_cdf) 
# get_data(ul_filtered_raw)  

# get_data(ul_unfiltered_cdf) 
# get_data(ul_unfiltered_raw) 

