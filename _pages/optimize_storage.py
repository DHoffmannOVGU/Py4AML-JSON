import streamlit as st
from utils import json_optimizer_combined
import bson
import json


def optimize_storage():
    import streamlit_antd_components as sac

    if "optimized_dict" not in st.session_state:
        st.session_state["optimized_dict"] = None

    if "optimized_json_string" not in st.session_state:
        st.session_state["optimized_json_string"] = None


    with st.expander("Optimization Settings", expanded=True):
        with st.container(border=True):
            descr_col, settings_col = st.columns([1, 2])
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

            descr_col, settings_col = st.columns([1, 2])
            descr_col.subheader("Binary encode JSON")
            with settings_col:
                binary_encode_seg = sac.segmented([
                    sac.SegmentedItem(label='No'),
                    sac.SegmentedItem(label='Yes'),
                ], align='center', key="binary_encode", use_container_width=True)
            if binary_encode_seg == "Yes":
                binary_encode = True
            else:
                binary_encode = False

        execute_optimization = st.button("Execute optimization", key="execute_optimization",
                                         use_container_width=True, type="primary")

        if execute_optimization:
            optimized_dict = json_optimizer_combined(st.session_state["aml_dict"], clean=True,
                                                     abbreviate=abbreviate)
            st.session_state["optimized_dict"] = optimized_dict
            st.json(optimized_dict, expanded=False)
            if binary_encode:
                binary_aml = bson.BSON.encode(optimized_dict)
                st.write(binary_aml)


    if st.session_state["optimized_dict"] is not None:
        optimized_json_string: str = json.dumps(st.session_state["optimized_dict"], indent=None)
        byte_length: float = len(optimized_json_string)
        delta = ((byte_length / 1000) / float(st.session_state['raw_data_size']) - 1) * 100
        rounded_delta = round(delta, 2)
        st.metric("File size", f"{byte_length / 1000} KB", delta=f"{rounded_delta} % ", delta_color="inverse")
        st.session_state["optimized_json_string"] = optimized_json_string

    try:
        binary_dict_string = str(binary_aml)
        byte_length: float = len(binary_dict_string)
        delta = ((byte_length / 1000) / float(st.session_state['raw_data_size']) - 1) * 100
        rounded_delta = round(delta, 2)
        st.metric("File size", f"{byte_length / 1000} KB", delta=f"{rounded_delta} % ", delta_color="inverse")
    except:
        pass
