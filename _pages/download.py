import streamlit as st
import yaml


def download():
    st.success("AML file successfully converted to JSON, Download file below")
    filename = st.text_input("Enter file name", st.session_state["file_name"])
    # st.checkbox("Add timestamp to file name as suffix")
    # st.checkbox("Zip file?")
    yaml_check = st.checkbox("Output as YAML")
    if st.session_state["optimized_json_string"] is not None:
        if yaml_check:
            yaml_string = yaml.dump(st.session_state["optimized_dict"], default_flow_style=False)
            st.write(yaml_string)
            st.session_state["optimized_yaml_string"] = yaml_string
            st.download_button("Download converted AML-YAML File", file_name=f"{filename}.yaml",
                               mime="application/yaml", data=st.session_state["optimized_yaml_string"],
                               use_container_width=True, key="download_button1", type="primary")

        else:
            st.download_button("Download converted AML-JSON File",
                               file_name=f"{filename}.json",
                               mime="application/json",
                               data=st.session_state["optimized_json_string"],
                               use_container_width=True,
                               key="download_button2",
                               type="primary")
    else:
        if yaml_check:
            yaml_string = yaml.dump(st.session_state["aml_dict"], default_flow_style=False)
            st.session_state["optimized_yaml_string"] = yaml_string
            st.download_button("Download converted AML-YAML File", file_name=f"{filename}.yaml",
                               mime="application/yaml", data=st.session_state["optimized_yaml_string"],
                               use_container_width=True, key="download_button1", type="primary")


        else:
            st.download_button("Download converted AML-JSON File",
                               file_name=f"{filename}.json",
                               mime="application/json",
                               data=st.session_state["json_string"],
                               use_container_width=True,
                               key="download_button2",
                               type="primary")
