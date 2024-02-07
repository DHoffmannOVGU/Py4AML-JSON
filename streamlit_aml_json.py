import streamlit as st
from PIL import Image
import streamlit_antd_components as sac 
from pages import file_upload_page, check_conversion, optimize_storage, download_page

# Load AML and header images
aml_image = Image.open('./aml_logo.png')
aml_header_logo = Image.open('./aml_header_logo.png')
aml_json_logo = Image.open('./aml_json_logo.png')

# Initialize Streamlit page configuration
st.set_page_config(page_title="AML-JSON Converter", page_icon=aml_image, initial_sidebar_state='expanded', layout='wide')

# Page header and title
st.image(aml_json_logo, width=500)

# Navigation steps
steps = sac.steps(
    items=[
        sac.StepsItem(title='Upload JSON or AML File'),
        sac.StepsItem(title='Check JSON conversion'),
        sac.StepsItem(title='Optimize storage Size'),
        sac.StepsItem(title='Download JSON'),
    ], 
)

if steps == "Upload JSON or AML File":
    file_upload_page()

elif steps == "Check JSON conversion":
    check_conversion()

elif steps == "Optimize storage Size":
    optimize_storage()

#     st.success("AML file successfully converted to JSON, Download file below")
#     st.download_button("Download converted AML-JSON File", file_name=f"{st.session_state['file_name']}.json", mime="application/json", data=cleaned_json, use_container_width=True, key="download_button2")


elif steps == "Download JSON":
    download_page()
       
