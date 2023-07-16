import streamlit as st
import xmltodict
import json
from PIL import Image

from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers import XmlParser, JsonParser
from xsdata.formats.dataclass.serializers import XmlSerializer, JsonSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig

from aml_base import Caexfile

# Utility function to optimize JSON dictionary
def json_optimizer(aml_dict: dict):
    for key, value in aml_dict.copy().items():
        if value is None or value == "" or value == "Null" or value == "None":
            del aml_dict[key]
        elif isinstance(value, list):
            if value:
                new_value_list = []
                for entry in value:
                    if isinstance(entry, str):
                        pass
                    elif isinstance(entry, dict):
                        new_value_list.append(json_optimizer(entry))
            else:
                del aml_dict[key]
        elif isinstance(value, dict):
            value = json_optimizer(value)
    return aml_dict

# Load AML and header images
aml_image = Image.open('./aml_logo.png')
aml_header_logo = Image.open('./aml_header_logo.png')

# Initialize Streamlit page configuration
st.set_page_config(page_title="AML-JSON Converter", page_icon=aml_image, initial_sidebar_state='collapsed', layout='wide')

# Create XML context, parser, and serializer
context = XmlContext()
parser = XmlParser(context=context)
json_parser = JsonParser(context=context)
xml_serializer = XmlSerializer(context=context)

# Page header and title
st.image(aml_header_logo)
st.title("AML-JSON Converter")

# File Upload section
st.header("File Upload")
raw_data = st.file_uploader("Upload AML file")

# Converter comparison section
st.header("Converter comparison")

if raw_data is not None:
    if raw_data.type == "text/xml" or raw_data.type == "application/octet-stream":
        bytes_data = raw_data.getvalue()

        try:
            # XMLDICT
            dict_data = xmltodict.parse(bytes_data)
            st.session_state["xmltodict_dict"] = dict_data
            st.session_state["type"] = "XML"
        except Exception as e:
            print(e)

        try:
            # XSDATA
            aml_object: Caexfile = parser.from_string(str(bytes_data, 'utf-8'), Caexfile)
            st.session_state["aml_object"] = aml_object
            st.session_state["type"] = "XML"
        except Exception as e:
            print(e)

    if raw_data.type == "application/json":
        dict_data = json.load(raw_data)
        st.session_state["aml_object"] = dict_data
        st.session_state["type"] = "JSON"

if st.session_state.get("type") == "XML":
    xml_tab, xml_to_dict_tab, xs_data_tab, optimized_tab = st.tabs(["AML data check", "Simple JSON-Converter", "Schema-based converter", "Optimized Converter (experimental))"])

    try:
        with xml_tab:
            # File metadata
            st.write(raw_data)
            st.session_state["file_name"] = raw_data.name[:-4]
            st.session_state["raw_data_size"] = raw_data.size / 1000
            col1, col2, col3 = st.columns([2, 1, 1])
            col1.metric("File name", st.session_state["file_name"])
            col2.metric("Data format", ".aml")
            col3.metric("File size", f"{st.session_state['raw_data_size']} KB")

            st.success("AML file successfully uploaded, please select a converter tab to continue")

            with st.expander("Show XMLDICT data"):
                st.json(dict_data, expanded=False)

            try:
                with st.expander("Show XS Data AML data"):
                    st.write(aml_object)
            except Exception as e:
                print(e)
                st.warning("Schmema-based converter failed, please use the simple converter instead")
                st.warning("Please provide AML files build with the CAEX 3.0 schema")

        with xml_to_dict_tab:
            bool_column, specific_column = st.columns([1, 5])

            # Indentation settings
            indent = bool_column.checkbox("Indent file?")
            if indent:
                indent_slider = specific_column.slider("Indentation", 0, 4)
                indent_value = indent_slider
            else:
                indent_slider = specific_column.slider("Indentation", 0, 4, disabled=True)
                indent_value = None

            dict_string: str = json.dumps(dict_data, indent=indent_value)
            byte_length: float = len(dict_string)
            delta = ((byte_length/1000)/float(st.session_state['raw_data_size'])-1)*100
            rounded_delta = round(delta, 2)
            col1, col2, col3 = st.columns([2, 1, 1])
            col1.metric("File name", st.session_state["file_name"])
            col2.metric("Data format", ".json")
            col3.metric("File size", f"{byte_length / 1000} KB", delta=f"{rounded_delta} % ", delta_color="inverse")
            with st.expander("Show JSON"):
                st.json(dict_data, expanded=False)
                st.session_state["xmltodict_dict"] = dict_data

            st.success("AML file successfully converted to JSON, Download file below")
            st.download_button("Download converted AML-JSON File", file_name=f"{st.session_state['file_name']}.json", mime="application/json", data=dict_string, use_container_width=True)

        with xs_data_tab:
            bool_column, specific_column = st.columns([1, 5])

            # Indentation settings
            indent = bool_column.checkbox("Indent file?", key="indent2")
            if indent:
                indent_slider = specific_column.slider("Indentation", 0, 4, key="indent_slider2")
                indent_value = indent_slider
            else:
                indent_slider = specific_column.slider("Indentation", 0, 4, disabled=True, key="indent_slider2")
                indent_value = None

            config = SerializerConfig(pretty_print=False, ignore_default_attributes=True)
            json_serializer = JsonSerializer(context=XmlContext(), config=config, indent=indent_value)
            aml_xs_json_string = json_serializer.render(st.session_state["aml_object"])
            aml_xsdict = json.loads(aml_xs_json_string)

            cleaned_aml = json_optimizer(aml_xsdict)

            with st.expander("Show Uncleaned JSON"):
                st.json(aml_xsdict, expanded=False)

            with st.expander("Show JSON"):
                st.json(cleaned_aml, expanded=False)

            cleaned_json: str = json.dumps(cleaned_aml, indent=indent_value)
            byte_length: float = len(cleaned_json)
            delta = ((byte_length/1000)/float(st.session_state['raw_data_size'])-1)*100
            rounded_delta = round(delta, 2)
            col1, col2, col3 = st.columns([2, 1, 1])
            col1.metric("File name", st.session_state["file_name"])
            col2.metric("Data format", ".json")
            col3.metric("File size", f"{byte_length / 1000} KB", delta=f"{rounded_delta} % ", delta_color="inverse")

            st.success("AML file successfully converted to JSON, Download file below")
            st.download_button("Download converted AML-JSON File", file_name=f"{st.session_state['file_name']}.json", mime="application/json", data=cleaned_json, use_container_width=True, key="download_button2")

        with optimized_tab:
            abbreviate = bool_column.checkbox("Abbreviate keys?")

    except Exception as e:
        print(e)
        st.info("Upload AML file to convert")

elif st.session_state.get("type") == "JSON":
    aml_object: Caexfile = json_parser.bind_dataclass(st.session_state["aml_object"], Caexfile)
    xml_string = xml_serializer.render(aml_object)
    st.success("JSON file successfully converted to AML, Download file below")
    st.download_button("Download converted AML (.aml) File", file_name=f"{st.session_state['file_name']}.aml", mime="text/xml", data=xml_string, use_container_width=True, key="download_button3")

else:
    st.info("Upload AML file to convert")
