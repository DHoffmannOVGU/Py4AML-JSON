import streamlit as st
from PIL import Image
import streamlit_antd_components as sac 
from _pages import file_upload, check_conversion, optimize_storage, download

# Load AML and header images
aml_image = Image.open('./aml_logo.png')
aml_header_logo = Image.open('./aml_header_logo.png')
aml_json_logo = Image.open('./aml_json_logo.png')

# Initialize Streamlit page configuration
st.set_page_config(page_title="AML-JSON Converter", page_icon=aml_image, initial_sidebar_state='expanded', layout='wide')

# Page header and title
st.image(aml_json_logo, width=500)

session_state_dict = {
    "aml_object": None,
    "raw_data": None,
    "json_size": None,
    "aml_dict": None,
    "optimized_yaml_string": None,
    "optimized_json_string": None,
    "optimized_dict": None,
    "aml_dict": None,
}

for key, value in session_state_dict.items():
    if key not in st.session_state:
        st.session_state[key] = value

page_dict ={
    "Upload JSON or AML File": file_upload,
    "Check JSON conversion": check_conversion,
    "Optimize storage Size": optimize_storage,
    "Download JSON": download,

}

nav_items = list(page_dict.keys())

# Navigation steps
nav_step = sac.steps(nav_items)

# Page navigation
page = page_dict[nav_step]()
