import streamlit as st
import uuid


from model import Caexfile, CaexfileSystemUnitClassLib, SystemUnitClassType, AttributeInstance, CaexfileInstanceHierarchy, InternalElementType, InternalElementTypeRoleRequirements

new_file = Caexfile(file_name="Motorfile.aml")

new_file.system_unit_class_lib.append(
    CaexfileSystemUnitClassLib(name="MotorLib"))

motor_lib = new_file.system_unit_class_lib[0]

motor_lib.system_unit_class.append(SystemUnitClassType(
    name="Drive",
    id="1234",
    ref_base_class_path="AutomationMLBaseRoleClassLib/AutomationMLBaseRole/Resource",
    attribute=[
        AttributeInstance(name="internal_id"),
        AttributeInstance(name="name"),
        AttributeInstance(name="velocity"),
    ])
)

attribute_list = ["internal_id", "name", "num_of_axis"]

control = SystemUnitClassType(name="Control")
control.ref_base_class_path = "AutomationMLBaseRoleClassLib/AutomationMLBaseRole/Resource"

motor_lib.system_unit_class.append(control)

for attribute_name in attribute_list:
    new_attribute = AttributeInstance(name=attribute_name)
    control.attribute.append(new_attribute)


mapping_dict = [
    {
        "key": "denomination",
        "evaluator": "contains",
        "value": "Drive Control",
        "class": "Control",
        "attributes": [
            {
                
                "achs-diameter": "Achs-ø",
            }
        ]
    },
    {
        "key": "denomination",
        "evaluator": "contains",
        "value": "Drive",
        "class": "Drive",
    },
]

raw_data_payload = [
    {
        "id": "PS_SubS_UMC_VAP_P1_CD1_D1",
        "denomination": "Drive01",
    },
    {"id": "PS_SubS_UMC_VAP_P1_CD1_D2",
     "denomination": "Drive Control01",
     }
]

class_path_dict = {
    "Control": "MotorLib/Control",
    "Drive": "MotorLib/Drive",
}

new_ih = CaexfileInstanceHierarchy(name="MotorenListe")
for object in raw_data_payload:
    for mapping_strategy in mapping_dict:
        mapping_key = mapping_strategy["key"]
        mapping_evaluator = mapping_strategy["evaluator"]
        mapping_value = mapping_strategy["value"]
        mapping_class = mapping_strategy["class"]

        if object[mapping_key]:
            st.success("Found key")
            if mapping_evaluator == "contains":
                if mapping_value in object[mapping_key]:
                    st.write(class_path_dict[mapping_class])
                    new_ie = InternalElementType(
                        name=object[mapping_key], 
                        id=str(uuid.uuid4()), 
                    )
                    new_ie.role_requirements.append(InternalElementTypeRoleRequirements(ref_base_role_class_path=class_path_dict[mapping_class]))
                    new_ih.internal_element.append(new_ie)
                    break
# st.write(new_ih)
# st.write(new_ih.__dict__)   

new_file.instance_hierarchy.append(new_ih)


st.write(new_file)
st.write(new_file.__dict__)  # This is the dict that will be converted to JSON

# st.write(motor_lib)
# st.write(motor_lib.__dict__)  # This is the dict that will be converted to JSON

# st.write(control)
# st.write(control.__dict__)  # This is the dict that will be converted to JSON
