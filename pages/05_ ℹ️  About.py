
import streamlit as st
import streamlit_antd_components as sac
from st_config import set_cfg
import time
from streamlit_extras.stylable_container import stylable_container
import base64
from streamlit.components.v1 import html


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

col1,col2,col3=st.columns(3)


def render_svg(svg_string):
    """Renders the given svg string."""
    c = st.container()
    with c:
        html(svg_string)



with col2:
    col2.text('')
    col2.text('')
    col2.text('')
    col2.text('')
    col2.text('')
    col2.text('')
    col2.text('')
    render_svg(open("logo_new.svg").read())

    sac.segmented(
        items=[
            sac.SegmentedItem(label='', icon='facebook', href='https://www.facebook.com/ahanasystems/'),
            sac.SegmentedItem(label='', icon='linkedin',  href='https://in.linkedin.com/company/ahana-systems-and-solutions-pvt-ltd'),
            sac.SegmentedItem(label='', icon='youtube', href='https://ahanait.com/'),
            sac.SegmentedItem(label='', icon='twitter-x',  href='https://x.com/i/flow/login?redirect_after_login=%2Fahanasystems'),
            sac.SegmentedItem(label='', icon='browser-safari',  href='https://ahanait.com/'),
        ], label='', index=None, align='center', size=25,use_container_width=True
    )
    k1,k2,k3=col2.columns([2,6,2])
    k2.caption('© 2024. Ahana Systems and Solutions Private Limited')



#info_btn=col1.button('Info')
#war_btn=col1.button('Warning')
#err_btn=col1.button('Error')
#
#if info_btn:
#    sac.result(label='Success', description='', status='success')
#elif war_btn:
#    sac.result(label='Warning', description='', status='warning')
#elif err_btn:
#    sac.result(label='Error', description='', status='error')
#
#with col1:
#    ass=sac.segmented(
#        items=[
#            sac.SegmentedItem(label='apple1',icon=''),
#            sac.SegmentedItem(label='apple2',icon=''),
#            sac.SegmentedItem(label='apple3',icon=''),
#            sac.SegmentedItem(label='apple4',icon=''),
#            sac.SegmentedItem(label='disabled', disabled=True),
#        ], align='center', use_container_width=True
#    )
#
#    st.write(ass)
#
#
#
#sac.rate(label='label', value=2.0, align='center')
#
##from streamlit_autorefresh import st_autorefresh
##count = st_autorefresh(interval=10000, limit=100, key="fizzbuzzcounter")
##st.write(count)
#
#
##with col1:
##    sac.buttons([
##        sac.ButtonsItem(label='button1'),
##        sac.ButtonsItem(label='button2'),
##        sac.ButtonsItem(label='button3'),
##        sac.ButtonsItem(label='button4'),
##        sac.ButtonsItem(label='button5'),
##        sac.ButtonsItem(label='button6'),
##    ],direction='vertical', use_container_width=True,key='sac.buttons')
##
#
#
#
#res=sac.buttons(['button1', 'button2', 'button3'], key='sac.buttons',direction='vertical',radius='lg', color='gray')
##st.write(f"sac.buttons session value **{st.session_state['sac.buttons']}**")
#
#if res == 'button3':
#    res1=sac.buttons(['button4', 'button5', 'button6'], key='sac.buttons1',direction='vertical')
#    if res1 == 'button5':
#        res2=sac.buttons(['button6', 'button7', 'button8'], key='sac.buttons2',direction='vertical')
#        if res2 == 'button7':
#            st.success('Working sessio state')
#
#
#
#







