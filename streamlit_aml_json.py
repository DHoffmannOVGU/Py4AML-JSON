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
    "Upload AML File": file_upload,
    "Upload JSON File": file_upload,
    "Check JSON conversion": check_conversion,
    "Optimize storage Size": optimize_storage,
    "Download JSON": download,
}

mode = sac.segmented(
    items=[
        sac.SegmentedItem(label='AML to JSON', icon='file-code'),
        sac.SegmentedItem(label='JSON to AML', icon='file-text'),
    ],
    label='Select Mode',
    align='center',
    use_container_width=True
)

if mode == 'AML to JSON':
    nav_items = ["Upload AML File", "Check JSON conversion", "Optimize storage Size", "Download JSON"]
elif mode == 'JSON to AML':
    nav_items = ["Upload JSON File"]


# Navigation steps
nav_step = sac.steps(nav_items)

# Page navigation
page = page_dict[nav_step]()
