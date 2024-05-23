import streamlit as st
import cv2
import numpy as np
from st_config import set_cfg
import time
import pandas as pd
import pydeck as pdk
import altair as alt


st.set_page_config(page_title='AI Analytics', page_icon="👥", layout="wide", initial_sidebar_state="auto", menu_items=None)
st.markdown(set_cfg.hide_deploy_btn,unsafe_allow_html=True)
st.markdown(f'''
    <style>
    .stApp .main .block-container{{
        padding:30px 50px
    }}
    .stApp [data-testid='stSidebar']>div:nth-child(1)>div:nth-child(2){{
        padding-top:50px
    }}
    iframe{{
        display:block;
    }}
    .stRadio div[role='radiogroup']>label{{
        margin-right:5px
    }}
    </style>
    ''', unsafe_allow_html=True)





###########################################

col1,col2,col3=st.columns(3)



chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

c = (
   alt.Chart(chart_data)
   .mark_circle()
   .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

col1.altair_chart(c, use_container_width=True)

###########################################

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

col2.bar_chart(chart_data)

###########################################
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

col3.area_chart(chart_data)

###########################################
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)

###########################################

chart_data = pd.DataFrame(
   np.random.randn(1000, 2) / [50, 50] + [25.242552559862478, 92.34500870575812],
   columns=['lat', 'lon'])

st.pydeck_chart(pdk.Deck(
    map_style=None,
    initial_view_state=pdk.ViewState(
        latitude=25.242552559862478,
        longitude=92.34500870575812,
        zoom=11,
        pitch=100,
    ),
    layers=[
        pdk.Layer(
           'HexagonLayer',
           data=chart_data,
           get_position='[lon, lat]',
           radius=200,
           elevation_scale=4,
           elevation_range=[0, 1000],
           pickable=True,
           extruded=True,
        ),
        pdk.Layer(
            'ScatterplotLayer',
            data=chart_data,
            get_position='[lon, lat]',
            get_color='[200, 30, 0, 160]',
            get_radius=200,
        ),
    ],
))
###########################################

#25.24262804819608, 92.34497775379907