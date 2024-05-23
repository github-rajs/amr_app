import streamlit as st
import cv2
import numpy as np
from st_config import set_cfg
import time
from streamlit_extras.stylable_container import stylable_container
import streamlit_antd_components as sac


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






st.sidebar.header('Filter Options')

@st.experimental_dialog("Update Incident",width="large")
def vote(id):
 
    remarks=st.text_area('Remarks ')
    if st.button("Submit"):
        sac.result(label='Success', description='', status='success')
        time.sleep(2)
        st.rerun()

@st.experimental_dialog("Captured Image",width="large")
def view_img(id):
    st.image('1.png')
    if st.button('Close Image',use_container_width=True):
        st.rerun()



k1,k2,k3,k4,k5,k6,k7=st.columns([3,3,2,5,1,1,1])
cam_status_sel=k1.multiselect("**:black[Select Incident Type]**",("Active", "Closed"),label_visibility='visible')
area_sel=k2.multiselect("**:black[Select Area]**",("Thermal Plant", "Admin Office", "Electric Stations","Other Areas"),label_visibility='visible')
k3.text('')
k3.text('')
filter_btn=k3.button('Apply Filters',use_container_width=True,type='secondary')


k5.metric("**:green[All Incidents ]**","100")
k6.metric("**:green[🟢 Active ]**","80")
k7.metric("**:red[🔴 Inactive ]**","20")



cc1,cc2,cc3=st.columns([0.1,10,0.1])
cc2.divider()
c1,c2,c3=st.columns([0.1,10,0.1])
colms = c2.columns((2, 2, 2, 2, 1, 1, 1, 2,1))
fields = ["Alert ID",'Alert Name','Date & Time','Location','Status','Time Elapased','View Image','Select Option','Action']
ticket_ids=[1001,1002,1003,1004,1005,1006,1007,1008]


c2.divider()
for col, field_name in zip(colms, fields):
    col.markdown(f'**{field_name}**')




for x in range(0,len(ticket_ids),1):
    col1, col2, col3, col4, col5,col6,col7,col8,col9 = c2.columns((2, 2, 2, 2, 1, 1, 1, 2,1))
    
    col1.caption(f'**:black[{ticket_ids[x]}]**')  
    col2.caption('Perimeter breach')
    col3.caption('2022-20-21 23:22')
    col4.caption('Thermal plant')
    col5.caption(':green[Active 🟢]')
    col6.caption('3 Hr')
    with col7.popover("View",use_container_width=True):
        st.image('1.png')
    option = col8.selectbox("",("Close", "Re-assign", "Mark as Fasle"),key=str(x)+'k',label_visibility='collapsed')
    

    #c2.divider()
    disable_status = 'active'
    button_type = "Unblock" if disable_status else "Block"
    button_phold = col9.empty()
    update_button = button_phold.button('Update', key=str(x),use_container_width=True,type="primary")
    if update_button:
         pass
         vote(x)
 
c2.divider()
sac.pagination(total=30, page_size=8, align='center', radius='xs', variant='light', jump=True,color='lime')
























