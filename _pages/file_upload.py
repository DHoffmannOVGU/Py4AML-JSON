import streamlit as st
from model import Caexfile
from utils import parser_definition, json_optimizer, json_unabbreviate
import json


def show_file_overview():
    json_string: str = json.dumps(st.session_state["aml_dict"], indent=None)
    byte_length: float = round(len(json_string), -3)
    json_size = byte_length / 1000
    st.session_state["json_size"] = json_size
    delta = ((byte_length / 1000) / float(st.session_state['raw_data_size']) - 1) * 100
    rounded_delta = round(delta, 2)
    st.session_state["json_string"] = json_string
    st.success(
        "AML file successfully uploaded, please go through the next steps to optimize your file or directly "
        "download below")

    col1, col2, col3 = st.columns([2, 1, 1])
    col1.metric("File name", st.session_state["file_name"])
    col2.metric("AML file size", f"{st.session_state['raw_data_size']} KB")
    col3.metric("JSON file size", f"~{json_size} KB", delta=f"{rounded_delta} % ", delta_color="inverse")

    st.download_button("Download converted AML-JSON File", file_name=f"{st.session_state['file_name']}.json",
                       mime="application/json", data=st.session_state["json_string"], type="primary",
                       use_container_width=True, key="direct_download_button")


def file_upload():
    context, parser, json_parser, xml_serializer, json_serializer = parser_definition()
    # File Upload section
    raw_data = st.file_uploader("Upload AML file or JSON file here")
    if raw_data is not None:
        st.session_state["file_name"] = raw_data.name[:-4]
        st.session_state["raw_data_size"] = raw_data.size / 1000
        if raw_data.type == "text/xml" or raw_data.type == "application/octet-stream":
            bytes_data = raw_data.getvalue()
            st.session_state["raw_data"] = bytes_data
            try:
                # XSDATA
                aml_object: Caexfile = parser.from_string(str(bytes_data, 'utf-8'), Caexfile)
                st.session_state["aml_object"] = aml_object
                st.session_state["type"] = "XML"
            except Exception as e:
                print(e)
                st.warning("Schmema-based converter failed")
                st.warning("Please provide AML files build with the CAEX 3.0 schema")

        elif raw_data.type == "application/json":
            dict_data = json.load(raw_data)
            st.session_state["raw_data"] = dict_data
            st.session_state["aml_object"] = dict_data
            st.session_state["type"] = "JSON"

        else:
            st.info("Upload AML or JSON file to convert")

    if st.session_state["aml_object"] is not None:
        if st.session_state["type"] == "XML":
            try:
                aml_xs_json_string = json_serializer.render(st.session_state["aml_object"])
                aml_xsdict = json.loads(aml_xs_json_string)
                optimized_dict = json_optimizer(aml_xsdict)
                st.session_state["aml_dict"] = optimized_dict
                show_file_overview()
            except Exception as e:
                print(e)
                st.warning("Schmema-based converter failed")
                st.warning("Please provide AML files build with the CAEX 3.0 schema")

        elif st.session_state["type"] == "JSON":
            st.json(st.session_state["aml_object"], expanded=False)
            full_json = json_unabbreviate(st.session_state["aml_object"])
            xml_object: Caexfile = json_parser.bind_dataclass(full_json, Caexfile)
            xml_string = xml_serializer.render(xml_object)
            st.success("JSON file successfully converted to AML, Download file below")
            st.download_button(
                "Download converted AML (.aml) File",
                file_name=f"{st.session_state['file_name']}.aml",
                mime="text/xml",
                data=xml_string,
                use_container_width=True,
                key="download_button3"
            )