from dataclasses import field
from enum import Enum

from pydantic import root_validator, Field
from pydantic.dataclasses import dataclass
from typing import List, Optional, Dict, Any, Union
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.dke.de/CAEX"


@dataclass
class AttributeValueRequirementTypeNominalScaledType:
    """
    :ivar required_value: Element to define a required value of an
        attribute. It may be defined multiple times in order to define a
        discrete value range of the attribute.
    """
    class Meta:
        global_type = False

    required_value: List[str] = field(
        default_factory=list,
        metadata={
            "name": "RequiredValue",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


@dataclass
class AttributeValueRequirementTypeOrdinalScaledType:
    """
    :ivar required_max_value: Element to define a maximum value of an
        attribute.
    :ivar required_value: Element to define a required value of an
        attribute.
    :ivar required_min_value: Element to define a minimum value of an
        attribute.
    """
    class Meta:
        global_type = False

    required_max_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequiredMaxValue",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    required_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequiredValue",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    required_min_value: Optional[str] = field(
        default=None,
        metadata={
            "name": "RequiredMinValue",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


@dataclass
class AttributeValueRequirementTypeUnknownType:
    """
    :ivar requirements: Defines informative requirements as a constraint
        for an attribute value.
    """
    class Meta:
        global_type = False

    requirements: Optional[str] = field(
        default=None,
        metadata={
            "name": "Requirements",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


class ChangeMode(Enum):
    STATE = "state"
    CREATE = "create"
    DELETE = "delete"
    CHANGE = "change"


@dataclass
class HeaderRevision:
    class Meta:
        global_type = False

    revision_date: Optional[str] = field(
        default=None,
        metadata={
            "name": "RevisionDate",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
            "required": True,
        }
    )
    old_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "OldVersion",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    new_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "NewVersion",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    author_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "AuthorName",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
            "required": True,
        }
    )
    comment: Optional[str] = field(
        default=None,
        metadata={
            "name": "Comment",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


@dataclass
class HeaderSourceObjectInformation:
    """
    :ivar value:
    :ivar origin_id: This attribute describes the ID of the origin of
        the belonging object, e.g. a source engineering tool. The value
        is according to the vendor specific OriginID.
    :ivar source_obj_id: Optional attribute representing the ID of the
        source object in the source data model.
    """
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    origin_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginID",
            "type": "Attribute",
            "required": True,
        }
    )
    source_obj_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SourceObjID",
            "type": "Attribute",
        }
    )


@dataclass
class SourceDocumentInformationType:
    """
    Defines a structure to model information about the data source of the
    present CAEX document.

    :ivar origin_name: Name of the origin of the CAEX document, e.g. the
        source engineering tool or an exporter software
    :ivar origin_id: Unique identifier of the origin of the CAEX
        document, e.g. a unique identifier of a source engineering tool
        or an exporter software. The ID shall not change even if the
        origin gets renamed.
    :ivar origin_vendor: Optional: the vendor of the data source of the
        CAEX document
    :ivar origin_vendor_url: Optional: the vendors URL of the data
        source of the CAEX document
    :ivar origin_version: Version of the origin of the CAEX document,
        e.g. the version of the source engineering tool or the exporter
        software.
    :ivar origin_release: Optional: release information of the origin of
        the CAEX document, e.g. the version of the source engineering
        tool or the exporter software.
    :ivar last_writing_date_time: Date and time of the creation of the
        CAEX document.
    :ivar origin_project_title: Optional: the title of the corresponding
        source project
    :ivar origin_project_id: Optional: a unique identifier of the
        corresponding source project
    """
    origin_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginName",
            "type": "Attribute",
            "required": True,
        }
    )
    origin_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginID",
            "type": "Attribute",
            "required": True,
        }
    )
    origin_vendor: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginVendor",
            "type": "Attribute",
        }
    )
    origin_vendor_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginVendorURL",
            "type": "Attribute",
        }
    )
    origin_version: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginVersion",
            "type": "Attribute",
            "required": True,
        }
    )
    origin_release: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginRelease",
            "type": "Attribute",
        }
    )
    last_writing_date_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "LastWritingDateTime",
            "type": "Attribute",
            "required": True,
        }
    )
    origin_project_title: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginProjectTitle",
            "type": "Attribute",
        }
    )
    origin_project_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "OriginProjectID",
            "type": "Attribute",
        }
    )


@dataclass
class HeaderCopyright:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    change_mode: ChangeMode = field(
        default=ChangeMode.STATE,
        metadata={
            "name": "ChangeMode",
            "type": "Attribute",
        }
    )


@dataclass
class HeaderDescription:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    change_mode: ChangeMode = field(
        default=ChangeMode.STATE,
        metadata={
            "name": "ChangeMode",
            "type": "Attribute",
        }
    )


@dataclass
class HeaderVersion:
    class Meta:
        global_type = False

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
    change_mode: ChangeMode = field(
        default=ChangeMode.STATE,
        metadata={
            "name": "ChangeMode",
            "type": "Attribute",
        }
    )

@dataclass
class AdditionalInformation:
    __root__: str = field(default_factory=str)



@dataclass(kw_only=True)
class CaexbasicObject:
    """
    CAEX basis object that comprises a basic set of attributes and header
    information which exist for all CAEX elements.

    :ivar description: Textual description for CAEX objects.
    :ivar version: Organizational information about the state of the
        version.
    :ivar revision: Organizational information about the state of the
        revision.
    :ivar copyright: Organizational information about copyright.
    :ivar additional_information: Optional auxiliary field that may
        contain any additional information about a CAEX object.
    :ivar source_object_information: Organizational information about
        the source of the corresponding CAEX object.
    :ivar change_mode: Optionally describes the change state of a CAEX
        object. If used, the ChangeMode shall have the following value
        range: state, create, delete and change. This information should
        be used for further change management applications.
    """
    class Meta:
        name = "CAEXBasicObject"

    additional_information: List[AdditionalInformation] = field(
        default_factory=list,
        metadata={
            "name": "AdditionalInformation",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


    source_object_information: List[HeaderSourceObjectInformation] = field(
        default_factory=list,
        metadata={
            "name": "SourceObjectInformation",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


    revision: Optional[List[HeaderRevision]] = field(
        default_factory=list,
        metadata={
            "name": "Revision",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )

    change_mode: ChangeMode = field(
        default=ChangeMode.STATE,
        metadata={
            "name": "ChangeMode",
            "type": "Attribute",
        }
    )



    description: HeaderDescription = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    version: HeaderVersion = field(
        default=None,
        metadata={
            "name": "Version",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    copyright: HeaderCopyright = field(
        default=None,
        metadata={
            "name": "Copyright",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


@dataclass
class AttributeTypeRefSemantic(CaexbasicObject):
    class Meta:
        global_type = False

    corresponding_attribute_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "CorrespondingAttributePath",
            "type": "Attribute",
            "required": True,
        }
    )

@dataclass
class AttributeValueRequirementType(CaexbasicObject):
    """
    Defines base structures for definition of value requirements of an
    attribute.

    :ivar ordinal_scaled_type: Element of to define constraints of
        ordinal scaled attribute values.
    :ivar nominal_scaled_type: Element of to define constraints of
        nominal scaled attribute values.
    :ivar unknown_type: Element to define constraints for attribute
        values of an unknown scale type.
    :ivar name: Describes the name of the constraint.
    """
    ordinal_scaled_type: Optional[AttributeValueRequirementTypeOrdinalScaledType] = field(
        default=None,
        metadata={
            "name": "OrdinalScaledType",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    nominal_scaled_type: Optional[AttributeValueRequirementTypeNominalScaledType] = field(
        default=None,
        metadata={
            "name": "NominalScaledType",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    unknown_type: Optional[AttributeValueRequirementTypeUnknownType] = field(
        default=None,
        metadata={
            "name": "UnknownType",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CaexfileExternalReference(CaexbasicObject):
    """
    :ivar path: Describes the path of the external CAEX file. Absolute
        and relative paths are allowed.
    :ivar alias: Describes the alias name of an external CAEX file to
        enable referencing elements of the external CAEX file.
    """
    class Meta:
        global_type = False

    path: Optional[str] = field(
        default=None,
        metadata={
            "name": "Path",
            "type": "Attribute",
            "required": True,
        }
    )
    alias: Optional[str] = field(
        default=None,
        metadata={
            "name": "Alias",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass(kw_only=True)
class Caexobject(CaexbasicObject):
    """
    CAEX basis object derived from CAEXBasicObject, augmented by Name
    (required) and ID (optional).

    :ivar id: Optional attribute that describes a unique identifier of
        the CAEX object.
    :ivar name: Describes the name of the CAEX object.
    """
    class Meta:
        name = "CAEXObject"

    id: str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Attribute",
        }
    )
    name: str = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class MappingTypeAttributeNameMapping(CaexbasicObject):
    class Meta:
        global_type = False

    system_unit_attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemUnitAttributeName",
            "type": "Attribute",
            "required": True,
        }
    )
    role_attribute_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoleAttributeName",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class MappingTypeInterfaceIdmapping(CaexbasicObject):
    class Meta:
        global_type = False

    system_unit_interface_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "SystemUnitInterfaceID",
            "type": "Attribute",
            "required": True,
        }
    )
    role_interface_id: Optional[str] = field(
        default=None,
        metadata={
            "name": "RoleInterfaceID",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AttributeInstance(Caexobject):
    """
    Defines base structures for attribute definitions.

    :ivar default_value: A predefined default value for an attribute.
    :ivar value: Element describing the value of an attribute.
    :ivar ref_semantic: A reference to a definition of a defined
        attribute, e. g. to an attribute in a standardized library, this
        allows the semantic definition of the attribute.
    :ivar constraint: Element to restrict the range of validity of a
        defined attribute.
    :ivar attribute: Element that allows the description of nested
        attributes.
    :ivar unit: Describes the unit of the attribute.
    :ivar attribute_data_type: Describes the data type of the attribute
        using XML notation.
    :ivar ref_attribute_type: References an attribute type in the
        attribute library.
    """
    attribute: Optional[List["AttributeInstance"]] = field(
        default_factory=list,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )

    constraint: List[AttributeValueRequirementType] = field(
        default_factory=list,
        metadata={
            "name": "Constraint",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    
    default_value: str = field(
        default=None,
        metadata={
            "name": "DefaultValue",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    value: str = field(
        default=None,
        metadata={
            "name": "Value",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    ref_semantic: Optional[List[AttributeTypeRefSemantic]] = field(
        default=None,
        metadata={
            "name": "RefSemantic",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )

    unit: Optional[str] = field(
        default=None,
        metadata={
            "name": "Unit",
            "type": "Attribute",
        }
    )
    attribute_data_type: Optional[str] = field(
        default="xs:string",
        metadata={
            "name": "AttributeDataType",
            "type": "Attribute",
        }
    )
    ref_attribute_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefAttributeType",
            "type": "Attribute",
        }
    )


@dataclass
class MappingType(CaexbasicObject):
    """
    Base element for AttributeNameMapping and InterfaceIDMapping.

    :ivar attribute_name_mapping: Allows the definition of the mapping
        between attributes of a related role class or its interfaces and
        attributes of the hosting system unit
    :ivar interface_idmapping: Allows the definition of the mapping
        between interfaces of a related role class and interfaces of the
        hosting system unit.
    """
    attribute_name_mapping: List[MappingTypeAttributeNameMapping] = field(
        default_factory=list,
        metadata={
            "name": "AttributeNameMapping",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    interface_idmapping: List[MappingTypeInterfaceIdmapping] = field(
        default_factory=list,
        metadata={
            "name": "InterfaceIDMapping",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


@dataclass
class SystemUnitClassTypeInternalLink(Caexobject):
    class Meta:
        global_type = False

    ref_partner_side_a: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefPartnerSideA",
            "type": "Attribute",
            "required": True,
        }
    )
    ref_partner_side_b: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefPartnerSideB",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class AttributeType(AttributeInstance):
    """
    Defines base structures for attribute type definitions.
    """
    attribute_type: List["AttributeType"] = field(
        default_factory=list,
        metadata={
            "name": "AttributeType",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
            "required": "False"
        }
    )



@dataclass
class InterfaceClassType(Caexobject):
    """
    Shall be used for InterfaceClass definition, provides base structures for
    an interface class definition.

    :ivar attribute: Characterizes properties of the InterfaceClass.
    :ivar external_interface:
    :ivar ref_base_class_path: Stores the reference of a class to its
        base class. References contain the full path to the referred
        class object.
    """
    attribute: List[AttributeInstance] = field(
        default_factory=list,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    external_interface: List["InterfaceClassType"] = field(
        default_factory=list,
        metadata={
            "name": "ExternalInterface",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    ref_base_class_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefBaseClassPath",
            "type": "Attribute",
        }
    )


@dataclass
class SystemUnitClassTypeSupportedRoleClass(CaexbasicObject):
    class Meta:
        global_type = False

    mapping_object: Optional[MappingType] = field(
        default=None,
        metadata={
            "name": "MappingObject",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    ref_role_class_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefRoleClassPath",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class CaexfileAttributeTypeLib(Caexobject):
    """
    :ivar attribute_type: Class definition for attribute Types
    """
    # class Meta:
    #     global_type = False

    attribute_type: List[AttributeType] = field(
        default_factory=list,
        metadata={
            "name": "AttributeType",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


@dataclass
class InterfaceFamilyType(InterfaceClassType):
    """Defines base structures for a hierarchical InterfaceClass tree.

    The hierarchical structure of an interface library has
    organizational character only.

    :ivar interface_class: Element that allows definition of child
        InterfaceClasses within the class hierarchy. The parent child
        relation between two InterfaceClasses has no semantic.
    """
    interface_class: List["InterfaceFamilyType"] = field(
        default_factory=list,
        metadata={
            "name": "InterfaceClass",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


@dataclass
class InternalElementTypeRoleRequirements(CaexbasicObject):
    """
    :ivar attribute: Characterizes properties of the RoleRequirements.
    :ivar external_interface:
    :ivar mapping_object: Host element for AttributeNameMapping and
        InterfaceIDMapping.
    :ivar ref_base_role_class_path:
    """
    class Meta:
        global_type = False

    attribute: List[AttributeInstance] = field(
        default_factory=list,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    external_interface: List[InterfaceClassType] = field(
        default_factory=list,
        metadata={
            "name": "ExternalInterface",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    mapping_object: Optional[MappingType] = field(
        default=None,
        metadata={
            "name": "MappingObject",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    ref_base_role_class_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefBaseRoleClassPath",
            "type": "Attribute",
            "required": True,
        }
    )


@dataclass
class RoleClassTypeExternalInterface(InterfaceClassType):
    class Meta:
        global_type = False




@dataclass(kw_only=True)
class InternalElementType(Caexobject):
    """Defines base structures for a hierarchical object instance.

    The instance maybe part of the InstanceHierarchy or a
    SystemUnitClass.

    :ivar role_requirements: Describes role requirements of an
        InternalElement. It allows the definition of a reference to a
        RoleClass and the specification of role requirements like
        required attributes and required interfaces.
    :ivar ref_base_system_unit_path: Stores the reference of an
        InternalElement to a class or instance definition. References
        contain the full path information.
    """
    attribute: List[AttributeInstance] = field(
        default_factory=list,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    external_interface: List[InterfaceClassType] = field(
        default_factory=list,
        metadata={
            "name": "ExternalInterface",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    internal_element: List["InternalElementType"] = field(
        default_factory=list,
        metadata={
            "name": "InternalElement",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    supported_role_class: List[SystemUnitClassTypeSupportedRoleClass] = field(
        default_factory=list,
        metadata={
            "name": "SupportedRoleClass",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    internal_link: List[SystemUnitClassTypeInternalLink] = field(
        default_factory=list,
        metadata={
            "name": "InternalLink",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


    role_requirements: List[InternalElementTypeRoleRequirements] = field(
        default_factory=list,
        metadata={
            "name": "RoleRequirements",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    ref_base_system_unit_path: str = field(
        default=None,
        metadata={
            "name": "RefBaseSystemUnitPath",
            "type": "Attribute",
        }
    )

@dataclass(kw_only=True)
class InternalElement(InternalElementType):
    pass

@dataclass
class SystemUnitClassType(Caexobject):
    """
    Defines base structures for a SystemUnit class definition.

    :ivar attribute: Characterizes properties of the SystemUnitClass.
    :ivar external_interface: Description of an external interface.
    :ivar internal_element: Shall be used in order to define nested
        objects inside of a SystemUnitClass or another InternalElement.
        Allows description of the internal structure of a CAEX object.
    :ivar supported_role_class: Allows the association to a RoleClass
        which this SystemUnitClass can play. A SystemUnitClass may
        reference multiple roles.
    :ivar internal_link: Shall be used in order to define the
        relationships between internal interfaces of InternalElements.
    """
    attribute: List[AttributeInstance] = field(
        default_factory=list,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    external_interface: List[InterfaceClassType] = field(
        default_factory=list,
        metadata={
            "name": "ExternalInterface",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    internal_element: List[InternalElementType] = field(
        default_factory=list,
        metadata={
            "name": "InternalElement",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    supported_role_class: List[SystemUnitClassTypeSupportedRoleClass] = field(
        default_factory=list,
        metadata={
            "name": "SupportedRoleClass",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    internal_link: List[SystemUnitClassTypeInternalLink] = field(
        default_factory=list,
        metadata={
            "name": "InternalLink",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


@dataclass
class CaexfileInterfaceClassLib(Caexobject):
    """
    :ivar interface_class: Class definition for interfaces.
    """
    class Meta:
        global_type = False

    interface_class: List[InterfaceFamilyType] = field(
        default_factory=list,
        metadata={
            "name": "InterfaceClass",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )

@dataclass
class RoleClassType(Caexobject):
    """
    Shall be used for RoleClass definition, provides base structures for a role
    class definition.

    :ivar attribute: Characterizes properties of the RoleClass.
    :ivar external_interface: Description of an external interface.
    :ivar ref_base_class_path: Stores the reference of a class to its
        base class. References contain the full path to the referred
        class object.
    """
    attribute: List[AttributeInstance] = field(
        default_factory=list,
        metadata={
            "name": "Attribute",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    external_interface: List[RoleClassTypeExternalInterface] = field(
        default_factory=list,
        metadata={
            "name": "ExternalInterface",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    ref_base_class_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefBaseClassPath",
            "type": "Attribute",
        }
    )


@dataclass
class SystemUnitFamilyType(SystemUnitClassType):
    """Defines base structures for a hierarchical SystemUnitClass tree.

    The hierarchical structure of a SystemUnit library has
    organizational character only.

    :ivar system_unit_class: Element that allows definition of child
        SystemUnitClasses within the class hierarchy. The parent child
        relation between two SystemUnitClasses has no semantic.
    :ivar ref_base_class_path: Stores the reference of a class to its
        base class. References contain the full path to the referred
        class object.
    """
    system_unit_class: List["SystemUnitFamilyType"] = field(
        default_factory=list,
        metadata={
            "name": "SystemUnitClass",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )
    ref_base_class_path: Optional[str] = field(
        default=None,
        metadata={
            "name": "RefBaseClassPath",
            "type": "Attribute",
        }
    )


@dataclass
class CaexfileInstanceHierarchy(Caexobject):
    """
    :ivar internal_element: Shall be used in order to define nested
        objects inside of a SystemUnitClass or another InternalElement.
        Allows description of the internal structure of a CAEX object.
    """
    class Meta:
        global_type = False

    internal_element: List[InternalElementType] = field(
        default_factory=list,
        metadata={
            "name": "InternalElement",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


@dataclass
class CaexfileSystemUnitClassLib(Caexobject):
    """
    :ivar system_unit_class: Shall be used for SystemUnitClass
        definition, provides definition of a class of a SystemUnitClass
        type.
    """
    class Meta:
        global_type = False

    system_unit_class: List[SystemUnitFamilyType] = field(
        default_factory=list,
        metadata={
            "name": "SystemUnitClass",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


@dataclass
class RoleFamilyType(RoleClassType):
    """Defines base structures for a hierarchical RoleClass tree.

    The hierarchical structure of a role library has organizational
    character only.

    :ivar role_class: Element that allows definition of child
        RoleClasses within the class hierarchy. The parent child
        relation between two RoleClasses has no semantic.
    """
    role_class: List["RoleFamilyType"] = field(
        default_factory=list,
        metadata={
            "name": "RoleClass",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


@dataclass
class CaexfileRoleClassLib(Caexobject):
    """
    :ivar role_class: Definition of a class of a role type.
    """
    class Meta:
        global_type = False

    role_class: List[RoleFamilyType] = field(
        default_factory=list,
        metadata={
            "name": "RoleClass",
            "type": "Element",
            "namespace": "http://www.dke.de/CAEX",
        }
    )


@dataclass
class Caexfile(CaexbasicObject):
    """
    Root-element of the CAEX schema.

    :ivar superior_standard_version: Describes the version of a superior
        standard, e.g. AutomationML x.y. The version string is defined
        in the superior standard.
    :ivar source_document_information: Provides information about the
        source(s) of the CAEX document.
    :ivar external_reference: Container element for the alias definition
        of external CAEX files.
    :ivar instance_hierarchy: Root element for a system hierarchy of
        object instances.
    :ivar interface_class_lib: Container element for a hierarchy of
        InterfaceClass definitions. It shall contain any interface class
        definitions. CAEX supports multiple interface libraries.
    :ivar role_class_lib: Container element for a hierarchy of RoleClass
        definitions. It shall contain any RoleClass definitions. CAEX
        supports multiple role libraries.
    :ivar system_unit_class_lib: Container element for a hierarchy of
        SystemUnitClass definitions. It shall contain any
        SystemunitClass definitions. CAEX supports multiple
        SystemUnitClass libraries.
    :ivar attribute_type_lib: Container element for a hierarchy of
        Attribute type definitions. CAEX supports multiple attribute
        type libraries.
    :ivar schema_version: Describes the version of the schema. Each CAEX
        document must specify which CAEX version it requires. The
        version number of a CAEX document must fit to the version number
        specified in the CAEX schema file.
    :ivar file_name: Describes the name of the CAEX file.
    """
    class Meta:
        name = "CAEXFile"
        namespace = "http://www.dke.de/CAEX"

    superior_standard_version: List[str] = field(
        default_factory=list,
        metadata={
            "name": "SuperiorStandardVersion",
            "type": "Element",
        }
    )
    source_document_information: List[SourceDocumentInformationType] = field(
        default_factory=list,
        metadata={
            "name": "SourceDocumentInformation",
            "type": "Element",
            "min_occurs": 1,
        }
    )
    external_reference: List[CaexfileExternalReference] = field(
        default_factory=list,
        metadata={
            "name": "ExternalReference",
            "type": "Element",
        }
    )
    instance_hierarchy: List[CaexfileInstanceHierarchy] = field(
        default_factory=list,
        metadata={
            "name": "InstanceHierarchy",
            "type": "Element",
        }
    )
    interface_class_lib: List[CaexfileInterfaceClassLib] = field(
        default_factory=list,
        metadata={
            "name": "InterfaceClassLib",
            "type": "Element",
        }
    )
    role_class_lib: List[CaexfileRoleClassLib] = field(
        default_factory=list,
        metadata={
            "name": "RoleClassLib",
            "type": "Element",
        }
    )
    system_unit_class_lib: List[CaexfileSystemUnitClassLib] = field(
        default_factory=list,
        metadata={
            "name": "SystemUnitClassLib",
            "type": "Element",
        }
    )
    attribute_type_lib: List[CaexfileAttributeTypeLib] = field(
        default_factory=list,
        metadata={
            "name": "AttributeTypeLib",
            "type": "Element",
        }
    )
    schema_version: str = field(
        init=False,
        default="3.0",
        metadata={
            "name": "SchemaVersion",
            "type": "Attribute",
            "required": True,
        }
    )
    file_name: Optional[str] = field(
        default=None,
        metadata={
            "name": "FileName",
            "type": "Attribute",
            "required": True,
        }
    )