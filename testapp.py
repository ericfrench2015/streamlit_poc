# -*- coding: utf-8 -*-
"""
https://www.youtube.com/watch?v=XDCB0uBCKMk

@author: ericf
"""

import streamlit as st
import plotly.express as px
import pandas as pd

def display_map(location_data):
    fig = px.scatter_mapbox(location_data, lat='latitude', lon='longitude')
    #fig.update_layout(mapbox_style='carto-darkmatter')
    fig.update_layout(mapbox_style='mapbox://styles/go-ifrc/ckrfe16ru4c8718phmckdfjh0')
    fig.update_mapboxes(accesstoken=st.secrets.mapbox_access_token)



    #fig.update_layout(mapbox_style='go-ifrc')
    return fig




st.set_page_config(page_title="map",page_icon=":tada:", layout="wide")


loc = [['2021 S Spring',43.5261636,-96.7353953]]

df = pd.DataFrame(loc, columns=['loc','latitude','longitude'])
st.dataframe(df)

st.title("Testing basic streamlit capabilities and deployment")

st.write("This page will be built out using youtube tutorials")

px_map = display_map(df)
st.plotly_chart(px_map, use_container_width=True)

