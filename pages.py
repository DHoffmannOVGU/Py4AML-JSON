import streamlit as st
from model import Caexfile
from utils import parser_definition, json_optimizer_combined, json_optimizer
import json
import bson


def file_upload_page():
    def show_file_overview():
        json_string: str = json.dumps(st.session_state["aml_dict"], indent=None)
        byte_length: float = round(len(json_string), -3)
        json_size = byte_length / 1000
        st.session_state["json_size"] = json_size
        delta = ((byte_length/1000)/float(st.session_state['raw_data_size'])-1)*100
        rounded_delta = round(delta, 2)
        st.session_state["json_string"] = json_string
        st.success("AML file successfully uploaded, please go through the next steps to optimize your file or directly download below") 

        col1, col2, col3= st.columns([2, 1, 1])
        col1.metric("File name", st.session_state["file_name"])
        col2.metric("AML file size", f"{st.session_state['raw_data_size']} KB")
        col3.metric("JSON file size", f"~{json_size} KB", delta=f"{rounded_delta} % ", delta_color="inverse")
        
        st.download_button("Download converted AML-JSON File", file_name=f"{st.session_state['file_name']}.json", mime="application/json", data=st.session_state["json_string"], type="primary",  use_container_width=True, key="direct_download_button")


    if "aml_object" not in st.session_state:
        st.session_state["aml_object"] = None
    if "raw_data" not in st.session_state:
        st.session_state["raw_data"] = None
    if "json_size" not in st.session_state:
        st.session_state["json_size"] = None
    if "aml_dict" not in st.session_state:
        st.session_state["aml_dict"] = None

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
            xml_object: Caexfile = json_parser.bind_dataclass(st.session_state["aml_object"], Caexfile)
            xml_string = xml_serializer.render(xml_object)
            st.success("JSON file successfully converted to AML, Download file below")
            st.download_button("Download converted AML (.aml) File", file_name=f"{st.session_state['file_name']}.aml", mime="text/xml", data=xml_string, use_container_width=True, key="download_button3")


def check_conversion():
    import streamlit_antd_components as sac

    nav_column, json_column = st.columns([3, 5])
    with nav_column:
        filter_item = sac.segmented(
            items=[
                sac.SegmentedItem(label='Whole file'),
                sac.SegmentedItem(label='Header Information'),
                sac.SegmentedItem(label='Instance Hierarchy'),
                sac.SegmentedItem(label='SystemUnitClass Library'),
                sac.SegmentedItem(label='RoleClass Library'),
                sac.SegmentedItem(label='Interface Class Library'),
                sac.SegmentedItem(label='AttributeType Library'),
            ], align='center', use_container_width=True, direction="vertical"
        )

    keys_of_interest_dict = {
        "Header Information": ["SchemaVersion", "FileName", "Revision", "RevisionDate", "OldVersion", "NewVersion", "AuthorName", "AdditionalInformation"],
        "Instance Hierarchy": ["InstanceHierarchy"],
        "SystemUnitClass Library": ["SystemUnitClassLib"],
        "RoleClass Library": ["RoleClassLib"],
        "Interface Class Library": ["InterfaceClassLib"],
        "AttributeType Library": ["AttributeTypeLib"],
    }

    with json_column:
        aml_xsdict = st.session_state["aml_dict"]
        st.info("Click the 3 dots to expand the file")
        if filter_item == "Whole file":
            st.json(aml_xsdict, expanded=False)

        else:
            partial_dict = {key: aml_xsdict[key] for key in keys_of_interest_dict[filter_item] if key in aml_xsdict}
            st.json(partial_dict, expanded=False)

def optimize_storage():
    import streamlit_antd_components as sac

    if "optimized_dict" not in st.session_state:
        st.session_state["optimized_dict"] = None
    
    if "optimized_json_string" not in st.session_state:
        st.session_state["optimized_json_string"] = None

    with st.expander("Optimization Settings", expanded=True):
        with st.container(border=True):
            descr_col, settings_col = st.columns([1,2])
            descr_col.subheader("Abbreviation settings")
            with settings_col:
                abbreviate_seg = sac.segmented([
                    sac.SegmentedItem(label='No'),
                    sac.SegmentedItem(label='Yes, string abbreviations'),
                    sac.SegmentedItem(label='Yes, number abbreviations'),
                ], align='center', use_container_width=True, key="abbreviate")
            if abbreviate_seg == "Yes, string abbreviations":
                abbreviate = 1
            elif abbreviate_seg == "Yes, number abbreviations":
                abbreviate = 2
            else:
                abbreviate = 0
        
        with st.container(border=True):

            descr_col, settings_col = st.columns([1,2])
            descr_col.subheader("Binary encode JSON")
            with settings_col:
                binary_encode_seg = sac.segmented([
                    sac.SegmentedItem(label='No'),
                    sac.SegmentedItem(label='Yes'),
                ], align='center', key="binary_encode", use_container_width=True, disabled=True)
            if binary_encode_seg == "Yes":
                binary_encode = True
            else:
                binary_encode = False
        

        execute_optimization = st.button("Execute optimization", key="execute_optimization", use_container_width=True, type="primary")

        if execute_optimization:
            optimized_dict = json_optimizer_combined(st.session_state["aml_dict"], clean=True, abbreviate=abbreviate)
            st.session_state["optimized_dict"] = optimized_dict
            st.json(optimized_dict, expanded=False)
            if binary_encode:
                binary_aml = bson.BSON.encode(optimized_dict)
                st.write(binary_aml)

    if st.session_state["optimized_dict"] is not None:
        optimized_json_string: str = json.dumps(st.session_state["optimized_dict"], indent=None)
        byte_length: float = len(optimized_json_string)
        delta = ((byte_length/1000)/float(st.session_state['raw_data_size'])-1)*100
        rounded_delta = round(delta, 2)
        st.session_state["optimized_json_string"] = optimized_json_string

        delta = ((byte_length/1000)/float(st.session_state['raw_data_size'])-1)*100
        rounded_delta = round(delta, 2)
        normal_delta = (st.session_state['json_size']/float(st.session_state['raw_data_size'])-1)*100
        normal_delta = round(normal_delta, 2)

        with st.container(border=True):
            col1, col2, col3= st.columns([1, 1, 1])
            col1.metric("AML file size", f"{st.session_state['raw_data_size']} KB")
            col2.metric("Without optimization", f"~{st.session_state['json_size']} KB", delta=f"{normal_delta} % ", delta_color="inverse")
            col3.metric("With optimization", f"{byte_length / 1000} KB", delta=f"{rounded_delta} % ", delta_color="inverse")



def download_page():
    st.success("AML file successfully converted to JSON, Download file below")
    filename = st.text_input("Enter file name", st.session_state["file_name"])
    if st.session_state["optimized_json_string"] is not None:
        st.download_button("Download converted AML-JSON File", file_name=f"{filename}.json", mime="application/json", data=st.session_state["optimized_json_string"], use_container_width=True, key="download_button2")
    else:
        st.download_button("Download converted AML-JSON File", file_name=f"{filename}.json", mime="application/json", data=st.session_state["json_string"], use_container_width=True, key="download_button2", type="primary")
