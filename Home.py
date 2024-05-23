import streamlit as st
import streamlit_antd_components as sac
from st_config import set_cfg
import time
from streamlit_extras.stylable_container import stylable_container
import base64


st.set_page_config(page_title='AI Analytics', page_icon="👥", layout="wide", initial_sidebar_state="auto", menu_items=None)
#st.markdown(set_cfg.ahana_logo, unsafe_allow_html=True) 
#st.markdown(set_cfg.hide_bar, unsafe_allow_html=True) 
#st.markdown(set_cfg.show_bar, unsafe_allow_html=True) 
#st.markdown(set_cfg.hide_deploy_btn,unsafe_allow_html=True)
#st.markdown(set_cfg.st_tabs,unsafe_allow_html=True)
#st.write('<style>div.block-container{padding-top:0rem;}</style>', unsafe_allow_html=True)
#st.markdown(set_cfg.hide_img_fs, unsafe_allow_html=True)

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
st.markdown(set_cfg.hide_deploy_btn,unsafe_allow_html=True)

#from streamlit_autorefresh import st_autorefresh
#count = st_autorefresh(interval=10000, limit=100, key="fizzbuzzcounter")
#st.write(count)





def load_gif():
    file_ = open("assets/alert_blink.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url



col1,col2,col3,col4=st.columns([4,4,4,1])




gif_data=load_gif()
st.sidebar.text('')
st.sidebar.text('')
st.sidebar.text('')
st.sidebar.text('')

if st.sidebar.button('test alert'):
    col4.markdown(f'<img src="data:image/gif;base64,{gif_data}" alt="cat gif">',unsafe_allow_html=True,)
    #st.sidebar.subheader('New alert generated!')
    


with col1:
    #st.subheader('Intrusion Alerts')
    sac.alert(label='**Intrusion Alerts**',variant='quote-light')
    sac.alert(label='Perimeter Intrusion', description='Alert Generated', radius='lg', variant='filled', color='warning', banner=False, icon=True, closable=True,key='1')
    sac.alert(label='Perimeter Intrusion', description='Alert Generated', radius='lg', variant='filled', color='warning', banner=False, icon=True, closable=True,key='2')
    sac.alert(label='Perimeter Intrusion', description='Alert Generated', radius='lg', variant='filled', color='warning', banner=False, icon=True, closable=True,key='3')
    sac.alert(label='Perimeter Intrusion', description='Alert Generated', radius='lg', variant='filled', color='warning', banner=False, icon=True, closable=True,key='31')
    sac.alert(label='Perimeter Intrusion', description='Alert Generated', radius='lg', variant='filled', color='warning', banner=False, icon=True, closable=True,key='32')

with col2:
    #st.subheader('Safety Alerts')
    sac.alert(label='**Safety Alerts**',variant='quote-light')
    sac.alert(label='Perimeter Intrusion', description='Alert Generated', radius='lg', variant='filled', color='warning', banner=False, icon=True, closable=True,key='4')
    sac.alert(label='Perimeter Intrusion', description='Alert Generated', radius='lg', variant='filled', color='warning', banner=False, icon=True, closable=True,key='5')
    sac.alert(label='Perimeter Intrusion', description='Alert Generated', radius='lg', variant='filled', color='warning', banner=False, icon=True, closable=True,key='6')
    sac.alert(label='Perimeter Intrusion', description='Alert Generated', radius='lg', variant='filled', color='warning', banner=False, icon=True, closable=True,key='61')
    sac.alert(label='Perimeter Intrusion', description='Alert Generated', radius='lg', variant='filled', color='warning', banner=False, icon=True, closable=True,key='62')


with col3:
    #st.subheader('Other Alerts')
    sac.alert(label='**Other Alerts**',variant='quote-light')
    sac.alert(label='Perimeter Intrusuin', description='Alert Generated', radius='lg', variant='filled', color='warning', banner=False, icon=True, closable=True,key='7')
    sac.alert(label='Perimeter Intrusuin', description='Alert Generated', radius='lg', variant='filled', color='warning', banner=False, icon=True, closable=True,key='8')
    sac.alert(label='Perimeter Intrusuin', description='Alert Generated', radius='lg', variant='filled', color='warning', banner=False, icon=True, closable=True,key='9')
    sac.alert(label='Perimeter Intrusuin', description='Alert Generated', radius='lg', variant='filled', color='warning', banner=False, icon=True, closable=True,key='91')
    sac.alert(label='Perimeter Intrusuin', description='Alert Generated', radius='lg', variant='filled', color='warning', banner=False, icon=True, closable=True,key='92')
    #with stylable_container(key="blue_button",css_styles="""button {background-color: #85929E;color: white;border-radius: 20px;}""",):
    #    st.link_button("View details", "http://localhost:8501/Manage_Incidents",use_container_width=True)

st.divider()
sac.pagination(total=30, page_size=8, align='center', radius='xs', variant='light', jump=True,color='lime')



st.markdown(set_cfg.footer, unsafe_allow_html=True)




#st.text(time.time())


#st.header('Alerts')
#st.divider()
#
#col1,col2,col3,col4,col5,col6=st.columns(6)
#
#
#def _customize_css_style():
#    # Note padding is top right bottom left
#    st.markdown(
#        """
#        <style>
#            div[data-testid=stToast] {
#                padding:  20px 10px 40px 10px;
#                margin: 10px 10px 10px 10px;
#                background-color: #ffffff;
#                width: 30%;
#            }
#             
#            [data-testid=toastContainer] [data-testid=stMarkdownContainer] > p {
#                font-size: 20px; font-style: normal; font-weight: 400;
#                foreground-color: #ffffff;
#            }
#        </style>
#        """, unsafe_allow_html=True
#    )
#
#
#_customize_css_style()
#
#if st.button('Click here'):
#    st.toast('This is a toast notification 1')
#    time.sleep(1)
#    st.toast('This is a toast notification 2')
#    time.sleep(1)
#    st.toast('This is a toast notification 3')
#    time.sleep(1)
#    st.toast('This is a toast notification')
#
#














