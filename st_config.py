### SYSTEM VARIABLES - DO NOT MAKE CHANGES TO BELOW VARIABLES  ###
import base64

img_data = open('logo_new.png', "rb").read()
encoded_image = base64.b64encode(img_data).decode("utf-8")

class set_cfg(object):
    footer = """
    <style>
    a:link , a:visited{
    color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
    background-color: transparent;
    text-decoration: none;
    }
    
    a:hover,  a:active {
    color: #0283C3; /* theme's primary color*/
    background-color: transparent;
    text-decoration: underline;
    }
    
    #page-container {
      position: relative;
      min-height: 10vh;
    }
    
    footer{
        visibility:hidden;
    }
    
    .footer {
    position: relative;
    left: 0;
    top:230px;
    bottom: 0;
    width: 100%;
    background-color: transparent;
    color: #808080; /* theme's text color hex code at 50 percent brightness*/
    text-align: center; /* you can replace 'left' with 'center' or 'right' if you want*/
    }
    </style>
    
    <div id="page-container">
    
    <div class="footer">
    <p style='font-size: 0.875em;'>© 2023. Ahana Systems and Solutions Private Limited </p>
    </div>
    
    </div>
    """
    
    hide_bar= """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            visibility:hidden;
            width: 0px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            visibility:hidden;
        }
        </style>
    """

    show_bar= """
        <style>
        [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
            visibility:visible;
            width: 350px;
        }
        [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
            visibility:visible;
        }
        </style>
    """

    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """    
    
    ahana_logo= """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url("data:image/png;base64,%s");
                background-repeat: no-repeat;
                padding-top: 0px;
                background-position: 0px 0px;
                background-size: 335px 115px;
                top: 13px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """% encoded_image

    hide_deploy_btn="""
    <style>
       .reportview-container {
           margin-top: -2em;
       }
       #MainMenu {visibility: hidden;}
       .stDeployButton {display:none;}
       footer {visibility: hidden;}
       #stDecoration {display:none;}
    </style>"""


    st_tabs="""
    <style>

	.stTabs [data-baseweb="tab-list"] {
		gap: 2px;
    }

	.stTabs [data-baseweb="tab"] {
		height: 5px;
        white-space: pre-wrap;
		background-color: #F0F2F6;
		border-radius: 4px 4px 0px 0px;
		gap: 1px;
		padding-top: 10px;
		padding-bottom: 10px;
    }

	.stTabs [aria-selected="true"] {
  		background-color: #FFFFFF;
	}

    </style>"""

    hide_img_fs = '''
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
    '''

    antd_rem_scpace='''
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
    '''