import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np


categories = [
        {
        'title':'Download Filtered',
        'cdf': pd.read_csv('data/dl_filtered_cdf.csv'),
        'results': pd.read_csv('data/dl_filtered_results.csv')
        },
        {
        'title':'Download Unfiltered',
        'cdf': pd.read_csv('data/dl_unfiltered_cdf.csv'),
        'results': pd.read_csv('data/dl_unfiltered_results.csv'), 
        },
        {
        'title':'Upload Filtered',
        'cdf': pd.read_csv('data/ul_filtered_cdf.csv'),
        'results': pd.read_csv('data/ul_filtered_results.csv')   
        },
        {
        'title':'Upload Unfiltered',
        'cdf': pd.read_csv('data/ul_unfiltered_cdf.csv'),
        'results': pd.read_csv('data/ul_unfiltered_results.csv')      
        },
        {
        'title':'Download & Upload Unfiltered',
        'cdf': pd.read_csv('data/both_unfiltered_cdf.csv'),
        'results': pd.read_csv('data/both_unfiltered_results.csv')         
        }]

tab0, tab1, tab2,tab3, tab4= st.tabs([categories[0]['title'],
                                     categories[1]['title'],
                                     categories[2]['title'],
                                     categories[3]['title'],
                                     categories[4]['title']])

def output(tab):
    st.header(categories[tab]['title'])
    
    fig = px.line(categories[tab]['cdf'], 
                  x="xleft", 
                y="data", 
                color="site",
                log_x=True
                )
    st.plotly_chart(fig)
    st.table(categories[tab]['results'])

with tab0: 
    output(0)
with tab1: 
    output(1)
with tab2: 
    output(2)
with tab3: 
    output(3)
with tab4: 
    output(4)
   