import streamlit as st
import cv2
import numpy as np
from st_config import set_cfg
import time
import extra_streamlit_components as stx
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




chosen_id = stx.tab_bar(data=[
    stx.TabBarItemData(id=1, title="Camera Settings", description=""),
    stx.TabBarItemData(id=2, title="Alerts Configurations", description=""),
    stx.TabBarItemData(id=3, title="Video Analytics Settings", description=""),
    stx.TabBarItemData(id=4, title="Misc Settings", description=""),
], default=1)

c1,c2,c3,c4=st.columns([2,0.5,4,8])


@st.experimental_dialog("Are you sure! ⚠️",width="small")
def confirm():
    #st.warning('Confirm to save')
    if st.button("Cofirm",use_container_width=True,type='primary'):
        sac.result(label='Success', description='', status='success')
        #close_op=sac.buttons([sac.ButtonsItem(icon=sac.BsIcon(name='x-circle', size=50))], align='center', variant='text', index=None)
        #st.text(close_op)

def camera_settings():
    c3.text('')
    c3.text('')
    c1.subheader('camera settings')
    with c1:
        cam_set1=sac.buttons(['Add Camera', 'View Cameras', 'Modify Camera','Remove Camera','Test Camera'], key='sac.buttons1',direction='vertical',radius='lg', color='gray',use_container_width=True)
        if cam_set1 == 'Add Camera':
            with c3.expander('Add new camera',expanded=True):
                cam_id=st.text_input('Enter Camera ID')
                cam_name=st.text_input('Enter Camera Name')
                cam_type=st.text_input('Enter Camera Type')
                cam_loc=st.text_input('Enter Camera Location')
                cam_ip=st.text_input('Enter Camera IP')
                cam_port=st.text_input('Enter Camera Port')
                cam_url=st.text_input('Enter Camera RTSP URL')
                cam_set2=sac.buttons(['Cancel','Save Camera'], key='sac.buttons2',direction='horizontal',radius='lg', color='gray',use_container_width=True,)
                if cam_set2 == 'Save Camera':
                    with c4:
                        sac.result(label='Success', description='Camera details saved successfully!', status='success')




def alert_settings():
    c3.text('')
    c3.text('')
    c1.subheader('Alert settings')
    with c1:
        alert_set1=sac.buttons(['Create Alert Group', 'Add/Remove Users','Manage Groups'], key='sac.buttons3',direction='vertical',radius='lg', color='gray',use_container_width=True)
        if alert_set1 == 'Create Alert Group':
            with c3.expander('Create new group',expanded=True):
                grp_name=st.text_input('Enter New Group Name')
                grp_desc=st.text_input('Group Description')
                grp_users=st.multiselect("**:black[Select Users]**",("user1@email.com", "user2@email.com", "user3@email.com", "user4@email.com", "user5@email.com"),label_visibility='visible')
                alert_set2=sac.buttons(['Cancel','Add Group'], key='sac.buttons4',direction='horizontal',radius='lg', color='gray',use_container_width=True,)
                if alert_set2 == 'Add Group':
                    with c4:
                        confirm()
        elif  alert_set1 == 'Add/Remove Users': 
            with c3.expander('Add or remove user from group',expanded=True):
                sel_grp=st.selectbox('Select existing group',['group1','group2','group3','group4'],index=None) 
                sel_usr=st.selectbox('Select user',['user1','user2','user3','user4'],index=None)
                add_usr_btn=sac.buttons(['Cancel','Add','Remove'], key='sac.buttons5',direction='horizontal',radius='lg', color='gray',use_container_width=True,)
                if add_usr_btn == 'Add':
                    if sel_grp is not None and sel_usr is not None:
                        confirm()
                    else:
                        with c3:
                            sac.alert(label='Information', description='Both fields should not be empty!', radius='lg', variant='filled', color='info', banner=False, icon=True, closable=True,key='1') 

                elif add_usr_btn == 'Remove':
                    if sel_grp is not None and sel_usr is not None:
                        confirm()













def misc_settings():
   c3.text('')
   c3.text('')
   c1.subheader('Alert settings')
   with c1:
       with stylable_container(key="blue_button",css_styles="""button {background-color: #85929E;color: white;border-radius: 20px;}""",):
           add_cam_btn=st.button('Add Camera',use_container_width=True)
           view_cam_btn=st.button('View Cameras',use_container_width=True)
           modi_cam_btn=st.button('Modify Camera',use_container_width=True)
           rm_cam_btn=st.button('Remove Camera',use_container_width=True)
           test_cam_btn=st.button('Test Camera',use_container_width=True)
   if add_cam_btn:
       with c3.expander('Add new camera',expanded=True):
           cam_id=st.text_input('Enter Camera ID')
           cam_name=st.text_input('Enter Camera Name')
           cam_type=st.text_input('Enter Camera Type')
           cam_loc=st.text_input('Enter Camera Location')
           cam_ip=st.text_input('Enter Camera IP')
           cam_port=st.text_input('Enter Camera Port')
           cam_url=st.text_input('Enter Camera RTSP URL')
           save_cam_btn=st.button('Save Camera',use_container_width=True,type='primary')





               








if chosen_id == '1':
    camera_settings()
elif chosen_id == '2':
    alert_settings()




#val = stx.stepper_bar(steps=["Ready", "Get Set", "Go","Ready", "Get Set", "Go"])
#st.info(f"Phase #{val}")